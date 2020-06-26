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


x_length = ( boundries["long max"] + abs(boundries["long min"]) ) * ppd * SCALE
y_length = ( boundries["lat max"] + abs(boundries["lat min"]) ) * ppd * SCALE
background = Image.new("RGB", (round(x_length), round(y_length)), (255, 255, 255))

"""
Correct scale causes memory errors.
The image would be 184680px 51300px
"""

# The pixel per degree constant.

for i in range(450, 500, 1):

    im = Image.open("images/zz_oba_" + str(i) + ".jpg")
    im = im.crop((400, 0, 1500, 1080))

    new_width = round( im.size[0] * SCALE )
    new_height = round( im.size[1] * SCALE )

    im = im.resize((new_width, new_height), Image.ANTIALIAS)

    long = round(data[str(i)]["long"] * ppd * SCALE)
    lat = round(data[str(i)]["lat"] * ppd * SCALE)

    #print(long, lat, x_length//2, y_length//2)
    background.paste(im, (int(x_length // 2 + long), int(y_length // 2 + lat)))


background.save("flightpath-wave-output.png")
