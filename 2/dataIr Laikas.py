# import datetime

# x = datetime.datetime.today()
# print(x)

# x = datetime.date.today()
# print(x)

# x = datetime.datetime.today().time()
# print(x)

# y = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(y)

# print(y.strftime("%A, %d. %B %Y %I:%M%p"))

# ---------------------------

# import datetime
# import locale

# locale.setlocale(locale.LC_TIME, 'lt_LT.UTF-8')
# x = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(x.strftime("%A, %d. %B %Y %I:%M%p"))

# Kaip pridėti ar atimti laiką:

# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=5))
# print(now + datetime.timedelta(days=20, hours=8))

# Kaip sužinoti datų skirtumą (pvz. dienomis):

# import datetime
# now = datetime.datetime.now()
# nepriklausomybes_diena = datetime.datetime(1990, 3, 11)
# skirtumas = now - nepriklausomybes_diena
# print(skirtumas.days)

# import datetime
# ivesta_data = input("Įveskite datą: ")
# data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
# skirtumas = (datetime.datetime.now() - data)
# print(skirtumas.days)

# Kaip iš datetime atskirai ištraukti metus, mėnesį, valandas...?

# import datetime

# now = datetime.datetime.today()

# print(now.year)
# print(now.month)
# print(now.weekday())
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)


# Naudodami timedelta galime pamatuoti, per kiek laiko mūsų 
# kompiuteris susidorojo su užduotimi, pvz.:
# import datetime

# pradzia = datetime.datetime.today()
# for x in range(10000):
#     print("Labas")

# pabaiga = datetime.datetime.today()
# print(f"Programa užtruko {(pabaiga - pradzia).total_seconds()}")
