#A new effort to combine all the images at the correct distances apart to show the flightpath.
# Currently working on finding the scale of the images.

from PIL import Image
import json
import os

data_file = open("results.txt")
data = json.loads(data_file.read())
data_file.close()
background = Image.new("RGB", (15000, 15000), (255, 255, 255))


x = -20;
for i in range(0, 10, 1):
    im = Image.open("images/zz_oba_" + str(i + 1) + ".jpg")
    im = im.crop((400, 0, 1500, 1080))
    im.putalpha(0)
    long = float(data[str(i)]["long"]) * x
    lat = float(data[str(i)]["lat"]) * x
    background.paste(im, (7500 - int(long), 7500 - int(lat)))


background.show()
