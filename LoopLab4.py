summa = 0
while True:
    tal = int(input("Mata in ett tal"))
    if tal == 0:
        break
    
    print(f"Du matade in {tal}")
    
    summa = summa + tal
    print(f"Summan av alla tal är {summa}")
