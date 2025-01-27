
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)

button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN


led.direction = digitalio.Direction.OUTPUT
led.value = True
print("Hello, CircuitPython!")

while True:
    if button.value:
        led.value = not led.value
        print("Button pressed!")
        time.sleep(1)
