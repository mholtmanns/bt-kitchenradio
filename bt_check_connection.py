#!/usr/bin/python

import os
import sys
# Using "native" GPIO to "misuse" the fact that it needs explicit
# cleanup so if we switch the GPIO off, it will stay off.
import RPi.GPIO as GPIO
import subprocess

# I dislike magic numbers, but for simplicity's sake we use one here
BTLED_GPIO = 17     # Pins 11/9 - Bluetooth Connection LED

def bt_connected():
    """Return the list of all paired and connected BT devices

    bt-device -l returns the list of all paired BT devices:
      Added devices:
      Markus Handy (90:A2:5B:79:9B:60)
    Using the MAC address we can iterate over all devices and check
    if any have a connection state of 1

    Returns
    -------
    list
        a list of MAC addresses of connected BT devices
    """

    cmd = ("bt-device -l")
    try:
        out = subprocess.check_output([cmd], shell=True, text=True)
    except subprocess.CalledProcessError:
        out = "None"

    devices = list()
    if out != "None":
        lines = out.splitlines()
        for d in lines:
            # Skip the first line
            if "Added" in d:
                continue
            # The MAC address is always at the end
            mac = (d.split(' '))[-1]
            # remove enclosing parentheses
            mac = mac[1:-1]
            # check the device details for this MAC
            # if there is an exception, just skip this device
            cmd = ("bt-device -i {}".format(mac))
            try:
                out2 = subprocess.check_output([cmd], shell=True, text=True)
            except subprocess.CalledProcessError:
                continue
            details = out2.splitlines()
            for d2 in details:
                # The line we are interested in looks like this:
                # 'Connected: 0' or '1' at the end
                if "Connected" in d2:
                    if d2[-1] == "1":
                        devices.append(mac)
    return devices

def bt_disconnect():
    """Disconnect any connected BT devices
    
    This is to allow for new BT devices to connect with the Radio
    """
    dl = bt_connected()
    if dl:
        for mac in dl:
            cmd = ("bt-device -d {}".format(mac))
            try:
                subprocess.check_output([cmd], shell=True, text=True)
            except subprocess.CalledProcessError:
                # TODO: Error handling
                pass


if __name__ == "__main__":
    # Sometimes the GPIO is initialized at boot-up, but we
    # want to make sure we switch it off if nothing is connected
    connections = bt_connected()
    if not connections:
        # Init GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BTLED_GPIO, GPIO.OUT)
        # Only switch it off if it was on at all
        if GPIO.input(BTLED_GPIO):
            GPIO.output(BTLED_GPIO, GPIO.LOW)
