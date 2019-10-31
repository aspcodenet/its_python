txt = "Stefan Holmberg"
txt = txt.lower()
print(txt)

while True:
    fortsatt = input("Vill du fortsätta J/N?")
    fortsatt = fortsatt.upper()
    if fortsatt != "J":
        break

variabel = "c:\\hej\\test\\hello.txt"

if variabel.find("hejqq") == -1:
    print("Nej")
else:
    print("Ja")