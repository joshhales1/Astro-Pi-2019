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

data_file = open("results.json")
data = json.loads(data_file.read()) # Load JSON file into program.
data_file.close()

boundries = {
"long max": float("inf"),
"long min": float("-inf"),
"lat max": float("inf"),
"lat min": float("-inf")
}


background = Image.new("RGB", (15000, 15000), (255, 255, 255)) # Set up the background, these values have no sigificant value as of the time of writing.


x = 512 # The pixel per degree constant.

for i in range(0, 10, 1):
    im = Image.open("images/zz_oba_" + str(i + 1) + ".jpg")
    im = im.crop((400, 0, 1500, 1080))
    im.putalpha(0)
    long = float(data[str(i)]["long"]) * x
    lat = float(data[str(i)]["lat"]) * x
    background.paste(im, (7500 - int(long), 7500 - int(lat)))


background.save("flightpath-output.png")
