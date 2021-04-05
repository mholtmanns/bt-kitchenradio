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

# TODO: Clean-up, function doc comments, cleaner logging, etc.

# The idea is that the random brightness increase emulates somewhat the
# behaviour of old tubes "warming up". Since it is only seen once
# I don't put too much thought/effort into it.

from gpiozero import PWMLED, Button
from subprocess import check_call, Popen
from time import monotonic, sleep
from random import randrange
from signal import pause
from threading import Thread, Event
from bt_check_connection import bt_disconnect

# I dislike magic numbers, but for simplicity's sake we use them here
LED_GPIO = 27           # Pins 13/14 - Power LED
OFF_BTN_GPIO = 13       # Pins 33/34 - Power Off Button
BT_BUTTON_GPIO = 5      # Pins 29/30 - Bluetooth disconnect button

# Initialize Power LED
onled = PWMLED(LED_GPIO)

def switch_on(led):
    """Randomize the LED brightness during boot-up
    """
    # Set to a value that actually triggers the LED on
    led.value = 0.4
    # Set to minimal value; it will effectively be higher due to
    # LED trigger curve
    led.value = 0.01

    t = monotonic()
    e = monotonic()
    # Light it up slowly over time emulating some flickering
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

def powerdown(e):
    """ Loop power LED on and off until we decide to shut down or not
    """
    while not e.isSet():
        onled.off()
        sleep(0.5)
        onled.on()
        sleep(0.5)
    

def shutdown():
    # print("Do you really want to shut down? Press the BT button to confirm!")
    # TODO: Ouput warning message and prompt for confirmation
    #       button press of the BT button
    e = Event()
    off_thread = Thread(target=powerdown, args=(e,), daemon=True)
    off_thread.start()
    bt_disconnect_btn.wait_for_press(10)
    if bt_disconnect_btn.active_time == None:
        # print("Shutdown cancelled!")
        # Signal the blinking thread to stop
        e.set()
        # make sure the Power LED is on
        onled.on()
        # TODO: Sound output
        return
    else:
        # print("Shutting down system NOW!")
        try:
            # print("sudo poweroff")
            # Signal the blinking thread to stop
            e.set()
            # make sure the Power LED is on before shutdown so once it
            # is off we know the system is off as well
            onled.on()
            r = check_call(['sudo', 'poweroff'])
        except subprocess.CalledProcessError:
            # TODO: Error handling
            pass

if __name__ == "__main__":
    # switch_on(onled)
    onled.on()

    shutdown_btn = Button(OFF_BTN_GPIO, hold_time=3)
    bt_disconnect_btn = Button(BT_BUTTON_GPIO, hold_time=3)

    shutdown_btn.when_held = shutdown
    bt_disconnect_btn.when_held = bt_disconnect

    pause()