# Apžvelgsime:
# Failų kūrimas, skaitymas, rašymas
# Failų trynimas
# Išimčių valdymas

# Darbas su failais
# Python darbui su failais nebutina importuoti išorinių bibliotekų, 
# reikiamos funkcijos jau paprastai būna įtrauktos. 
# Naudojama open funkcija, kuri grąžina failo objektą, turintį
# reikiamus metodus ir atributus darbui su failu.

# Failų valdymas
# Vienas iš būdų darbui su failas yra open() funkcija.
# Ji turi du parametrus: failo vardas ir režimas (parodo kas bus daroma su failu)
# Galimi keturi darbo su failu režimai:
# "r" - Read - ši reikšmė priskirta pagal nutylėjimą. 
# Atidaro failą skaitymui, arba įvyksta klaida jei failas neegzistuoja
# "a" - Append - atidaro failą papildymui, sukuria naują, jei jis neegzistuoja
# "w" - Write - atidaro failą rašymui, sukuria naują, jei jis neegzistuoja
# "x" - Create - sukuria failą, įvyksta klaida jei toks failas egzistuoja

# Failą apdoroti (skaityti, rašyti ir kt.) galima kaip tekstinį arba dvejetainį:
# "t" - Text - reikšmė pagal nutylėjimą. Tekstinis režimas
# "b" - Binary - dvejetainis režimas (pavyzdžiui paveikslėliai)

# Pavyzdys:
f = open("demofile.txt") # f - kintamojo darbui su failu įvedimas - bet koks REIKŠMINGAS KINTAMOJO VARDA.
# neturi/gali sutapti su failo pavadinimu.
f = open("demofile.txt", "rt")
# Abi eilutės atlieka tą patį veiksmą, kadangi “r” parodo, kad failas atidaromas
# skaitymui, o “t” - kad tekstinis, šios abi reikšmės taip pat yra priskiriamos pagal
# nutylėjimą, jei nenurodyta kitaip.

# Failo skaitymas
# read(size=-1) - skaitomas visas failas arba size baitų kiekis (jei nurodytas)
# readline(size=-1) - skaitoma viena eilutė arba size simbolių skaičius (jei nurodytas)
# readlines() - skaito visas likusias eilutes iš failo objekto ir grąžina jas kaip sąrašą

# Skaitymas ir failo uždarymas
# Atidarius failą "open" ir atlikus norimus veiksmus, jį reikia uždaryti - close.

f = open("demofile.txt", "r")
print(f.readline())
f.close()

f = open("demofile.txt", "r")
for x in f:
 print(x)
f.close()


#=========================================================================================
import os 

# Kaip pažiūrėti, ką gali os modulis:
# print(dir(os))

# Kaip sužinoti katalogą, kuriame esame:
print(os.getcwd())

# Kaip pakeisti aktyvų katalogą, kuriame esame:
os.chdir('C:\\Users\\ginta\\OneDrive - Kaunas University of Technology\\Darbalaukis')
print(os.getcwd())

# Kaip pažiūrėti, kokie failai ir katalogai yra kataloge:
print(os.listdir())

# Kaip sukurti naują katalogą:
# os.mkdir("Naujas katalogas")
# arba
# os.makedirs("Naujas katalogas/Katalogas kataloge")
# print(os.listdir())

# Kaip sužinoti failo/katalogo informaciją:
print(os.stat("2D modeliavimas"))
# arba
print(os.stat("bilietai.pdf"))

# stat.ST_MODE - Inode protection mode.

# stat.ST_INO - Inode number.
# stat.ST_DEV - Device inode resides on.
# stat.ST_NLINK - Number of links to the inode.
# stat.ST_UID - User id of the owner.
# stat.ST_GID  - Group id of the owner.
# stat.ST_SIZE - Size in bytes of a plain file; amount of data waiting on some special files.
# stat.ST_ATIME - Time of last access.
# stat.ST_MTIME - Time of last modification.
# stat.ST_CTIME - The “ctime” as reported by the operating system. 
# On some systems (like Unix) is the time of the last metadata change, 
# and, on others (like Windows), is the creation time (see platform documentation for details).

