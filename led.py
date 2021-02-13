from gpiozero import PWMLED, Button
from signal import pause
from time import sleep
from time import monotonic
from random import randrange

def switch_on():
    if led.is_lit:
        led.value = 0.0
        return

    led.value = 0.4
    led.value = 0.01

    t = monotonic()
    e = monotonic()
    while e - t < 16:
        diff = randrange(int(e - t), 21)
        led.value = 0.015 * diff
        e = monotonic()
    for i in range(100001):
        led.value = 0.1 + (0.6 * i/100000)

def switch_off():
    for i in range(10):
        led.value = 0.1 - (0.01 * i)
        sleep(0.1)

led = PWMLED(17)
button = Button(2, bounce_time = 1)

print (monotonic())

button.when_pressed = switch_on
# button.when_released = switch_off


pause()

