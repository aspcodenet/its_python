listaMedTal = []
for i in range(0,4):
    n = int(input("Ange ett tal"))
    listaMedTal.append(n)

greatestSoFar = 0
for i in listaMedTal:
    if i > greatestSoFar:
        greatestSoFar = i

print(f"Största talet är {greatestSoFar}")