# Kaip sužinoti failo dydį:
print(os.stat("bilietai.pdf").st_size) # baitais

# Kaip sužinoti kada failas buvo paskutinį kartą modifikuotas:
print(os.stat("bilietai.pdf").st_mtime)

# Pakeitus suprantamu formatu:
from datetime import datetime

data = os.stat("bilietai.pdf").st_mtime
print(datetime.fromtimestamp(data))

# Tekstinių failų kūrimas ir nuskaitymas
# Kaip sukurti tekstinį failą: (jei failo nėra, bus sukurtas naujas, jei yra - bus įrašoma jame)


print(os.getcwd())
os.chdir('C:\\Users\\ginta\\OneDrive - Kaunas University of Technology\\Darbalaukis\\Naujas katalogas')
print(os.getcwd())

#with open("failas.txt", 'w') as failas:
#    failas.write("Sveikas, pasauli!")

# arba rečiau naudojamas
#failas = open("failas.txt", 'w')
#failas.write("Labas, pasauli!")
#failas.close()

# Kaip nuskaityti tekstą iš failo:
#with open("failas.txt", 'r') as failas:
#    print(failas.read())

# Kaip įrašyti ir nuskaityti failą vienu metu:
#with open("failas.txt", 'r+') as failas: # be + not writable
 #   print(failas.read())
#    failas.write("Labas rytas, pasauli!")

#with open("failas.txt", 'r') as failas:
#    print(failas.read())

# Kaip į failą įrašyti lietuviškus rašmenis: Problema:
# with open("failas.txt", 'w') as failas:
#    failas.write("Čia yra pirmas failo sakinys")
# UnicodeEncodeError: 'charmap' codec can't encode character '\u010c' in position 0: character maps to <undefined>

# Sprendimas:
#with open("failas.txt", 'w', encoding="utf-8") as failas:
#    failas.write("Čia yra pirmas failo sakinys")

# Kaip nuskaityti failą su lietuviškais rašmenimis:
#with open("failas.txt", 'r') as failas:
#    print(failas.read())
# ÄŒia yra pirmas failo sakinys

#with open("failas.txt", 'r', encoding="utf-8") as failas:
#    print(failas.read())

# Kaip pridėti, o ne perrašyti failo eilutę:

# with open("failas.txt", 'w', encoding="utf-8") as failas:
#   failas.write("Test")
#    failas.write("Test")

# with open("failas.txt", 'w', encoding="utf-8") as failas:
#    failas.write("Test")
#    failas.seek(0)
#    failas.write("BE")

with open("failas.txt", 'r', encoding="utf-8") as failas:
    print(failas.readline())
    print(failas.readline())
    print(failas.readline())

with open("failas.txt", 'r', encoding="utf-8") as failas:
    print(failas.readlines())

import pickle
# Marinavimo modulis įgyvendina dvejetainius protokolus, skirtus Python objektų struktūros serializavimui ir išserializavimui. 
# „Pickling“ yra procesas, kurio metu „Python“ objektų hierarchija konvertuojama į baitų srautą, 
# o „atrinkimas“ yra atvirkštinė operacija, kai baitų srautas (iš dvejetainio failo arba į baitus panašaus objekto) 
# paverčiamas atgal į objektų hierarchiją. 
# Marinavimas (ir išėmimas) kitaip vadinamas „serializavimu“, „rūšiavimu“, 1 arba „išlyginimu“ (“serialization”, “marshalling,” or “flattening”); tačiau, siekiant išvengti painiavos, čia vartojami terminai „marinavimas“ ir „atrinkimas“ (“pickling” and “unpickling”).
class Automobilis:
    def __init__(self, marke, modelis):
        self.marke = marke
        self.modelis = modelis

automobiliai = [Automobilis("Toyota", "Avensis"), Automobilis("Toyota", "Corolla"), Automobilis("Toyota", "Camry")]

with open("automobilis.pkl", "wb") as failas: #write binarry
    pickle.dump(automobiliai, failas)

with open("automobilis.pkl", "rb") as failas: #read binarry
    automobiliai = pickle.load(failas)
    for automobilis in automobiliai:
        print("Markė", automobilis.marke)
        print("Modelis", automobilis.modelis)