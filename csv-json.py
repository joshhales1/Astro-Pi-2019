import json
old = open("Raw results.csv")
new = open("new long lats.txt")

oldText = old.read()
newText = new.read()

vals = {};



oldText = oldText.split("\n")
newText = newText.split("\n")

for i in range(len(oldText)):
    vals[i] = {
        "long": newText[i].split(",")[0],
        "lat": newText[i].split(",")[1],
        "time": oldText[i].split(",")[3]        
        }

newFile = open("results.txt", "w+")
newFile.write(json.dumps(vals))
newFile.close()



