#!/usr/bin/python3

# boot_led.py - Light up a GPIO LED on bootup using random flickering
# Copyright(C) 2021 - Markus Holtmanns

# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY
# without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see < https: // www.gnu.org/licenses/>.

# The idea is that the random brightness increase emulates somewhat the
# behaviour of old tubes "warming up". Since it is only seen once
# I don't put too much thought/effort into it.
# Note: Process import needs to be capitalized, 'process' is built-in

from gpiozero import PWMLED, Button
from subprocess import check_call
from time import monotonic
from random import randrange
from signal import pause

# Define GPIO to use for the LED, default to 17

LED_GPIO = 17
OFF_BTN_GPIO = 2
BT_BUTTON_GPIO = 3

# randomized switch on sequence
def switch_on(led):
    # Set to a value that actually triggers the LED on
    led.value = 0.4
    # Set to minimal value; it will effectively be higher due to
    # LED trigger curve
    led.value = 0.01

    t = monotonic()
    e = monotonic()
    # Light it up slowly over time emulating some form of hyteresis
    while e - t < 16:
        diff = randrange(int(e - t), 21)
        led.value = 0.015 * diff
        e = monotonic()
    # after the time is up just slowly increase brightness to full
    for i in range(100001):
        led.value = 0.1 + (0.6 * i/100000)
    # Keep this process running to not switch off the LED
    # Might be dirty, but until gpiozero does not support NOT
    # cleaning up specific GPIOs, this is the easiest solution

def shutdown():
    # check_call(['sudo', 'poweroff'])
    print("Do you really want to shut down? Press the BT button to confirm!")
    # TODO: Ouput warning message and prompt for confirmation
    #       button press of the BT button
    bt_disconnect_btn.wait_for_press(10)
    if bt_disconnect_btn.active_time == None:
        print("Shutdown cancelled!")
        # TODO: Sound output
    else:
        # check_call(['sudo', 'poweroff'])
        print("Shutting down system NOW!")


def bt_disconnect()
    # TODO: Implement BT disconnect by checking active devices
    # and disconencting them
    print("Disconnecting all connected BT devices, please wait...")
    print("Done! Ready for pairing.")


# Initialize LED
onled = PWMLED(LED_GPIO)
switch_on(onled)

shutdown_btn = Button(OFF_BTN_GPIO, hold_time=3)
bt_disconnect_btn = BUTTON(BT_BUTTON_GPIO, hold_time=3)

shutdown_btn.when_held = shutdown
bt_disconnect_btn.when_held = bt_disconnect

pause()

