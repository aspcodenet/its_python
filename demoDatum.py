import datetime

justNu = datetime.datetime.now()
if justNu.month == 11 and justNu.day == 4:
    print("Grattis syrran") 
if justNu.hour == 20:
    print("Dags att sova")

julAfton = datetime.datetime(2019,12,24,15,0,0)    
diff = julAfton - justNu
print(diff)


thirtyDaysAgo = justNu + datetime.timedelta(days=-30)
print(thirtyDaysAgo)

