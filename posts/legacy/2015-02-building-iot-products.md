# Building IoT Products

**Published:** February 2015
**Categories:** Internet of Things
**Tags:** Internet of Things, Technology

---

**Copyright © 2015 Ivan Judson. All Rights Reserved.**

This blog post and all original images are protected by copyright. See [COPYRIGHT.md](../COPYRIGHT.md) for details.

---

This week I gave a talk about IoT, AllJoyn, and the complexity of building products at the Linux Foundations annual Collaboration Summit. I was a bit concerned, I haven't spoken to this particular community before but I'm worked with them in the past. This was my first time participating from Micrsooft and, quite honestly, when I was a part of this community I wasn't the greatest fan of Microsoft.

It was a great event, I took my son, and we had a blast. The community was warm and welcoming and the talk was well received.

![Isaiah teaching folks how to make s](https://irjudson.org/content/images/2015/02/IsaiahLFSmores.jpg)
Building products in the IoT space is hard, very hard, for many reasons. My talk followed the following format:

- Illustrate the complexity of the IoT

- Walk through the requirements for an IoT company (a device company) to build an IoT device.

- Show how we can make that easier if we work together.

Concretely, I walked the audience through this diagram (showing the generalized architecture of IoT solutions):

![Generalized IoT Architecture](https://irjudson.org/content/images/2015/02/IoTArchitecture.png)

You can see in this diagram many moving parts; what's even more amazing is how many alternatives, companies, protocols, standards, and communities are trying to be the best for *each* of these architectural components. Some of the savvier solutions have attempted to provide solutions to multiple components with the goal of providing an end-to-end solution. That's great.

If they work together.

They don't. But worse.

They aren't even open enough to try.

So what we propose, and what my team has invested in is building a Cordova plugin for AllJoyn. This is what we're talking about at Mobile World Congress next week in Barcelona.

AllJoyn is a proximal network protocol for H2M and M2M interactions that can build a rich service layer that enables true Home Automation. A smart thermostat isn't pretty -- it disappears because the home owner doesn't need to worry about it anymore.

Successful technology fades into the background so we can live life, not tinker with knobs.

Open Standards, Open Data, and Open Source can help us get to a place where IoT product companies can select from a set of solutions without worrying about "lockin" -- freeing them up to make the *best technology decisions, without necessarily constraining business opportunities*.

One of the quotes from my talk I noticed got retweed a bit was this, which in hindsight captures why I believe we need to focus on open solutions:

"The internet of things is bigger than any of us, but it's not bigger than all of us."

---

*This post was migrated from WordPress. Original publication date: 2015-02-28 01:29:30*
