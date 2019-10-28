correctuser = "stefan"
correctpwd = "secret"

username = input("Användarnamn:")
pwd = input("lösenord:")

if username != correctuser:
    print("Fel anv")
elif pwd != correctpwd:
    print("Fel lösen")
else:
    print("Du är inloggad")    

