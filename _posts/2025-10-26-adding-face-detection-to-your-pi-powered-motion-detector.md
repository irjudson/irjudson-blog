---
title: "Adding Face Detection to your Pi Powered Motion Detector"
date: 2025-10-26 22:29:26 +0000
categories: [Internet of Things, Hardware]
tags: ["raspberry-pi", "computer-vision", "python", "azure", "motion-detection", "hardware"]
---

Back during [//Build 2015](https://build.microsoft.com) I was playing with the [Project Oxford APIs](https://www.projectoxford.ai) — Microsoft's computer vision platform, now called [Azure AI Vision](https://azure.microsoft.com/en-us/products/ai-services/ai-vision) — and in parallel building some Raspberry Pi based AllJoyn projects. I ended up combining them: a Pi running the [Motion](https://motion-project.github.io/) app as a security camera, with a hook that sends every captured frame through Oxford's face detection API.

Here's how to build your own.

## Hardware and software you need

- Raspberry Pi (any model with a camera connector)
- Pi Camera module or USB webcam
- WiFi adapter (if your Pi doesn't have built-in WiFi)
- A [Project Oxford / Azure AI Vision API key](https://azure.microsoft.com/en-us/products/ai-services/ai-vision)

## Step 1: Get the Pi running

1. [Install Raspberry Pi OS](https://www.raspberrypi.com/documentation/computers/getting-started.html) on an SD card
2. Connect camera, WiFi adapter (if needed), SD card
3. Boot, run `raspi-config` — enable SSH, camera, set WiFi credentials
4. [Configure wireless](https://www.raspberrypi.com/documentation/computers/configuration.html#configuring-networking) if not done in raspi-config

Update everything and install Motion:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install motion
```

## Step 2: Hook Motion to the face detector

Motion has a configuration directive that runs a shell script whenever it captures a frame. Edit `/etc/motion/motion.conf` — around line 510 you'll find the `on_picture_save` directive:

```
# Command to be executed when a picture (.ppm|.jpg) is saved (default: none)
# To give the filename as an argument to a command append it with %f
on_picture_save sh /home/pi/oxford/motion-picture-save.sh %f
```

This tells Motion to call your script with the captured filename every time motion is detected.

## Step 3: The shell script

Create `/home/pi/oxford/motion-picture-save.sh`:

```bash
#!/usr/bin/env bash
echo $1
/usr/bin/python /home/pi/oxford/oxford.py $1
```

Make it executable:

```bash
chmod +x /home/pi/oxford/motion-picture-save.sh
```

## Step 4: The face detection script

Create `/home/pi/oxford/oxford.py`. This sends the captured image to the Oxford face detection API and prints what it finds:

```python
#!/usr/bin/env python
import sys
import urllib
import json
import requests

url = "https://api.projectoxford.ai/face/v1.0/detect"
headers = {
    'Content-type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'YOUR_API_KEY_HERE',
}
params = {
    'returnFaceAttributes': 'age,gender,headPose',
    'returnFaceLandmarks': 'true',
}

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    print("Usage: oxford.py <image_file>")
    sys.exit(0)

payload = open(filename, "rb").read()
try:
    resp = requests.post(url, params=params, data=payload, headers=headers)
    faces = resp.json()
    if faces:
        for face in faces:
            attrs = face.get('faceAttributes', {})
            print("Face detected — age: {age}, gender: {gender}".format(**attrs))
    else:
        print("No faces detected")
except Exception as e:
    print("Error: {0}".format(str(e)))
```

Install the dependencies:

```bash
pip install requests
```

## Step 5: Run it

Start Motion:

```bash
sudo motion
```

Walk in front of the camera. Motion captures a frame, calls your shell script, which calls oxford.py, which hits the API and prints face attributes to the log. You'll see output like:

```
Face detected — age: 38, gender: male
```

## What this is actually useful for

On its own, printing to a log isn't that interesting. But this is a skeleton you can build on:

- **Notify on unknown faces** — store known face IDs and alert if a stranger is detected
- **Count people** — track how many distinct faces appear over time
- **Log to a database** — store detections with timestamps for later analysis
- **Push to Nitrogen or another IoT platform** — stream detections as events

The Oxford/Azure Face API also returns face landmarks, emotion attributes, and can do face identification if you train it with a person group. The [Python client library](https://github.com/irjudson/oxford) I wrote at the time wraps all of this cleanly if you want to go further than raw REST calls.

The Pi + Motion combination is solid for a low-cost always-on camera. Adding cloud vision on top of it is what turns it from a dumb motion sensor into something actually useful.
