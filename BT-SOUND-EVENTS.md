# bluetooth-sound-events

This is a fork of the very helpful original https://github.com/Pivek/bluetooth-sound-events.

Trying to run the April 2020 version of this tool on current kernel `5.4.79-v7+` caused several issues. I could address them successfully and happily share the results.

### Updated Dependencies:
- The original README mentioned a couple of deependencies that needed to be fulfilled. Beside `mpg123` most are already part of default Python 2.7 on Buster. The easiest way to get the still missing `dbus` and `signal` is to install `pip`
- The original Bluetooth instructions are from 2014, so `gobject` is a bit outdated and should be replaced by [`PyGObject`][3]

   But `PyGObject` depends on `cairo` so you need to install that first.

The following should be all that is needed in addition to the original README instructions in terms of dependencies:
```bash
sudo apt install python-pip libcairo2-dev
pip install PyGObject
```
### Code changes
The code changes are minimal. Beside replacing the deprecated `gobject` by `GLib` I only moved from `os.system()` to `subprocess.call()` to be able to make sure to get the correct execution environment for the python call to `mpg123` on a BT event.

### TODOs
- Add code to optionally enable/disable a LED on a BT event (using `GPIO`)
- Move to Python 3

## Original README from Pivek's project:

Add new functionalities:
- Sound on boot (when A2DP sink into Pulseaudio is ready)
- Sound on connect or disconnect events (when new A2DP interface is added or removed)

Code as expansion for this [tutorial][1].
Originally from [here][2] by Douglas6 written for Raspberry Pi.

Usage:
- Make clone using `git clone https://github.com/Pivek/bluetooth-sound-events` in your Raspberry Pi home dir for pi user
- Go to cloned directory and run `./install.sh`. It will create global `bluetooth-sound-events-onchange` and local `bluetooth-sound-events-onboot` services

Dependencies and assumptions:
- System `Raspbian GNU/Linux 10 (buster)`
- Bluetooth/A2DP and Pulseaudio are configured according to mentioned tutorial
- Python 2.7 is installed with following modules: `os`, `sys`, `signal`, `logging`, `logging.handlers`, `dbus`, `dbus.service`, `dbus.mainloop.glib`, `gobject`
- You have installed `mpg123` terminal player
- Your bluetooth device is operating as `hci0` in bus object_path `/org/bluez/hci0/`

[1]:https://www.raspberrypi.org/forums/viewtopic.php?t=235519
[2]:https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=85101
[3]:https://pygobject.readthedocs.io/en/latest/getting_started.html
