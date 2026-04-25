from PIL import Image, ImageDraw
import sys

# Create an image
eink_resolution = (800, 480)  # in pixels (this is for 7.3 in inky impression)

with Image.open("display_image.png") as im:
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)

    # write to stdout
    im.save(sys.stdout, "PNG")
