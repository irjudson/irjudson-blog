# What We Built: The Buffalo Jump Forge LED Controller

**Published:** TBD — Hold for Kickstarter Launch
**Categories:** Hardware, Entrepreneurship
**Tags:** hardware, kickstarter, led, wled, esp32, firmware, buffalo-jump-forge
**LinkedIn:** YES

---

**Copyright © 2026 Ivan Judson. All Rights Reserved.**

## SEO Metadata
- **SEO Title:** Buffalo Jump Forge LED Controller: Hardware & Firmware Deep Dive
- **Meta Description:** The full spec on the Buffalo Jump Forge LED Controller — ESP32 hardware design, WLED usermod firmware architecture, and every change between the v1 prototype and our Kickstarter build.
- **URL Slug:** buffalo-jump-forge-led-controller-hardware-firmware

---

This is the post where I stop talking about the problem and show you what we actually built.

The first two posts in this series covered why off-the-shelf LED controllers fall short for serious workshop and forge environments — cheap power stages, firmware that fights you, no real integration story. If you read those, you know the pain. This post is the payoff: the full hardware specification, the firmware architecture, how we integrated WLED, and every meaningful decision that changed between the v1 breadboard prototype and the design we're taking to Kickstarter.

No fluff. Let's get into it.

---

## The Hardware Specification

The core of the controller is an ESP32-S3 WROOM-1 module. We evaluated the original WROOM-32, the ESP32-C3, and the S3 side by side. The S3 won on three counts: it has enough GPIO to drive multiple independent LED channels without bit-banging tricks, the USB OTG support simplifies firmware flashing in the field, and the dual-core architecture gives us clean separation between the real-time LED output path and the Wi-Fi/BLE stack. When your controller is mounted in a shop with 20 other devices on the network, you want that isolation.

Power input is 12–24V DC via a ruggedized barrel connector — the same XT30 spec you'll find on power tool batteries and quality bench supplies. We chose not to chase USB-C PD for the main power rail. The firmware can tell Wi-Fi to be very chatty. USB-C PD negotiation adds latency and complexity to a path where we want clean, predictable power delivery. A separate USB-C port handles firmware updates and serial debugging only.

Output stage: four independent constant-current LED channels, each capable of driving up to 5A continuous. Each channel has its own MOSFET with overcurrent protection and a flyback diode — no shared protection that masks a fault on one channel by tripping all four. This matters in forge environments where a connector can work loose and pull intermittent load. We want to know which channel faulted, not just that something went wrong.

There's a two-wire temperature sensor header (DS18B20 protocol) on the board. We'll come back to why in the firmware section.

The PCB is a 4-layer design at 1.6mm thickness: signal, power plane, ground plane, signal. We moved to 4-layer partway through because the power and ground traces on the 2-layer v1 prototype were causing noise artifacts in the LED output at high PWM frequencies. The fix cost us about $0.80 per board at production quantities. Worth it.

Physical format is a 75×55mm board that mounts on standard 35mm DIN rail. Most shop panels already have DIN rail. We're not going to make you add a new mounting solution.

---

## Firmware Architecture

We started with WLED. If you're not familiar, WLED is an open-source ESP32/ESP8266 firmware for addressable LEDs that has become the de facto standard for DIY LED control. It supports hundreds of effects, has a solid web UI, handles OTA updates cleanly, and has a large community of contributors. Building on top of it instead of rolling our own saved us roughly six months of work on table-stakes features.

WLED uses a usermod system — essentially a plugin architecture that lets you extend the base firmware with custom code that gets called at defined points in the main loop. Usermods can register their own API endpoints, add settings to the web UI, react to LED state changes, and run their own background tasks. It's the right integration point for what we needed.

Our usermod is called `BJF_ForgeControl`. It adds four things:

**1. Channel Mapping and Zone Management**
The base WLED firmware treats your LED output as a single strip or a few segments. We needed finer control: each of our four output channels is a physically distinct circuit with independent power delivery. The usermod registers each channel as a named zone with its own current limit profile, so the web UI and the API both let you address channels by name — `forge_overhead`, `workbench_left`, `workbench_right`, `accent` — rather than by strip index. This is the difference between a product and a dev kit.

**2. Temperature-Aware Dimming**
The DS18B20 sensor header isn't decorative. The usermod polls the sensor every 500ms and maintains a running average. If ambient temperature inside the enclosure crosses a configurable threshold, the firmware linearly de-rates total LED output — reducing current draw reduces heat. If temperature hits a hard ceiling, the firmware logs the event, sends a notification via MQTT, and dims to 30% until the enclosure cools. We've seen shop environments where a closed cabinet housing a controller gets genuinely hot. We wanted software that responds to reality, not firmware that ignores the physical world until something fails.

