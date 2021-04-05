from gpiozero import PWMLED, Button
from signal import pause
from time import sleep
from time import monotonic
from random import randrange

def shutdown(btn, text="test"):
    print("Shutting down!")
    print("Waiting for secodn button")
    button.wait_for_press(10)
    print("I was active for")
    if button.active_time:
        print (button.active_time)
    else:
        print ("Nope")

def switch_on():
    print("Button pressed! Active time: ", button.active_time)

button = Button(5)
off_btn = Button(13, hold_time=3)

button.when_pressed = switch_on
off_btn.when_held = shutdown

pause()

