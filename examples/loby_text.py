from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

serial = i2c(device=0, address=0x3C)
device = ssd1306(serial)

font_path = "SAC.ttf"
font = ImageFont.truetype(font_path, 12)

text = "Hello, World!"

with canvas(device) as draw:
    draw.text((0, 0), text, font=font, fill="white")