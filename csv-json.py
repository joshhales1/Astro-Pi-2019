#The python programmed used to convert the CSV into JSON for the canvas project.
#Decided to keep developing it later in the project for reusability for other possible methods and languages.
import json

def degrees_to_decimal_degrees(degrees): # Colon seperated string. e.g. "130:30:21"
    output = degrees.split(":")
    output = float(output[0])//1 + float(output[1])/60 + float(output[2])/3600
    return output

old = open("runtime/first-results.csv")
oldText = old.read()
vals = {}
oldText = oldText.split("\n")

for i in range(1, len(oldText)): #To skip headers

    long = degrees_to_decimal_degrees(oldText[i].split(",")[0])
    lat  = degrees_to_decimal_degrees(oldText[i].split(",")[1])

    vals[i] = {
        "long": long,
        "lat": lat,
        "time": float(oldText[i].split(",")[3])
        }

newFile = open("results.json", "w+")
newFile.write(json.dumps(vals))
newFile.close()
