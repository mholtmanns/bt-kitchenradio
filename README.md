# bt-kitchenradio
Extending general Raspberry Pi as Bluetooth Radio functionality with LEDs and buttons for a modded old tube radio.

## Current status
- All HW provisionally installed and running
- Raspberry Pi 3 B with built-in BT and USB WiFi installed
- Blue LED installed to show that a device is connected
- Raspbian Image set up to support raspotify and BT including sound events
- Prepared the boot-led.service to enable a "flickering" orange LED on startup on the development Raspberry
- Moved the repo contents of the forked bt-sound-events repo here ([Details](./BT-SOUND-EVENTS.md))

## More details
For a complete description of motivation, idea and further steps on this project, refer to my detailed [Notes](./NOTES.md)

## Acknowledgements
- Raspberry Pi Bluetooth speaker tutorials: https://www.raspberrypi.org/forums/viewtopic.php?t=235519 and https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=85101
- The original BT sound events repo on github (no specific LICENSE): https://github.com/Pivek/bluetooth-sound-events
- raspotify code (MIT License): https://github.com/dtcooper/raspotify

