# CodaLab

**Published:** September 2014
**Categories:** Uncategorized
**Tags:** Technology

---

**Copyright © 2014 Ivan Judson. All Rights Reserved.**

This blog post and all original images are protected by copyright. See [COPYRIGHT.md](../COPYRIGHT.md) for details.

---

[CodaLab](http://codalab.org/) is a project to make Machine Learning simple, reproducable, and scalable. It focuses both on "bench" science in ML and supporting competitions to enable the community to work together to find the best solutions to hard problems.

For almost a year I worked on CodaLab as part of the [Microsoft Research Outreach](http://research.microsoft.com/en-us/projects/codalab/) team. My focus was on enabling CodaLab to be a competition platform that allows participants (and competition hosts) to run competitions that compare algorithms to solve problems.

Enabling a cloud platform to executed user code safely while preventing resource abuse and cheating and making it possible for users to customize the experience were challenges we had to overcome that hadn't been tackled before. Systems like [Kaggle](http://www.kaggle.com/) provide a basic platform for these activities, but we didn't find a cloud-backed execution platform out there - so we built one.

Another piece of CodaLab that makes it interesting is the implementation of Percy Liang's vision of a digital notebook for machine learning experimentation. This notebook is both a command line and web-based system that allows investigators to seamlessly explore new algorithm ideas and test them out on their local machine and when they are ready promote them to the hosted CodaLab platform for sharing with others and executing at scale.

We delivered an excellent piece of software and the adoption has been consistently increasing. Go checkout [CodaLab](http://www.codalab.org/), it's still under active development!

---

*This post was migrated from WordPress. Original publication date: 2014-09-26 13:43:04*
