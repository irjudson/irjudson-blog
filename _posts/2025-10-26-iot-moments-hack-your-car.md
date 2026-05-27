---
title: "IoT Moments: Hack your Car"
date: 2025-10-26 22:29:29 +0000
categories: [Internet of Things]
tags: ["iot", "obd-ii", "nitrogen", "android", "telemetry", "hardware"]
---

This is a tutorial on how to do basic telemetry collection from your automobile using the diagnostic port that's on almost every car out there. Here's what you need:

- Android tablet with Bluetooth and cellular
- An [OBD-II to Bluetooth adapter](http://www.plxdevices.com/product_info.php?id=KWBT) — I used the PLX Kiwi Bluetooth
- [Torque](https://play.google.com/store/apps/details?id=org.prowl.torque) — an OBD-II app for Android
- A car manufactured after 1996 (OBD-II was federally mandated that year)
- A [Nitrogen.io](https://nitrogen.io) account

## What's actually going on

Every car manufactured after 1996 has a diagnostic port somewhere near the driver side dashboard, usually tucked away discreetly since it's technically for mechanics. But this port is a goldmine of data — the EPA mandated a standard set of diagnostics be accessible via OBD-II so emissions and fuel efficiency could be monitored. That's what we're tapping into.

The data pipeline looks like this:

**Car → OBD-II Bluetooth adapter → Android (via Bluetooth) → Torque → Nitrogen.io**

Torque reads the data from the OBD-II adapter over Bluetooth, displays it in dashboards and maps in real time, and ships it up to Nitrogen where you can query it, build apps on top of it, or just watch your driving patterns over time.

It's worth knowing: your car almost certainly broadcasts more than the OBD-II standard. The CAN bus carries manufacturer-specific data that hasn't been published. Getting at that requires documentation (rarely available) or reverse engineering (out of scope here). But the standard OBD-II data — speed, RPM, fuel consumption, coolant temp, throttle position, and more — is plenty to work with.

## Step 1: Connect the OBD-II adapter

Plug the PLX Kiwi (or your adapter of choice) into the OBD-II port under the dash. Turn the car to accessory mode or start the engine — the adapter needs power to broadcast. Most adapters have an LED that goes solid or starts blinking when they're active.

## Step 2: Pair Bluetooth on Android

On your Android tablet, go to **Settings → Bluetooth** and scan for devices. The PLX Kiwi shows up as something like `OBDII` or `PLX Kiwi`. Pair it — default PIN is usually `1234` or `0000`.

## Step 3: Configure Torque

Install Torque from the Play Store and open it. Go to **Settings → OBD2 Adapter Settings**:

- Connection type: **Bluetooth**
- Select your adapter from the list

Back in main settings, go to **Data Logging & Upload → Webserver Settings**:

- Enable upload: **on**
- Upload URL: `https://[your-nitrogen-device-id].nitrogen.io/logs`
- Upload interval: every 1–5 seconds depending on how much data you want

Torque will start pushing readings to Nitrogen as soon as it connects to the adapter and has a data signal.

## Step 4: Set up Nitrogen

Sign up at [nitrogen.io](https://nitrogen.io) and create a new device to represent your car. Nitrogen will give you an API key and endpoint. Use those in the Torque upload URL above.

Once data starts flowing you can query it from the Nitrogen dashboard or build against the [Nitrogen API](https://github.com/irjudson/nitrogen) directly. The time-series data is stored per device and queryable by time range, message type, or custom fields Torque includes in its uploads.

## What you'll see

After a drive you'll have a stream of messages in Nitrogen containing things like:

- Vehicle speed (km/h or mph)
- Engine RPM
- Throttle position
- Fuel consumption rate
- Coolant temperature
- GPS position (if your tablet has GPS)
- Calculated metrics Torque derives: fuel economy, horsepower, torque (yes, really)

From there you can build dashboards, correlate fuel economy with routes, or just satisfy curiosity about what your car is actually doing. The fact that this is all running on a $30 adapter and a free IoT platform is the part that still impresses me.

## What you can't see

As mentioned, manufacturer-specific data lives on the CAN bus and isn't accessible this way. If your car has a sport mode, adaptive suspension, or anything proprietary, that data isn't coming through OBD-II. Some cars (mostly German, BMW especially) have more accessible CAN data — there's a whole community around that — but that's a different project.

This is a good starting point. The data is real, the setup takes about 20 minutes, and once it's running it runs automatically every time you drive.
