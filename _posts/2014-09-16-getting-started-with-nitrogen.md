---
title: "Getting Started with Nitrogen"
date: 2014-09-16 18:42:50 +0000
categories: [Uncategorized]
tags: ["technology"]
---

My teammate, [Tim Park](https://twitter.com/timpark), wrote [Nitrogen](http://nitrogen.io/). I've been working with it for about a month, while hacking on lots of IoT related projects. I've got a few bits and pieces I've accumulated to make working with Nitrogen easier (for me) and its' time to share.

So, [here](http://github.com/ivanjudson/vagrant-vms) is a repository of vagrant vm configuration I'm accumulating. Once you have virtualbox installed, Nitrogen is the first VM, here's how to use it:

- You must have virtualbox installed

# Clone the repo
> git clone https://github.com/ivanjudson/vagrant-vms.git
# Get into the code
> cd vagrant-vms/nitrogen
# Add the ubuntu/trusty64 box
> vagrant add ubuntu/trusty64
# create the vm
> vagrant up

Then you can open your browser to a [local port](http://localhost:9000/) and you'll have a running instance of the Nitrogen service and admin panel.

** This does work with the parallels provider, but these are supposed to be the simplest instructions possible.

#### Things to do from here

- Build a new device

- Build a new application

Look for blog posts on these topics soon.

---

*This post was migrated from WordPress. Original publication date: 2014-09-16 18:42:50*
