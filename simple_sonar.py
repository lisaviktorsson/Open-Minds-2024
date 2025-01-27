import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)

import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP12, echo_pin=board.GP13)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)