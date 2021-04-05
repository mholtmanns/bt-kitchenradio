# bt-kitchenradio
Extending general Raspberry Pi as Bluetooth Radio functionality with LEDs and buttons for a modded old tube radio.

## Current status
As of 05.04.2021
- All HW provisionally installed and running
- Raspberry Pi 3 B with built-in BT and USB WiFi installed
- Blue LED installed to show that a device is connected
- Red/Orange Power LED in old tube housing installed and "flickering" on during boot-up using boot-led.service
- Buttons for BT disconnect and Power down isntalled
- Raspbian Image set up to support raspotify and BT including sound events

## More details
For a complete description of motivation, idea and further steps on this project, refer to my detailed [Notes](./NOTES.md)

## Acknowledgements
- Raspberry Pi Bluetooth speaker tutorials: https://www.raspberrypi.org/forums/viewtopic.php?t=235519 and https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=85101
- The original BT sound events ([Details](./BT-SOUND-EVENTS.md)) repo on github (no specific LICENSE): https://github.com/Pivek/bluetooth-sound-events
- raspotify code (MIT License): https://github.com/dtcooper/raspotify

