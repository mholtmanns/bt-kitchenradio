# Generic development notes and references
This is the attemtp to somewhat documnt the development steps to the final (or is it ever?) version of the "Bluetooth on Raspberry Pi" powered Kitchen Radio.

As a background: My wife and I discovered an old tube radio from the 1950s on a garbage dump and decided to turn it into a nice looking BT speaker. I found some old speaker parts that I could put into the cleaned out interior as well as an unused Raspberry Pi 2 with extra Wifi and BT through USB.

What's done so far:
- Created a POC with all the parts in the casing
- Have an additional warm-yellow light bulb installed to give it retro-lighting
- Have BT support up and running to make it usable

What's next (not necessarily in this order):
- Screw all parts down in the right places
- Add proper casing for the Raspi
- Add two buttons to
    - Switch the Raspi off, that is, call `sudo poweroff`
    - Disconnect all currently connected BT devices to allow pairing

## BT Sound events
I am using the setup of the Github user [Pivek][1] to enable sound events for the BT speaker functionality of the Raspi Radio. I needed to address some smaller issues in a personal fork, which I will incorporaste into this repository at some point to streamline installation.

The BT support as such comes from a forum post on [raspberrypi.org][2]. 
## Spotify support
This build also incorporates Spotify support, but that is not as reliable as connecting via BT, since the device discovery is rather sketchy. Sometimes it works, most of the time it does not.

Basic support is installed by using [raspotify][3].

## Power LED
I wanted to add a fake Lighted tube to the radio to show that it is powered on without lighting up the full interior lighting. And it was supposed to "flicker" to life slowly. For that purpose I needed a service to run on startup and trigger the GPIO controlled LED. I ended up creating two Python scripts, `boot-led` and `power-led`, where the former is just a dummy that spawns a subprocess with `power-led` and can be called as a `forking` process from the respective service. `power-led` will stay in `pause()` state throughout the devices uptime.

### Useful links
- The BT startup/connect/disconnect logic is forked from the [original BT Sound events github](https://github.com/Pivek/bluetooth-sound-events).
- Much of the LED and Button functionality implemented here is using [gpiozero](https://gpiozero.readthedocs.io/en/stable/index.html).


---
EOF

[//]: # (All reference links should go below this line)

[1]: https://github.com/Pivek "Github user Pivek"
[2]: https://www.raspberrypi.org/forums/viewtopic.php?f=35&t=235519 "Yet another Raspi BT tutorial"
[3]: https://github.com/dtcooper/raspotify "Using a Rasspberry Pi as a Spotify sink"