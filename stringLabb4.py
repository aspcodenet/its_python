mail = input("Mata in en mailadress")

valid = True
if mail.find("@") == -1:
    valid = False

print(len(mail))
pos = mail.rfind(".")    
if pos == -1:
    valid = False    
else:
    if pos < len(mail)-4 or pos > len(mail)-3:
        valid   = False    
print(valid)        
