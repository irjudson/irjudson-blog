# Hacking ESP8266's

**Published:** November 2015
**Categories:** Internet of Things
**Tags:** Internet of Things, Technology

---

**Copyright © 2015 Ivan Judson. All Rights Reserved.**

This blog post and all original images are protected by copyright. See [COPYRIGHT.md](../COPYRIGHT.md) for details.

---

I heard about ESP8266's from a friend at Google last year; I'd seen noise about them but hadn't paid any attention. Then what he said caught my attention -- using standard batteries we can make them run months, maybe more.

I started trying to come up with a good reason to get a few and play with them. Then I saw the [Huzzah](https://www.adafruit.com/products/2471) announcement and thought, heck, $10? I'll get a couple and play.

Then a colleague, was picking up a [FTDI Friend](https://www.adafruit.com/product/284) -- so I asked him to grab me one. At that point I had all the hardware I just needed a few minutes some time to figure out how to use them.

I spent last Saturday afternoon fighting these things. Nothing worked, I was fighting everything -- finding software, serial console baud rates, horrified I might have to resort to, *gasp* **AT commands**. Then Sunday afternoon, I found the #esp866 irc channel and life got good fast.

Here's a summarized version of how *I* got started, so that others don't waste the time I did:

Using these four pieces of hardware:

- [USB Cable](http://www.amazon.com/AmazonBasics-USB-2-0-Cable--Male/dp/B00NH13S44/ref=sr_1_3?ie=UTF8&qid=1447632508&sr=8-3&keywords=mini+usb+cables)

- [FTDI Friend](https://www.adafruit.com/product/284)

- [Huzzah](https://www.adafruit.com/products/2471)

- [Experiment Breadboard](http://www.amazon.com/microtivity-IB400-400-point-Experiment-Breadboard/dp/B0084A7PI8/ref=sr_1_4?ie=UTF8&qid=1447632437&sr=8-4&keywords=experiment+breadboard)

I did these things:

- Download a custom build of nodemcu, I got the default configuration of the latest build from the [NodeMCU Custom Build Service](http://frightanic.com/nodemcu-custom-build/).

- get [esptool.py](https://github.com/themadinventor/esptool.git):

`git clone https://github.com/themadinventor/esptool.git`

- Install pyserial: `pip install pyserial`

Then using esptool.py flash the nodemcu firmware to the esp8266 code. This involves two steps, and the second step must be done before the first step times out:

Step 1: Invoke the flashing command on your machine.

`sudo python esptool.py --port /dev/tty.usbserial-AH0331HQ write_flash 0x00000 ~/Downloads/nodemcu-master-7-modules-2015-11-15-02-21-44-integer.bin`

Step 2: Reset the hardware so it accepts the firmware update.

While **holding down** the *GPIO0* button, **press and release** the *RESET* button.

Voila! Reflashed.

Now, connect to your Huzzah and play at the command line. I do this by using screen:

`screen /dev/tty.usbserial-AH0331HQ`

Happy Hacking.

---

*This post was migrated from WordPress. Original publication date: 2015-11-18 22:56:52*
