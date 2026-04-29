from PIL import Image, ImageDraw, ImageFont
from data_analysis import *
import sys

##
activities = load_activities_file()
running_stats = get_running_stats(activities=activities, numDays=7)


# Create an image
eink_resolution = (800, 400)  # in pixels (this is for 7.3 in inky impression)
background_colour = (223, 248, 235)
bar_colours = (232, 135, 30)
text_colour = (78, 2, 80)

base_image = Image.new("RGBA", eink_resolution, color=background_colour)
draw = ImageDraw.Draw(base_image)

# Create an image for the distance text:
disp_txt = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
# get a font
fnt = ImageFont.truetype("fonts\\FjallaOne-Regular.ttf", size=60)
# get a drawing context
d = ImageDraw.Draw(disp_txt)

## Strings for displaying
dist_string = f"Total Distance = {running_stats[0] / 1000:.1f} km"
climb_string = f"Total Climb = {running_stats[1]} m"

# draw text, half opacity
d.text((10, 10), dist_string, font=fnt, fill=text_colour)
# draw text, full opacity
d.text((10, 70), climb_string, font=fnt, fill=text_colour)

out = Image.alpha_composite(base_image, disp_txt)

out.show()

# base_image.show()
