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


   
photocell = analogio.AnalogIn(board.GP28)



vcc = digitalio.DigitalInOut(board.GP14)
vcc.direction = digitalio.Direction.OUTPUT
vcc.value = True
time.sleep(1)
i2c = busio.I2C (scl=board.GP13, sda=board.GP12) # This RPi Pico way to call I2C
display_bus = displayio.I2CDisplay (i2c, device_address = 0x3C) # The address of my Board
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64) 


# Set text, font, and color
text = "Hello World!"
font = terminalio.FONT
color = 0xFFFFFF

# Create the text label
text_area = label.Label(font, text=text, color=color)

# Set the location
text_area.x = 0
text_area.y = 10

# Show it
display.root_group = text_area

# Loop forever so you can enjoy your image
while True:
    try:
        text_area.text = str(photocell.value)
    except RuntimeError:
        print("Retrying!")
    
    if photocell.value > 500:
        pixels.brightness = 0.4
    else:
        pixels.brightness = 0.1
    pixelOn = False
    if touch_sensor.value:
        pixelOn = True 
        set_color(random_color) # Set all NeoPixels to the random color
    
    if not pixelOn:
        set_color((0, 0, 0))
        random_color = random.choice(colors) # Change color for next time

    time.sleep(1)  # Small delay to avoid flooding with events
