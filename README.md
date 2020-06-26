# Astro-Pi-2019
My Astro Pi entry.

 My Python program was run for 2 and a half hours on the ISS, this repo contains the data and programs associated with that flight.

 The photos taken on flight and a video of them all strung together is available at https://jayhal.es/shared/astro-pi.

 At the current time the CSV file of the initial data, including longitude and latitude, has been converted into JSON and a crude HTML5 canvas project was created but suffered from performance issues when loading in the large amounts of images. If you download and unzip the images into a cloned repository the .gitignore file will not attempt to commit or push the files. Note the file must be called "images".

 ## Download and unzip the file: (Here)[https://jayhal.es/shared/astro-pi/compressed-images.zip into a file called] ```images``` in the repo.

 The below image is the current state of the image rendered by the Python program creating the flightpath of the ISS. At scale x0.1.
 Note: The dark section are during the night and the yellowish frames before and after these sections are due to reflection from the sun hitting the casing at the wrong angle. You might want to open the image in a new tab as its very large so you can zoom and explore at your own leisure.
 ![The current state of the image rendered by the Python program creating the flightpath of the ISS](./flightpath-wave-output.png)
