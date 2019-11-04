import os
import datetime

listOfLogFiles = []
listOfAllFiles = os.listdir("c:\\kurser")
for filnamn in listOfAllFiles:
    if filnamn.find(".log") != -1:
        listOfLogFiles.append(filnamn)
        print(filnamn)






with open("c:\\logfile.txt", "a") as myfile:
    myfile.write(f"{datetime.datetime.now()} Nu startar Claes-scriptet\n")

