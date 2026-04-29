from PIL import Image, ImageDraw, ImageFont
from data_analysis import *
import sys

##
activities = load_activities_file()
running_stats = get_running_stats(activities=activities, numDays=7)


## Layout
metrics_x = 20
metrics_y = 100

header_x = 20
header_y = 20

# Create an image
eink_resolution = (800, 400)  # in pixels (this is for 7.3 in inky impression)
background_colour = (223, 248, 235)
bar_colours = (232, 135, 30)
text_colour = (78, 2, 80)

base_image = Image.new("RGBA", eink_resolution, color=background_colour)
draw = ImageDraw.Draw(base_image)

# Define fonts
label_font = ImageFont.truetype("fonts/FjallaOne-Regular.ttf", 24)
value_font = ImageFont.truetype("fonts/FjallaOne-Regular.ttf", 60)
header_font = ImageFont.truetype("fonts/FjallaOne-Regular.ttf", 45)

## Strings for displaying
dist_string = f"Total Distance = {running_stats[0] / 1000:.1f} km"
climb_string = f"Total Climb = {running_stats[1]:.0f} m"
header_string = f"Strava Weekly Mileage"

draw.text((metrics_x, metrics_y), "Distance", font=label_font, fill=text_colour)
draw.text(
    (metrics_x, metrics_y + 30),
    f"{running_stats[0] / 1000:.1f} km",
    font=value_font,
    fill=text_colour,
)


draw.text((header_x, header_y), header_string, font=header_font, fill=text_colour)
draw.text((metrics_x, metrics_y + 150), "Climb", font=label_font, fill=text_colour)
draw.text(
    (metrics_x, metrics_y + 170),
    f"{running_stats[1]:.0f} m",
    font=value_font,
    fill=text_colour,
)

draw.rectangle((10, 20, 780, 80), outline=0)  # header
draw.rectangle((10, 100, 320, 360), outline=0)  # metrics
draw.rectangle((340, 100, 780, 360), outline=0)  # plot


base_image.show()
