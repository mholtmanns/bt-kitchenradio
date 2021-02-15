from gpiozero import PWMLED, Button
from signal import pause
from time import sleep
from time import monotonic
from random import randrange

def shutdown():
    print("Shutting down!")
    print("Waiting for secodn button")
    button.wait_for_press(10)
    print("Was I active?", button.active_time)

def switch_on():
    print("Button pressed! Active time: ", button.active_time)

button = Button(3)
off_btn = Button(2, hold_time=3)

button.when_pressed = switch_on
off_btn.when_held = shutdown

pause()

