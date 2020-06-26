# Astro Pi 2019
### Josh Hales

## The story
The project originally began with an attempt to use 4 band images, RGB and near infrared, and cross reference the data obtained via [NVDI](https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index) with pollution levels of the surrounding area and observe the effect that it had on plant life. However, due to my own sole mistake I managed to take the photos with no near infrared band, rendering our entire project useless. Rather than give up on the project I decided to change the direction and work on compiling all 2,500 images into a collage in their correct positions (and rotations I would later find).

## The project
The first part of this write up will contain the journey I went on to get to my current situtation.

### Day 1
Having already released my mistake on capturing the wrong file type I got to work attempting to compile all the images into a stop motion video. I played around in JS canvas, an environment I was already very comfortable with, for a while attempting to make a video I could later capture. I immediately ran into issues of loading the images into memory and latency in rendering them. After experimenting with JS workers and moving to a local server the loading times became unusable. Having to load them across network as well only made these issues worse.

I eventually put them all into Premier Pro to just create a video I could share with my family and friends. 

I then moved to Python, drawn by the PIL module and a strong foundation in the langauge. I immediately released that there was no way I could ever hope to accurately position the images without knowing the scale of the images. Attempts to find the FOV of the camera were inconclusive, with not enough evidence to support basing the whole project of. With the FOV some basic trigonometry could have revealed the scale of the images. The next solution presented itself in the city of Dakar.

