import os

for filename in os.listdir("c:\\kurser"):
    s = os.path.getsize("c:\\kurser\\" + filename)
    print(f"{filename} {s} bytes")
