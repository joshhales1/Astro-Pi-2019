"""

A new effort to combine all the images at the correct distances apart to show the flightpath.
Currently working on finding the scale of the images.

0.00195 degrees per 1 pixel

512.71209 pixels per 1 degree


Find distance between 2 images.
Find that in degrees.
Multiply that distance by  512.71209 / degrees difference.

Distance in degrees * 512.

"""

from PIL import Image
import json
import os

from math import degrees, atan2
SCALE = 0.1

ppd = 512.71209


data_file = open("results.json")
data = json.loads(data_file.read()) # Load JSON file into program.
data_file.close()

boundries = {
"long max": float("-inf"),
"long min": float("inf"),
"lat max": float("-inf"),
"lat min": float("inf")
}

for i in range(1, len(data)): # Finds the upper and lower bounds of the long and lat to make the correct size canvas.
    item = data[str(i)]
    if item["long"] > boundries["long max"]: boundries["long max"] = item["long"]
    if item["long"] < boundries["long min"]: boundries["long min"] = item["long"]
    if item["lat"] >  boundries["lat max"]:  boundries["lat max"] =  item["lat"]
    if item["lat"] <  boundries["lat min"]:  boundries["lat min"] =  item["lat"]


x_length = (boundries["long max"] + abs(boundries["long min"])) * ppd * SCALE
y_length = (boundries["lat max"] + abs(boundries["lat min"])) * ppd * SCALE

x_length += (1920 * SCALE) // 2
y_length += (1080 * SCALE) // 2

background = Image.new("RGBA", (round(x_length), round(y_length)), (255, 255, 255))

"""
Correct scale causes memory errors.
The image would be 184680px 51300px
"""

# The pixel per degree constant.
old_long = 0
old_lat  = 0

start_image = 1
end_image = len(data)
step = 1
percentage = 0
for i in range(start_image, end_image, step):

    im = Image.open("images/zz_oba_" + str(i) + ".jpg")
    im = im.crop((400, 0, 1500, 1080))

    new_width = round(im.size[0] * SCALE)
    new_height = round(im.size[1] * SCALE)

    im = im.resize((new_width, new_height), Image.ANTIALIAS)

    x_offset = im.size[0] // 2
    y_offset = im.size[1] // 2

    raw_long = data[str(i)]["long"]
    raw_lat = data[str(i)]["lat"]

    long = round(raw_long * ppd * SCALE)
    lat = round(raw_lat * ppd * SCALE)

    long_distance = raw_long - old_long
    lat_distance  = raw_lat - old_lat

    angle = atan2(lat_distance, long_distance)
    angle = -degrees(angle)

    if angle < 0: angle = 360 + angle

    im = im.convert("RGBA")
    im = im.rotate(angle, Image.NEAREST, expand = 1)

    background.paste(im, (int(x_length // 2 + long) - x_offset, int(y_length // 2 + lat) - y_offset), im)
    old_long = raw_long
    old_lat  = raw_lat

    if percentage != int(i / end_image * 100):
        print(str(percentage) + "%")
        percentage = int(i / end_image * 100)



background.save("flightpath-wave-output.png")
