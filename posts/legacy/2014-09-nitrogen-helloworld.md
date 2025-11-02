# Nitrogen HelloWorld

**Published:** September 2014
**Categories:** Uncategorized
**Tags:** Technology

---

**Copyright © 2014 Ivan Judson. All Rights Reserved.**

This blog post and all original images are protected by copyright. See [COPYRIGHT.md](../COPYRIGHT.md) for details.

---

In my [last blog post](http://irjudson.org/getting-started-with-nitrogen/) about [Nitrogen](http://nitrogen.io), I showed how to get started developing with nitrogen with very little effort. To enable that blog post, I wrote a vagrant configuration that allows you to bring up a virtual machine running the Nitrogen [Service](http://github.com/nitrogenjs/service) and [Admin](http://http://github.com/nitrogenjs/admin) web application.

In this post, I'll show how to use that vm to build and test the simplest Nitrogen device possible. All the code is in a [github repo](https://github.com/irjudson/helloworld).

### Background

Recall, to setup the virtual machine you need to:

- Have a virtualization application ([virtualbox](http://virtualbox.org) or [parallels](http://parallels.com))

- Install [vagrant](http://vagrantup.com)

Then, run these commands:

`# Clone the rep`

```
`> git clone https://github.com/irjudson/vagrant-vms.git
# Get into the code
> cd vagrant-vms/nitrogen
# Add the ubuntu/trusty64 box
> vagrant add ubuntu/trusty64
# create the vm
> vagrant up`
```

Once you've done that, you can get started writing your first device that sends data to Nitrogen. To get started, be sure you have the latest [Node](http://nodejs.org) installed.

### Hello World, Nitrogen Style

Then make a directory named helloworld:

`mkdir helloworldcd helloworld`

Open an empty file named [helloworld.js](https://raw.githubusercontent.com/irjudson/helloworld/master/helloworld.js) and type or paste this code into it:

var Store = require("nitrogen-leveldb-store"),
  nitrogen = require("nitrogen");
var config = {
  host: process.env.HOST_NAME || "localhost",
  http_port: process.env.PORT || 3030,
  protocol: process.env.PROTOCOL || "http",
  api_key: process.env.API_KEY,
};
config.store = new Store(config);
var service = new nitrogen.Service(config);
var helloWorld = new nitrogen.Device({
  nickname: "helloWorld",
  tags: ["sends:ping"],
  api_key: config.api_key,
});
service.connect(helloWorld, function (err, session, helloWorld) {
  if (err) return console.log("failed to connect helloWorld: " + err);
  var self = this;
  setInterval(function () {
    var message = new nitrogen.Message({
      type: "_ping",
      body: { command: { message: "I'm alive. My ID is: " + helloWorld.id } },
    });
    message.send(session);
  }, 2000);
});

Then, open an empty file named [package.json](https://raw.githubusercontent.com/irjudson/helloworld/master/package.json), and type or paste these lines:

`{
  "name": "helloworld",
  "repository": { "type": "git", "url": "" },
  "version": "0.1.0",
  "private": "true",
  "dependencies": {
    "nitrogen": "~0.2.0",
    "nitrogen-leveldb-store": "~0.1.201"
  },
  "devDependencies": { "mocha": "1.x" }
}`

Then run this command to install the dependencies your device has (specifically, nitrogen and the nitrogen-leveldb-store).

`npm install`

### Getting your API Key

Finally, we have to do some configuration and interaction with the Nitrogen Service, so:

- Open a browser to [http://localhost:9000/](http://localhost:9000/)

- Create a new account
![Create Account Screen](https://raw.githubusercontent.com/irjudson/helloworld/master/doc/CreateAccount.png)

- Login with that account
![Home Screen After Login](https://raw.githubusercontent.com/irjudson/helloworld/master/doc/HomeScreen.png)

- Go find your API Key
![API Keys](https://raw.githubusercontent.com/irjudson/helloworld/master/doc/APIKeys.png)

### Running HelloWorld!

Copy the API Key and run this command in your shell (from the directory where you built the helloworld example):

`API_KEY="" node helloworld.js`

Here's what it looks like:
![Run HelloWorld](https://raw.githubusercontent.com/irjudson/helloworld/master/doc/ShellCommand.png)

Now, if you go to your [messages screen](http://localhost:9000/#/messages/skip/0/sort/ts/direction/-1) you should see this:

![Messages Flowing](https://raw.githubusercontent.com/irjudson/helloworld/master/doc/Messages.png)

### Conclusion

From this *very* brief example you can see how simple it is to get a device sending telemetry data. In the next post, I'll show how to recieve commands and act on them.

---

*This post was migrated from WordPress. Original publication date: 2014-09-30 12:56:59*
