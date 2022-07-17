# 1 užduotis
# Python faile padaryti šiuos veiksmus (atskirai, ne iškart):
# Importuoti modulį datetime. Atsispausdinti šiandienos datą ir laiką kartu, tik datą (date.today()) bei tik laiką (.now().time()).
# Iš paketo datetime importuoti modulį date. Atsispausdinti šiandienos datą.
# Iš paketo datetime importuoti modulį date kaip data (as data). Atsispausdinti šiandienos datą.

# import datetime
# print(datetime.date.today())
# print(datetime.datetime.now().time())
# from datetime import date
# print(date.today())

# 4 užduotis
# Sukurti programą, kuri:
# Leistų vartotojui įvesti norimą eilučių kiekį
# Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
# Patarimai:
# Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)

# tekstas = ""

# while True:
#     pirmas = input("Iveskite eilute: ")
#     if pirmas != "":
#         tekstas += pirmas + "\n"
#     else:
#         break

# failo_pavadinimas = input("Iveskita failo pavadinima: ")
# with open(failo_pavadinimas + ".txt", "w", encoding="UTF-8") as failas:
#     failas.write(tekstas)

# 5 užduotis
# Sukurti programą, kuri:
# Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
# Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
# Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
# Patarimai:
# Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime

import os
from datetime import datetime

# try:
#     os.chdir('C:\\Users\\MSI\OneDrive\\Desktop')
#     os.mkdir("Naujas katalogas")
# except:
#     "Toks katalogas jau yra"

# os.chdir('C:\\Users\\MSI\\OneDrive\\Desktop\\Naujas katalogas')

# with open("data.txt", "w") as failas:
#     failas.write(str(datetime.today()))

os.chdir('C:\\Users\\MSI\\OneDrive\\Desktop\\Naujas katalogas')
print("Sukurimo data:", datetime.fromtimestamp(os.stat("data.txt").st_ctime))
print("failo dydis:", os.stat("data.txt").st_size)


