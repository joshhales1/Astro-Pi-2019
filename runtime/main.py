#Import required module
from picamera import PiCamera
from time import sleep, time
from ephem import readtle
#Initiate ISS data
stationName = "ISS (ZARYA)"
line1 = "1 25544U 98067A   20043.56222881  .00000636  00000-0  19643-4 0  9995"
line2 = "2 25544  51.6443 250.0442 0004805 259.3788 151.6176 15.49157075212546"
iss = readtle(stationName, line1, line2)
#Initiate camera and set start time
camera = PiCamera()
startTime = time()
#Write headers into output file
f = open('results.csv', 'w+')
f.write("Long,Lat,#,Time\n")
f.close()
i = 0
runLength = 2.5 * 60 * 60
#While the time differenece from start to now is less than run length
while time() - startTime < runLength:
  i += 1
  #Take photo and compute ISS data
  camera.capture(str(i)+'.jpg')
  iss.compute()
  #Open log file and write long, lat, photo number and current time
  f = open("results.csv", "a")
  f.write("{},{},{},{}\n".format(str(iss.sublong), str(iss.sublat), str(i), str(time())))
  f.close()
  print("Data captured and stored." + str(int(((time() - startTime) / runLength) * 100)) + "%")
  #Wait 3 secs before continuing 
  sleep(3)
print("End of program")



