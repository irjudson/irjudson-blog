---
title: "Why Every WLED Controller Ships Blind (And What It Takes to Fix That)"
date: 2026-06-09
categories: [Hardware, Technical]
tags: ["hardware", "kickstarter", "led", "wled", "electronics", "pcb", "esp32"]
series: "Buffalo Jump Forge LED Controller"
series_part: 2
image:
  path: /assets/img/posts/led-controller/board-and-enclosure.jpg
  alt: "Buffalo Jump Forge LED Controller v1.0 PCB and 3D printed enclosure"
---

*Second in a series on building the Buffalo Jump Forge LED Controller from idea to Kickstarter.*

---

<!-- [FLAG] AI setup/callback opener — "what it didn't tell us" pivot is a stock AI transition; "became clear pretty fast" is filler -->
The market research told us current monitoring was the gap. What it didn't tell us was why nobody had filled it.

Once we started designing the board, that became clear pretty fast.

## The problem

A WLED controller is basically an ESP32 with level shifters and MOSFETs. The ESP32 generates the data signal, the level shifters translate 3.3V logic to 5V for the LED strips, and the MOSFETs switch the power. The data path is well understood — WLED has been doing it for years, and the community has documented every edge case.

The power path is where things get complicated.

When you're running addressable strips at scale — multiple channels, mixed voltages, large outdoor installations — the things that go wrong are almost always power problems. A strip drawing more current than expected. A connection with marginal resistance that shows up as heat. A PSU that's undersized for a cold-start surge. <!-- [FLAG] AI dramatic personification: "None of these announce themselves" — slightly overwrought -->
None of these announce themselves. They show up as flickering, reboots, or eventually a failed component.

<!-- [FLAG] AI staccato list-as-sentences: "Per-channel draw at runtime. Total system load. Whether a channel is pulling what it should." -->
Current monitoring on every channel means you can see all of it. Per-channel draw at runtime. Total system load. Whether a channel is pulling what it should. We wanted that data in WLED natively, not as a separate instrument you clip on after the fact.

## The constraints

**I2C address space.** The INA219 has two address pins, which gives four possible addresses: 0x40, 0x41, 0x44, 0x45. Four sensors, four channels, four addresses. That's exactly the limit — no room to expand without switching to a different sensor or adding a multiplexer. The four-channel design isn't arbitrary; it's what the INA219 address space allows cleanly.

**Dual power architecture.** The controller and the LEDs need separate power. The ESP32 and logic run at 3.3V, sourced from 5V via a TPS54302 buck converter. That 5V comes from USB-C PD — the CH224K chip negotiates 9V from the charger, and the converter steps it down. The LED rail is completely separate: it comes in on its own connector, passes through a 20A Schottky diode, and distributes to the four channel outputs through the shunt resistors the INA219s measure across. Keep those two paths isolated and you avoid a whole class of ground loop and noise problems that plague LED controllers.

**Shunt resistor sizing.** The INA219 measures current by reading the voltage drop across a known resistance. Too high and you waste power and introduce voltage sag on the LED rail. Too low and you lose measurement resolution. At 0.05Ω and 3W, the shunt resistors drop 250mV at 5A — acceptable for most LED applications, and within the INA219's measurement range.

**Level shifting.** The ESP32 runs at 3.3V. WS2812B strips want 5V data signals. The TXB0108PW handles that translation on all four channels. It's bidirectional, which matters for any future protocol work, and it's fast enough not to distort the WLED timing.

**Board size.** We landed at 84 × 50mm. Small enough to fit in a standard project enclosure, large enough to route four power channels with adequate copper width for 5A each without heroic layout work.

## What we built

The v1.0 board has all of this resolved: ESP32-WROOM-32, four INA219s on I2C, CH224K USB-C PD negotiation, TPS54302 5V regulation, TXB0108PW level shifting, MBRD20100 20A Schottky on the LED power rail, NTC thermistor for thermal monitoring. 68 components, 34 unique parts, all in the JLCPCB catalog.

<!-- [FLAG] AI staccato status bullets dressed as sentences — reads like a checklist, not prose -->
DRC clean. ERC clean. Fab files generated for five manufacturers.

The WLED usermod reads all four INA219s over I2C and surfaces wattage, current, and voltage per channel into the WLED interface. <!-- [FLAG] "That's the part that doesn't exist anywhere else" — AI emphasis setup; the "Not X, not Y — Z" construction is also an AI rhythm pattern -->
That's the part that doesn't exist anywhere else. Not as a separate display, not as a log you pull after the fact — live, in the interface you're already using to control the lights.

Prototypes are being ordered this month. The bring-up plan is straightforward: verify USB-C PD negotiation, verify the buck converter output, verify I2C communication with all four sensors, validate the shunt calibration at known loads, and run each channel at full current for thermal profiling.

<!-- [FLAG] AI mic-drop closer: "What comes next is community." — punchy one-liner that sounds written, not said -->
If the board comes back the way it should, the hardware story is done. What comes next is community.

---

*Next in this series: why we're spending six months in the WLED community before touching Kickstarter, and what that actually looks like.*
