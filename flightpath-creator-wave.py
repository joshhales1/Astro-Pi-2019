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
SCALE = 0.1 # Can scale up and down the resolution of the ouptut. It needs to be slow so as to not fill memory

ppd = 512.71209 # Constant pixels per degree. See distance-reference folder for information

data_file = open("results.json")
data = json.loads(data_file.read()) # Load JSON file into program.
data_file.close()

boundries = { # Object for holding boundry data for the canvas
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

x_length += (1920 * SCALE) // 2 # Stops lower and upper images from rendering half off screen
y_length += (1080 * SCALE) // 2


"""
Creates background image
Correct scale causes memory errors.
The image would be 184680px 51300px
"""
background = Image.new("RGBA", (round(x_length), round(y_length)), (255, 255, 255)) #


old_long = 0 # For calculating theta between two frames
old_lat  = 0

start_image = 1 # The first image to render
end_image = len(data) # The last image to render
step = 1 # The step of each iteration
percentage = 0 # For viewing progess in terminal
for i in range(start_image, end_image, step):

    im = Image.open("images/zz_oba_" + str(i) + ".jpg") # Open current image
    im = im.crop((400, 0, 1500, 1080)) # Crop the window out of the image

    new_width = round(im.size[0] * SCALE)
    new_height = round(im.size[1] * SCALE)

    im = im.resize((new_width, new_height), Image.ANTIALIAS) # Scales image down

    x_offset = im.size[0] // 2 # Calculating offset for later use to paste image by their center points
    y_offset = im.size[1] // 2

    raw_long = data[str(i)]["long"]
    raw_lat = data[str(i)]["lat"]

    long = round(raw_long * ppd * SCALE) # Get image friendly long and lats
    lat = round(raw_lat * ppd * SCALE)

    long_distance = raw_long - old_long # Find difference between current and last image
    lat_distance  = raw_lat - old_lat

    angle = atan2(lat_distance, long_distance) # Calculate from the X axis in radians
    angle = -degrees(angle) # Convert to degrees. Additionally, PIL uses angles anticlockwise so the negative value is required.

    if angle < 0: angle = 360 + angle # PIL also can't take negative values

    im = im.convert("RGBA") # Get an alpha channel to stop issues when rotating image
    im = im.rotate(angle, Image.NEAREST, expand = 1)

    background.paste(im, (int(x_length // 2 + long) - x_offset, int(y_length // 2 + lat) - y_offset), im) # Paste image onto main canvas
    old_long = raw_long
    old_lat  = raw_lat

    if percentage != int(i / end_image * 100): # Just for visual benefit to see how long it will take
        print(str(percentage) + "%")
        percentage = int(i / end_image * 100)



background.save("flightpath-wave-output.png")
