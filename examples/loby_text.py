import time
from pathlib import Path
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import ImageFont

def do_nothing(obj):pass

serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)
device.cleanup = do_nothing

def make_font(name, size):
    font_path = str(Path(__file__).resolve().parent.joinpath('fonts', name))
    return ImageFont.truetype(font_path, size)

def primitives(device, draw):
    # Draw some shapes
    # First define some constants to allow easy resizing of shapes
    padding = 2
    shape_width = 20
    top = padding
    bottom = device.height - padding - 1
    fonts = [make_font("SAC.ttf", sz) for sz in range(24, 8, -2)]
    # Move left to right keeping track of the current x position for drawing shapes
    #x = padding

    # Write two lines of text
    #left, t, right, bottom = draw.textbbox((0, 0), 'World!!!')
    #w, h = right - left, bottom - t
    #x = device.width - padding - w
    #draw.rectangle((x, top + 4, x + w, top + h), fill="black")
    #draw.rectangle((x, top + 16, x + w, top + 16 + h), fill="black")
    draw.text((30, 40), 'Hello', font=fonts, fill="cyan")
    #draw.text((device.width - padding - w, top + 4), 'Hello', fill="cyan")
    #draw.text((device.width - padding - w, top + 16), 'World!', fill="purple")

    # Draw a rectangle of the same size of screen
    draw.rectangle(device.bounding_box, outline="white")

def main():
    print("Testing basic canvas graphics...")
    for _ in range(2):
        with canvas(device) as draw:primitives(device, draw)
    time.sleep(5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass