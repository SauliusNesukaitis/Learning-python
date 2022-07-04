# Išimtys ir jų suvaldymas
# Last Updated: Apr 25, 2022 by Gedas Gardauskas

7 / 0
# ZeroDivisionError: division by zero


skaicius = int(input("Įveskite skaičių: "))
# Įveskite skaičių: k11
# ValueError: invalid literal for int() with base 10: 'k11'
# Ką daryti, kad programa išmestų norimą pranešimą ir nesustotų? Variantas:


dalinys = 7
daliklis = 0
if daliklis == 0:
    print("Dalyba iš nulio negalima")
else:
    dalinys / daliklis
print("Programa vykdoma toliau")

# Dalyba iš nulio negalima
# Programa vykdoma toliau
# Klaidų suvaldymas naudojant try/except:

try:
    7 / 0
except:
    print("Dalyba iš nulio negalima")
    
# Dalyba iš nulio negalima


try:
    skaicius = int(input("Įveskite skaičių: "))
except:
    print("Įvestas klaidingas skaičius")
    
# Įveskite skaičių: k11
# Įvestas klaidingas skaičius


try:
    open('file.txt')
except:
    print("Nepavyksta atidaryti failo")

print("Programa vykdoma toliau")

# Nepavyksta atidaryti failo
# Programa vykdoma toliau
# Kuo naudingas try/except/finally naudojimas:
# Leidžia pakeisti klaidų pranešimus norimu tekstu

# Įvykus klaidai, programa nesustoja (apsaugo nuo lūžimo). Po neįvykdyto kodo, programa vykdoma toliau

# Leidžia nuspręsti, ką daryti, atsiradus klaidai (pvz., išmesti tam tikrą pranešimą, paleisti kitą funkciją ir t.t

# Kaip suvaldyti kelias išimtis:

try:
    skaicius = int(input("Įveskite skaičių: "))
    print(7 / skaicius)
    open('file.txt')
except ZeroDivisionError:
    print("Dalyba iš nulio negalima")
except ValueError:
    print("Įvestas klaidingas skaičius")
except FileNotFoundError:
    print("Nepavyko atidaryti failo")

# Įveskite skaičių: k11
# Įvestas klaidingas skaičius


# Įveskite skaičių: 0
# Dalyba iš nulio negalima


# Įveskite skaičių: 7
# 1.0
# Nepavyko atidaryti failo
# Galimų klaidų sąrašas: https://docs.python.org/3/library/exceptions.html 

# Finally
# (kodas, vykdomas nepaisant to, kas įvyksta try/except blokuose)


try:
    print(7 / 0)
except:
    print("Dalyba iš nulio negalima")
finally:
    print("Todėl įvykdysime daugybą: ")
    print(7 * 7)
print("Programa vykdoma toliau")


# Dalyba iš nulio negalima
# Todėl įvykdysime daugybą:
# 49
# Programa vykdoma toliau
# Kaip panaudoti try/except įvedant duomenis:

while True:
    try:
        x = int(input("Įveskite skaičių: "))
        break
    except ValueError:
        print("Įvedėte ne skaičių. Bandykite dar kartą")