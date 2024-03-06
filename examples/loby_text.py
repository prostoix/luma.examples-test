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
font = ImageFont.truetype(font_path, 12)

text = "Hello, World!"

with canvas(device) as draw:
    draw.text((0, 0), text, font=font, fill="white")