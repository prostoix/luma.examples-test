import time
from pathlib import Path
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont

#Define the I2C serial interface and the SSD1306 device
serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)

#Define a custom font
font_path = "tmp/luma.examples-test/examples/fonts/SAC.ttf" 
custom_font = ImageFont.truetype(font_path, 12)

#Display text using the custom font
device.clear() 
device.text((0, 0), "Hello, World!", fill="white", font=custom_font) 
device.show()

time.sleep(5) # Display text for 5 seconds

#Clear the display
device.clear() 
device.show()