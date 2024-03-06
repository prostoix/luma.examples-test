import time
from pathlib import Path
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont

#Define the I2C serial interface and the SSD1306 device
serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)

font_path = "/usr/share/fonts/SAC.ttf"
font = ImageFont.truetype(font_path, 20)

name = "Piano"
number = "001"
collection = "1"

with canvas(device) as draw:
    draw.text((10, 0), name, font=font, fill="white")
    draw.text((10, 5), number, font=font, fill="white")
    draw.text((60, 10), collection, font=font, fill="white")
time.sleep(5) 