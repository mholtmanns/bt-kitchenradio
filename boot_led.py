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

from gpiozero import PWMLED, Button
from time import monotonic
from random import randrange

# Define GPIO to use for the LED, default to 17

LED_GPIO = 17

# randomized switch on sequence
def switch_on():

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

led = PWMLED(LED_GPIO)
switch_on()
