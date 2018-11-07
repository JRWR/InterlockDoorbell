from gpiozero import Button
from signal import pause
from gpiozero import Buzzer
import time 
import requests

doorbellhook = "REPLACEMEN"
doorbellhookheld = "REPLACEMENT"
bz = Buzzer(17)

button = Button(4, pull_up=False)
held = 0

def say_hello():
    global held
    if held == 0:
        bz.on()
        time.sleep(0.5)
        bz.off()
	held = 0
	r = requests.post(doorbellhook)
	print(r.text)
    else:
	held = 0
def say_hello2():
    global held
    held = 1
    bz.on()
    time.sleep(1)
    bz.off()
    r = requests.post(doorbellhookheld)
    print(r.text)
    time.sleep(0.5)
    bz.on()
    time.sleep(1)
    bz.off()



button.when_released = say_hello
button.when_held = say_hello2

pause()