**3. Forge Presets**
A forge workflow has distinct phases: heating, working, inspection. Each phase calls for different lighting. Heating: you want the fire visible and the ambient light low enough to read color accurately. Working: high-intensity task lighting where you need it. Inspection: even, neutral-temperature illumination to evaluate the work. We shipped twelve built-in presets tuned specifically for blacksmithing workflows, accessible via the web UI, physical button, or MQTT message. Users can also save custom presets. This is the feature that made the prototype immediately useful the first time we tested it in an actual forge.

**4. Safety Timeout**
If no input has been received — no web UI interaction, no MQTT message, no physical button press — for a configurable duration, the firmware dims to a safe idle level and logs a timeout event. A forge shop can get busy. People forget. We don't want a fully-driven LED installation running indefinitely unattended. The timeout is off by default and configurable; this isn't nannying, it's a professional feature for operators who want it.

The usermod adds approximately 18KB to the compiled firmware size. It does not meaningfully affect the base WLED loop performance — we benchmarked at 1,000 LED output cycles and saw no degradation against baseline WLED.

---

## What Changed Between v1 and the Kickstarter Design

The v1 prototype was a success by prototype standards: it worked, we learned from it, and it clearly identified everything we needed to change.

**Power connector.** v1 used a standard 5.5/2.1mm barrel jack. Fine for a lab. Not fine for a shop. Connectors get knocked loose. We moved to XT30 with a locking sleeve. The XT30 spec handles up to 30A continuous — we're nowhere near that — but the connector is rated, common, and survives being stepped on.

**Output protection.** v1 had a single shared overcurrent fuse on the output rail. One fault took down all four channels. The Kickstarter design has per-channel protection as described above. This was a non-negotiable change after we had a wiring mistake during prototyping take out the entire prototype. Discovering the failure mode in the lab is the right time to discover it.

**ESP32 module.** v1 used an ESP32-WROOM-32E. We moved to the S3 for the dual-core architecture and the GPIO count. We didn't make this call until we had the usermod far enough along to actually benchmark it. Data first.

**PCB layer count.** Already covered this: 2-layer to 4-layer. The noise artifacts at high PWM frequencies were real and repeatable, and 4-layer solved them cleanly.

**Mounting.** v1 had no defined mounting strategy — it was mounted with standoffs and zip ties during testing. The Kickstarter design has DIN rail clips integrated into the PCB edge. This is a detail that separates a product from a prototype, and it cost us almost nothing to add at design time.

**Web UI branding.** The base WLED UI is perfectly functional and looks like a hobbyist tool. We've extended it with the BJF skin — same functionality, cleaner layout for the forge-specific zones and presets, and it looks like something a shop professional would buy. Aesthetics matter when you're asking someone to put your product in their workspace.

**Documentation.** v1 had none. The Kickstarter design ships with a QR code on the board that links to the setup guide. This is not a hardware change, but it belongs on this list because it was a deliberate design decision that required knowing who we were actually building for.

---

## Conclusion

The Buffalo Jump Forge LED Controller is a real piece of hardware running real firmware on a tested PCB. It isn't a concept or a rendering — it's a thing that exists, that we've used in an actual forge, and that we're confident enough in to run a Kickstarter campaign around.

If you've been following this series, you've seen the problem space and now you've seen the solution. The next post will cover the campaign itself: pricing, tiers, timeline, and what happens after.

If you want to be notified when the campaign goes live, sign up below. We'll send exactly one email: the launch announcement.

---

# LINKEDIN VERSION

We spent months building the LED controller we couldn't buy. Here's everything that went into it. 🔨⚡

𝗪𝗵𝗮𝘁'𝘀 𝗶𝗻𝘀𝗶𝗱𝗲 the Buffalo Jump Forge LED Controller:

→ **ESP32-S3 dual-core** — clean separation between real-time LED output and Wi-Fi/BLE, no stack interference at high load
→ **4 independent 5A output channels** with per-channel overcurrent protection — one fault doesn't kill the whole board
→ **Custom WLED usermod** adds forge workflow presets, temperature-aware dimming, zone management, and safety timeout — all configurable, none mandatory
→ **XT30 power connector, DIN rail mounting, 4-layer PCB** — the decisions that separate a product from a prototype

We went from a 2-layer breadboard lash-up to a production-ready design by following the data: benchmarked the dual-core ESP32-S3 before committing, measured the PWM noise artifacts that forced the 4-layer stack, and broke a channel on the v1 prototype before adding per-channel protection.

The Kickstarter campaign is launching soon. Full hardware and firmware deep dive on the blog.

Read more → [BLOG_URL]

#hardware #esp32 #wled #kickstarter #ledcontroller #firmware #entrepreneurship #makerculture