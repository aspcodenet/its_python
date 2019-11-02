########## a
path = "c:\\hej\\test\\hello.txt"
pos = path.rfind("\\")
if pos == -1:
    print("Fanns ingen backslash")
else:   
    print(f"Sista backslash är på position {pos}")

########## b
txtEfter = path[pos+1:]
print(txtEfter)

########## c
if path.find("hej") >= 0:
    print("JA")


########    DEMOS

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