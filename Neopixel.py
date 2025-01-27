# Code to play a rainbow animation on the neopixel hat. You will need to include the neopixel file in the lib folder on the pico.

import time
import board
import neopixel

# Initialize the NeoPixel strip
num_pixels = 12
pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 0.1

# Function to create rainbow colors across 0-255 positions
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colors are a transition r -> g -> b -> back to r.
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

# Main loop to cycle rainbow colors quickly
speed = 50  # Increase this value to make the animation faster

while True:
    for i in range(num_pixels):
        # Increase speed factor for faster animation
        pixel_index = (i * 256 // num_pixels) + time.monotonic() * speed
        pixels[i] = wheel(int(pixel_index) & 255)
    pixels.show()
    time.sleep(0.01)  # Reduce sleep time to make the animation smoother and faster
