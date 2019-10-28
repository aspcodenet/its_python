while True:
    tal1 = int(input("Ange tal 1:"))
    tal2 = int(input("Ange tal 2:"))
    summa = tal1 + tal2
    print(f"Summan är {summa}")
    if input("Vill du fortsätta J/N? ") != "J":
        break
