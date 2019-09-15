lista = []
summa = 0
while True:
    tal = int(input("Mata in ett tal"))
    if tal == 0:
        break
    print(f"Du matade in {tal}")
    
    summa = summa + tal
    print(f"Summan av alla tal är {summa}")
    
    lista.insert(0,tal)
    lenToCount = len(lista)
    if lenToCount > 3:
        lenToCount = 3
    summaAttBeraknaMedelPa =  0

    antalTillagda  = 0
    for i in lista:
        summaAttBeraknaMedelPa = summaAttBeraknaMedelPa + i
        antalTillagda = antalTillagda + 1
        if antalTillagda == lenToCount:
            break
    print(f"Medelvärde på de {lenToCount} senaste är {summaAttBeraknaMedelPa/lenToCount}")
