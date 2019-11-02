import datetime

idag = datetime.datetime.now()
jul = datetime.datetime(2019,12,24)

diff = jul - idag

print(f"Till julafton är det {diff.days} dagar")
