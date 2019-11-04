listaMedTal = []
for nr in range(1,5):
    n = int(input(f"Ange tal nummer {nr}"))
    listaMedTal.append(n)

# antal = 0
# while antal < 4:
#     n = int(input("Ange tal"))
#     listaMedTal.append(n)
#     antal = antal + 1


greatestSoFar = 0
for i in listaMedTal:
    if i > greatestSoFar:
        greatestSoFar = i

print(f"Största talet är {greatestSoFar}")
