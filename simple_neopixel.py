import time
import board
import touchio
import neopixel
import random

num_pixels = 12  # Number of NeoPixels

# NeoPixel setup starting 
pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 0.1

# Touch pin setup
touch_sensor = touchio.TouchIn(board.GP2)

# Define colors
colors = [
    (0, 0, 255),    # Blue
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255), # Magenta
    (255, 0, 127) ,  #Pink
    (255, 127, 0)  , # Orange
]

# Function to set all NeoPixels to a specific color
def set_color(color):
    for i in range(num_pixels):
        pixels[i] = color
    pixels.show()


pixelOn = False
random_color = random.choice(colors) # Random color to start with


# Main loop
while True:
    pixelOn = False
    if touch_sensor.value:
        pixelOn = True 
        set_color(random_color) # Set all NeoPixels to the random color
    
    if not pixelOn:
        set_color((0, 0, 0))
        random_color = random.choice(colors) # Change color for next time

    time.sleep(0.01)  # Small delay to avoid flooding with events
