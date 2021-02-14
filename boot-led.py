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

from subprocess import Popen

p = Popen(["/usr/bin/python3", "/home/pi/src/bt-kitchenradio/power-led.py"])

