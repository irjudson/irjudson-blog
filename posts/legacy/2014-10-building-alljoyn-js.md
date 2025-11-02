# Building Alljoyn-js

**Published:** October 2014
**Categories:** Uncategorized
**Tags:** Technology

---

**Copyright © 2014 Ivan Judson. All Rights Reserved.**

This blog post and all original images are protected by copyright. See [COPYRIGHT.md](../COPYRIGHT.md) for details.

---

The [AllSeen Alliance's](https://allseenalliance.org) [AllJoyn](https://www.alljoyn.org) protocol is designed to enable the "everything" in the Internet of Everything to find and talk with one another. We've been working with AllJoyn for a couple of reasons:

- Microsoft is a member of the AllSeen Alliance

- We have Startups in the Microsoft Ventures Seattle Accelerator who are using AllJoyn for their devices.

As a result of these facts, we've decided we should spend some time looking into the state of AllJoyn and specifically, how easy it is to use AllJoyn if you are developing within or near our ecosystem.

The first thing we noticed was the alljoyn bits hadn't been compiled for windows 8.1 (or even less recent versions of our platform) - so we started there. Back in September at our AllJoyn hackfest in Paris.

Since then we've been working on more help, identifying areas of weakness that seem to be place others could use help (because we could have used it). So what I have available at [github](https://github.com/irjudson/alljoyn-scripts.git).

In this repo are three scripts:

- **get_alljoyn.sh** - run this on the command prompt or if running on windows, run this from the git shell (a bash shell).

- **build_alljoyn.sh** / **build_alljoyn.bat** - run the appropriate script for your platform - indicating platform and architecture. This script when given a reasonable platform (darwin or linux) and a correct architecture (x86 or x86_64), will build the ajtcl, alljoyn core, and alljoyn-js code on OS X and Ubuntu and build ajtcl on Windows.

What is AllJoyn-JS, it's not on the AllSeen [download](https://allseenalliance.org/source-code) page?

AllJoyn-JS is, from what I can glean from the docs, a simple AllJoyn library that appears to build cross-platform plus a Javascript API that calls into the library. Here are the links I can find on their wiki that relate to AllJoyn-JS:

- [The Hackfest Resources Page](https://wiki.allseenalliance.org/develop/hackfests)

- [The AllJoyn-JS Project Page](https://wiki.allseenalliance.org/develop/hackfests/alljoyn-js)

- [The Getting Started with AllJoyn-JS Page](https://git.allseenalliance.org/cgit/core/alljoyn-js.git/plain/doc/html/Getting%20Started%20with%20AllJoyn.js.html)

From these sources I put together and tested the build script above. Hopefully, it will be useful to others as they start to use AllJoyn.

For more background see posts by my coworkers:

[From Mario](http://blog.mszcool.com/index.php/2014/09/alljoyn-iot-peer-to-peer-protocol-framework-making-it-work-with-visual-studio-2013/)

[From Rachel](http://azure.microsoft.co.il/?p=164/)

---

*This post was migrated from WordPress. Original publication date: 2014-10-22 13:20:34*
