import os
import datetime

datum = datetime.datetime.now()
if(datum.month == 10):
    print("Åhh fyy oktober");
if(datum.day == 1):
    print("jsdfiljasf");
if(datum.hour > 9):    
    print("jsdfiljasf");


ago = datum - datetime.timedelta(days=52)


datum1 = datetime.datetime.now()
datum2 = datetime.datetime(2019,12,24,15,0,0)
d = datum2 - datum1
print(d)



filAtLoggaStatusI = "c:\\kurser\\status.txt"


listOfAllFiles = os.listdir("c:\\kurser")

with open(filAtLoggaStatusI, "a") as myfile:
    myfile.write(f"{datetime.datetime.now()} Nu startar Claes-scriptet\n")

listOfLogFiles = []
for filnamn in listOfAllFiles:
    if filnamn.find(".log") != -1:
        listOfLogFiles.append(filnamn)

with open(filAtLoggaStatusI, "a") as myfile:
    myfile.write(f"{datetime.datetime.now()} Hittade {len(listOfLogFiles)} loggfiler\n")



if not os.path.exists("c:\\kurser\\claes"):
    os.makedirs("c:\\kurser\\claes")

filesWithClaesIn = []
for filnamn in listOfLogFiles:
    with open("c:\\kurser\\" + filnamn) as myfile:
        if "Claes" in myfile.read():
            filesWithClaesIn.append(filnamn)


with open(filAtLoggaStatusI, "a") as myfile:
    myfile.write(f"{datetime.datetime.now()} Hittade {len(filesWithClaesIn)} Claes filer\n")


for filnamn in filesWithClaesIn:
    os.rename("c:\\kurser\\" + filnamn, "c:\\kurser\\claes\\" + filnamn)            

# gå igenom alla filer som slutar på *.log
# i biblioteket c:\kurser
# om texten Claes finns där så ska filen
# flyttas till c:\kurser\claes
# skapa mappen claes om den inte finns







a = os.listdir("c:\\kurser")
























listaMedTal = []
for i in range(0,4):
    n = int(input("Ange ett tal"))
    listaMedTal.append(n)

greatestSoFar = 0
for i in listaMedTal:
    if i > greatestSoFar:
        greatestSoFar = i













goodPlayers = ["Foppa"]
while True:
    print("Bra spelare är")
    for box in goodPlayers:
        print(box)
    ny = input("Säg en bra spelare du?")
    goodPlayers.append(ny)





age = 12
if age < 18:
    print(f"{age} - ungdom")
    print("Så priset blir 22 kr")

year = 2000
while year < 2020:
    print(year)
    year = year + 1

while True:
    #anropa arp -a
    #nmap 
    #stoppa alla MAC-adresser i en LISTA
    #for loop i listan
        #if address finns i WHITELIST OK
        # annars larma - skicka mail !! Intruder???



    print("Hello")
    c = input("Do you want to continue J/N?") 
    if c == "N":
        break

for i in range(2000,2020):
    print(i)






stefansBarn = ["Fanny", "Josefine", "Oliver"]
for box in stefansBarn:
    print(box)

barn1 = "Fanny"
barn2 = "Josefine"
barn3 = "Oliver"
print(barn1)
print(barn2)
print(barn3)








print(stefansBarn[0])




for i in range(10,15):
    print("Hej")

for i in range(2000,2020):
    print(i)



pris = 1000
pris = pris / 2

pris = 22
if pris >= 100 and pris < 200:    
    print("Ganska billigt")
elif pris < 100:
    print("Oj vad billigt")
else:    
    print("Oj vad dyrt")


print(pris)
moms = pris * 0.2 
print(moms)





print("12*10")



print("Hejsan ITS!")
print(12.231312231)
print(True)
namn = "Stefan "
namn2 = "Holmberg" 
fullName = namn + namn2
print(fullName)


for filnamn in listOfAllFiles:
    if filnamn.find(".log") != -1:
        print(filnamn)




res = namn.find(".log")
print(res)
