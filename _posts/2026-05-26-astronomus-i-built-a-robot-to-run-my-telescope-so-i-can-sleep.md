---
title: "Astronomus: I Built a Robot to Run My Telescope So I Can Sleep"
date: 2026-05-26 09:00:00 -0600
categories: [Projects, Astronomy]
tags: ["astronomy", "astrophotography", "python", "ai", "seestar", "side-project", "buffalo-jump-forge"]
image:
  path: /assets/img/posts/astronomus/grid.jpg
  alt: "A night's worth of deep sky objects captured by Astronomus"
---

I've been doing astrophotography for a while now. It started as a hobby and quickly became an obsession, the way these things do. The problem is that astrophotography has a lot of friction — planning which targets are up tonight, figuring out when they'll be optimally positioned, checking weather, watching satellite tracks, staying up until 2am to babysit the scope so it doesn't point into a tree or decide the neighbor's porch light is interesting. The more friction between me and something I love, the less of it I actually do.

So I did what any reasonable person does when a hobby gets annoying: I spent way more time than the hobby was costing me to build a system that removes the friction entirely. Meet [Astronomus](https://github.com/irjudson/astronomus).

## What It Actually Does

Astronomus is an intelligent session planner for the [ZWO Seestar S50](https://www.zwoptical.com/goods/detail?id=175) — a smart telescope that's basically a camera, mount, and optics in one sealed unit. The S50 is remarkable for what it is: point it at the sky, tell it what you want to image, and it handles tracking, stacking, and even some basic processing. The catch is that the software that comes with it is designed for casual users, not for someone who wants to image 20 objects a night automatically.

That's the gap Astronomus fills. Here's what it does on a typical evening:

1. At noon every day, it generates an optimized observation plan for that night. Not just "what's up" — it runs a greedy scheduling algorithm with urgency-based lookahead across **12,400+ objects** from the OpenNGC catalog, Caldwell, Arp Atlas, Sharpless HII regions, and more. It accounts for my local horizon profile (measured by scanning the actual sky/terrain brightness ratio with the scope itself), satellite avoidance using live Celestrak TLEs, moon phase, weather forecasts, and field rotation on an alt-az mount.

2. At astronomical twilight — the exact computed moment, not "around 9pm" — Celery Beat kicks off the session automatically. It TCP-pings the S50 to make sure it's connected, retrying every 5 minutes for up to 6 attempts. If it can't reach the scope, I get a notification. If the weather watchdog sees rain, excessive wind, or high humidity, it aborts cleanly.

3. The plan gets pushed directly to the scope via the `set_plan` API — a **"Send to Scope"** button in the web UI that uploads the night's schedule over WiFi. Then it just runs.

4. I go to bed. In the morning I see what was captured.

That last step is the whole point. I'm not babysitting anything. The scope is out in the yard doing its thing while I sleep.

## The Results

Here's what a November night produced. These are the actual processed outputs — FITS files stacked with CUDA-accelerated sigma-clipped mean stacking, auto-stretched to match Seestar's native output.

**M81 (Bode's Galaxy)** — 34 frames stacked, about 5.7 minutes total integration:

![M81 Bode's Galaxy captured by Astronomus](/assets/img/posts/astronomus/m81.jpg)
_M81, 34 × 10s, IRCUT filter_

**M31 (Andromeda)** — 64 frames, mosaic:

![M31 Andromeda Galaxy captured by Astronomus](/assets/img/posts/astronomus/m31.jpg)
_M31, 64 × 10s mosaic, IRCUT filter_

**M33 (Triangulum Galaxy)** — 775 frames, mosaic. This one took a while:

![M33 Triangulum Galaxy captured by Astronomus](/assets/img/posts/astronomus/m33.jpg)
_M33, 775 × 10s mosaic, IRCUT filter_

**NGC 1499 (California Nebula)** — 406 frames through a light pollution filter:

![NGC 1499 California Nebula captured by Astronomus](/assets/img/posts/astronomus/ngc1499.jpg)
_NGC 1499, 406 × 10s mosaic, LP filter_

And here's a grid of everything from that session:

![Astrophotography grid from a single night with Astronomus](/assets/img/posts/astronomus/grid.jpg)
_A night's work, unattended_

None of that required me to stay up. The scope just worked through the list.

## The Stack

If you're curious what's under the hood:

- **FastAPI** backend with Celery for task scheduling and Beat for cron jobs
- **Vue 3 SPA** for the web UI — tonight view, sky map, interactive timeline, plan editor
- **PostgreSQL** for the object catalog and session history
- **CuPy/CUDA** for FITS stacking (this made a huge difference in processing speed)
- **7Timer** for astronomical seeing forecasts, **Open-Meteo** for 7-day weather, and my **Ambient Weather WS-2902** local station for ground truth on conditions
- **Celestrak TLEs** for satellite avoidance — this matters more than you'd think; ISS will ruin a frame
- Direct Seestar WiFi API for telescope control: goto, capture, focus, gain, dew heater, and the horizon scan

The UI has a live now-marker that advances in real time during an active session, a NowPlayingPanel showing the current and next target with frame progress, and a drag-to-edit timeline with real-time conflict detection if you want to adjust the plan mid-session.

## Standing on Shoulders

None of this would exist without the [seestar_alp](https://github.com/smart-underworld/seestar_alp) community. As ZWO's software updates progressively closed off direct access to the S50, they stepped in to keep it open for builders. They reverse-engineered the protocol, documented everything, and maintain an active [Discord](https://discord.gg/seestar) that's genuinely generous and technically sharp. Astronomus is my contribution back to that ecosystem.

If you have a Seestar and you're not in that Discord, find it.

## On Building With AI

I built Astronomus with [Claude](https://claude.ai) as a genuine collaborator throughout — and I want to be specific about what that means, because "I used AI" covers a lot of ground.

Requirements discussions before I wrote a line of code. Test-driven development, not vibes-driven development. Careful engineering from start to finish. The AI didn't write sloppy code that I shipped anyway — we worked through design decisions together, caught problems early, and I reviewed everything. The process produced something I'm proud of, not a prototype I'm embarrassed to show people.

There's a lot of anxiety in the conversation around AI right now, and I understand it. But I keep coming back to this: the most useful thing any of us can do is pick something we care about and build it — seriously, with good engineering discipline — and see what's actually possible. Astronomus took me from idea to a working system that runs unattended every clear night. That's what's possible.

The code is on [GitHub](https://github.com/irjudson/astronomus). If you're a Seestar owner and want to try it, the [Quick Start](https://github.com/irjudson/astronomus/blob/main/QUICK_START.md) will get you running.

Clear skies.
