# 1 uzduotis

# skaicius = int(input("Įveskite skaičių: "))
# ar_skaicius_teigiamas = skaicius > 0
# print(ar_skaicius_teigiamas)

# alternatyva:

# print(int(input("Įveskite skaičių")) > 0)

# 2 uzduotis

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

# import datetime
# from datetime import timedelta

# now = datetime.datetime.now()
# print(now)
# print(now - timedelta(days=5))
# print(now + timedelta(hours=8))
# print(now.strftime("%Y %m %d, %X"))

# 3 uzduotis

import datetime

ivesta = input("Įveskite metus (YYYY-MM-DD HH:MM:SS) ")

ivesta_data = datetime.datetime.strptime(ivesta, "%Y-%m-%d %X")
now = datetime.datetime.now()
skirtumas = now - ivesta_data

print("Praėjo metų: ", skirtumas.days // 365)
print("Praėjo mėnesių: ", round(skirtumas.days / 365 * 12))
print("Praėjo savaičių: ", skirtumas.days // 7)
print("Praėjo dienų: ", skirtumas.days)
print("Praėjo valandų: ", round(skirtumas.total_seconds() / 3600))
print("Praėjo minučių: ", round(skirtumas.total_seconds() / 60))
print("Praėjo sekundžių: ", round(skirtumas.total_seconds()))


# jeigu norime laiko intervalą atvaizduoti taip, pvz:
# praėjo 2 metai, 7 mėnesiai, 23 dienos ir t.t.
# konsolėje: pip install python-dateutil

# from dateutil.relativedelta import relativedelta
# delta = relativedelta(datetime.datetime.now(), kazkokia_data)
# print(f'metu: {res.years}, menesiu {res.months}, dienu {res.days}, valandu {res.hours}') ir t.t.