import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

def do_nothing(obj):pass

serial = i2c(port=0, address=0x3C)
device = ssd1306(serial)
device.cleanup = do_nothing

def primitives(device, draw):
    # Draw some shapes
    # First define some constants to allow easy resizing of shapes
    padding = 2
    shape_width = 20
    top = padding
    bottom = device.height - padding - 1

    # Move left to right keeping track of the current x position for drawing shapes
    x = padding

    # Draw an ellipse
    draw.ellipse((x, top, x + shape_width, bottom), outline="red", fill="black")
    x += shape_width + padding

    # Draw a rectangle
    draw.rectangle((x, top, x + shape_width, bottom), outline="blue", fill="black")
    x += shape_width + padding

    # Draw a triangle
    draw.polygon([(x, bottom), (x + shape_width / 2, top), (x + shape_width, bottom)], outline="green", fill="black")
    x += shape_width + padding

    # Draw an X
    draw.line((x, bottom, x + shape_width, top), fill="yellow")
    draw.line((x, top, x + shape_width, bottom), fill="yellow")
    x += shape_width + padding

    # Write two lines of text
    left, t, right, bottom = draw.textbbox((0, 0), 'World!!!')
    w, h = right - left, bottom - t
    x = device.width - padding - w
    draw.rectangle((x, top + 4, x + w, top + h), fill="black")
    draw.rectangle((x, top + 16, x + w, top + 16 + h), fill="black")
    draw.text((device.width - padding - w, top + 4), 'Hello', fill="cyan")
    draw.text((device.width - padding - w, top + 16), 'World!', fill="purple")

    # Draw a rectangle of the same size of screen
    draw.rectangle(device.bounding_box, outline="white")

def main():
    print("Testing basic canvas graphics...")
    for _ in range(2):
        with canvas(device) as draw:
            primitives(device, draw)
time.sleep(5)

