# AllJoyn 101: Getting Started with AllJoyn

**Published:** March 2015
**Categories:** Internet of Things
**Tags:** Internet of Things, Technology

---

**Copyright © 2015 Ivan Judson. All Rights Reserved.**

This blog post and all original images are protected by copyright. See [COPYRIGHT.md](../COPYRIGHT.md) for details.

---

I just returned from giving a talk at [the Linux Foundations](http://www.linuxfoundation.org/) [Embedded Linux Conference](http://events.linuxfoundation.org/events/embedded-linux-conference) in San Jose. It was an excellent event with very good information working in the embedded space, and it didn't just cover Linux, but also more general embedded tooling including tizin and AllJoyn. There was also a heavy emphasis on security in the embedded space, which is always a good thing to see as the number of devices continues to grow.

My presentation, [available on github](http://github.com/irjudson/AJIntro), was focused on introducing embedded developers to [AllJoyn](https://allseenalliance.org/) as a technology and take them through the process of writing an AllJoyn service for their embedded device. In order to deliver this content I chose to use the [Heatworks Model 1](http://www.myheatworks.com/) hot water heater as my example device. The Heatworks Model 1 is produced by a startup that participated in [Microsoft Ventures](https://www.microsoftventures.com/) fall 2014 cohort, where we became fast collaborators on IoT, Embedded, and Cloud.

Here you can see the generalized architecture that is required to build an IoT device and bring it to market. You can see the Model 1 on the left, with connectivity indicated both to the cloud and to local devices - here represented as mobile devices. Once data is pushed to the cloud it is available for storage, processing and analysis (the right side of the diagram).

The orange vertical connector on the Model 1 is where hardware will be added to add internet connectivity. The software I described in my talk should run on that board, making the Model 1 an AllJoyn device.

![The Heatworks Model1](https://irjudson.org/content/images/2015/03/Model1Ecosystem.png)

Here's the implementation of the service, available in [github](http://github.com/irjudson/heatworks-model1) with a client that invokes each method to prove the implementation works.

Here's how to build the interface using the AllJoyn Thin Library:

`/** * The interface name followed by the method signatures. * 
 * See also aj_introspect.h */
static
const char *
  const sampleInterface[] = {
    "com.myheatworks.model1",
    /* The first entry is the interface name. */ "?setPoint tempy",
    /* Get the water temperature setting */ "?softCurrentLimit currenty",
    /* Get the current draw at this instant */ "?timeOdometerValue time>i",
    /* Get the number of seconds the unit has been running. */ "?currentOdometerValue current>i",
    /* Get the integral of amps where dt = 4 seconds */ NULL
  }; /** * A NULL terminated collection of all interfaces. */
static
const AJ_InterfaceDescription sampleInterfaces[] = {
  sampleInterface,
  NULL
}; /** * Objects implemented by the application. The first member in the AJ_Object structure is the path. * The second is the collection of all interfaces at that path. */
static
const AJ_Object AppObjects[] = {
  {
    ServicePath,
    sampleInterfaces
  },
  {
    NULL
  }
};`

And here's the resulting interface definition:

`
    
        
            
        
        
            
        
        
            
        
        
            
        
        
            
        
        
            
        
    
P`

Here's the service implementation (I have eliminated some code to make this more compact and easier for viewing):

`#define BASIC_SERVICE_SETPOINT                                                 \
  AJ_APP_MESSAGE_ID(0, 0, 0)                                                   \
  #define BASIC_SERVICE_CURRENT_TEMP AJ_APP_MESSAGE_ID(                        \
      0, 0, 1) #define BASIC_SERVICE_SOFT_CURRENT_LIMIT                        \
      AJ_APP_MESSAGE_ID(0, 0, 2) #define BASIC_SERVICE_CURRENT_DRAW_INSTANT    \
          AJ_APP_MESSAGE_ID(0, 0, 3) #define BASIC_SERVICE_TIME_ODOMETER       \
              AJ_APP_MESSAGE_ID(0, 0,                                          \
                                4) #define BASIC_SERVICE_CURRENT_ODOMETER      \
                  AJ_APP_MESSAGE_ID(0, 0, 5) int main(int argc, char **argv) { \
     /* One time initialization before calling any other AllJoyn APIs. */   \
        AJ_Initialize();                                                       \
    AJ_RegisterObjects(AppObjects, NULL);                                      \
    while (TRUE) {                                                             \
      AJ_Message msg;                                                          \
      if (!connected) {                                                        \
        status =                                                               \
            AJ_StartService(&bus, NULL, CONNECT_TIMEOUT, FALSE, ServicePort,   \
                            ServiceName, AJ_NAME_REQ_DO_NOT_QUEUE, NULL);      \
         connected = TRUE;                                                  \
      }                                                                        \
      status = AJ_UnmarshalMsg(&bus, &msg, UNMARSHAL_TIMEOUT);                 \
       if (AJ_OK == status) {                                               \
        switch (msg.msgId) {                                                   \
         case BASIC_SERVICE_SETPOINT: {                                     \
          uint8_t setPoint = 40;                                               \
          AJ_Message reply;                                                    \
          AJ_UnmarshalArgs(&msg, "y", &setPoint); /* Check bounds */           \
          if (setPoint > SPMIN && setPoint  case BASIC_SERVICE_SOFT_CURRENT_LIMIT: {                           \
          uint8_t currentLimit = 10;                                           \
          AJ_Message reply;                                                    \
          AJ_UnmarshalArgs(&msg, "y", &currentLimit);                          \
          AJ_AlwaysPrintf(("Setting soft current limit to: %d amps.\n",        \
                           currentLimit)); /* Actually set the set point! */   \
          AJ_MarshalReplyMsg(&msg, &reply);                                    \
          AJ_InfoPrintf(                                                       \
              ("Setting soft current limit: returned %d, session_id=%u\n",     \
               status, sessionId));                                            \
          status = AJ_DeliverMsg(&reply);                                      \
        } break;                                                               \
           default : /* Pass to the built-in handlers. */ status =          \
                            AJ_BusHandleBusMessage(&msg);                      \
          break;                                                               \
        }                                                                      \
      } /* Messages MUST be discarded to free resources. */                    \
      AJ_CloseMsg(&msg);                                                       \
      if ((status == AJ_ERR_SESSION_LOST || status == AJ_ERR_READ)) {          \
        AJ_AlwaysPrintf(("AllJoyn disconnect.\n"));                            \
        AJ_Disconnect(&bus);                                                   \
        connected =                                                            \
            FALSE; /* Sleep a little while before trying to reconnect. */      \
        AJ_Sleep(SLEEP_TIME);                                                  \
      }                                                                        \
    }                                                                          \
    AJ_AlwaysPrintf(("Basic service exiting with status %d.\n", status));      \
    return status;                                                             \
  }`

This code enables the Heatworks Model 1 to implement an AllJoyn Service interface, enabling AllJoyn aware applications and devices to interact with the hotwater heater. The interface is also simple enough to allow for teaching others how to build AllJoyn services on stage at an event like the Embedded Linux Conference.

There are improvements to both the service and the process that could be made, most importantly:

- Bounds checking parameters

- Checking return types

- Ensuring return messages contain appropriate success/failure messages

These things should be done before this code is ever put into production. I'm sure the Heatworks folks are prepared for that, given the success of their product launch so far. Happy Hacking!

---

*This post was migrated from WordPress. Original publication date: 2015-03-25 17:07:42*
