# IoT Moments: Hack your Car

**Published:** October 2025
**Categories:** Internet of Things, technology
**Tags:** Internet of Things, Technology

---

**Copyright © 2025 Ivan Judson. All Rights Reserved.**

This blog post and all original images are protected by copyright. See [COPYRIGHT.md](../COPYRIGHT.md) for details.

---

This is a tutorial on how to do basic telemetry collection from your automobile leveraging the diagnostic port that's on almost every car out there. Here's what you need:

- Android Tablet with Bluetooth, Cellular, and running Android

- An ODB-II to Bluetooth adapter. I used PLX -

- Torque, an ODB-II application for android.

- A car manufactured after 1986.

- An account at nitrogen.io.

I'll describe this process in a tutorial so that it's easy to see the various parts. First, let me describe what's going on.

Every car manufactured after 1986 as a diagnostic port somewhere near the driver side dashboard. It's typically mounted discreetly because only mechanics need to access it. However, this port can be used for a variety of information -- some of it documented, most of it not.

In order to measure car efficiency the EPA mandated that a basic set of data be standardized and made available via the ODB-II protocol. This data is what we'll collect. It is possible, in fact likely, that your car is trying to share more data with you using the CAN bus and other protocols that haven't been published by your auto maker. We can't access these without documentation or reverse engineering -- which is not covered here.

This data from your car is going to be accessed using the ODB-II to Bluetooth adapter (item #2 in the list above) and transmitted to the android tablet (via Bluetooth). The Torque application is going to recieve that information via Bluetooth, display it via dashboards, maps, etc and upload it to Nitrogen.

Nitrogen is going to collect this data and make it available to you for other applications.

Here's how to make this work:

-

---

*This post was migrated from WordPress. Original publication date: 2025-10-26 22:29:29*
