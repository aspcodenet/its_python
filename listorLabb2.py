listaMedTal = []

antal = int(input("Hur många mätningar ska registreras?"))

for i in range(0,antal):
    n = float(input("Ange temp"))
    listaMedTal.append(n)

for temp in listaMedTal:
    print(temp)

summa = 0
maxTal = 0
antal = 0
for temp in listaMedTal:
    summa = summa + temp
    if temp > maxTal:
        maxTal = temp
    antal = antal + 1

print(f"Max:{maxTal}  Medel:{summa/antal}")
