# Adding Face Detection to your Pi Powered Motion Detector

**Published:** October 2025
**Categories:** Internet of Things
**Tags:** Internet of Things, Technology

---

**Copyright © 2025 Ivan Judson. All Rights Reserved.**

This blog post and all original images are protected by copyright. See [COPYRIGHT.md](../COPYRIGHT.md) for details.

---

Back during //build 2015 I was playing with our Oxford API's and in parallel building some Raspbery Pi based AllJoyn projects. During that time I started fiddling with Oxford via Python and built a face detector for the [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) app.

Here's how to build your own:

- [Install Raspian on sd card](https://www.raspberrypi.org/documentation/installation/installing-images/)

- Install Camera, Wifi adapter, sdcard into Raspberry Pi

- Login, raspi-config, ssh, etc

- [Configure wireless](http://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/)

- Update software and install motion:

`sudo apt-get update
sudo apt-get upgrade
sudo apt-get install motion`

Now you're ready to add some magic.

Modify the configuration file, /etc/motion/motion.conf, around line 510 you should see this block (this is what mine looks like):

`# Command to be executed when a picture (.ppm|.jpg) is saved (default: none)
# To give the filename as an argument to a command append it with %fon_picture_save sh /home/pi/oxford/motion-picture-save.sh %f`

So, I've told the Motion software that when it captures a picture it should invoke the motion-picture-save.sh script passing the name of the file as an argument.

Here's what's in that shell script:

`#!/usr/bin/env bash
#echo -n "Invoking face detector with file "
echo $1/usr/bin/python /home/pi/oxford/oxford.py $1`

and in the oxford.py script:

```
`#!/usr/bin/env python
#import sys
import urllib
import json
import requests

url = "https://api.projectoxford.ai/face/v0/detections"
headers = {
    'Content-type': 'application/octet-stream',
}
params = urllib.urlencode({    
    # Specify your subscription key
    'subscription-key': '',
    # Specify values for optional parameters, as needed    
    'analyzesFaceLandmarks': 'true',    
    'analyzesAge': 'true',    
    'analyzesGender': 'true',    
    'analyzesHeadPose': 'true',})

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:    
    print("You need to pass a filename into the script.")    
    sys.exit(0)
    
payload = open(filename, "rb").read()
try:    
    resp = requests.post(url, params=params, data=payload, headers=headers)    
    print resp.json()
except Exception as e:    
    print("[Errno {0}] {1}".format(e.errno, e.strerror))`
```

---

*This post was migrated from WordPress. Original publication date: 2025-10-26 22:29:26*
