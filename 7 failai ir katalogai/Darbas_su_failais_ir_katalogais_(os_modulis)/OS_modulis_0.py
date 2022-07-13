# Apžvelgsime:
# Failų kūrimas, skaitymas, rašymas
# Failų trynimas
# Išimčių valdymas

# Darbas su failais
# Python darbui su failais nebutina importuoti išorinių bibliotekų, 
# reikiamos funkcijos jau paprastai būna įtrauktos. 
# Naudojama open funkcija, kuri grąžina failo objektą, turintį
# reikiamus metodus/funkcijas ir atributus darbui su failu.

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
# demofile = open("demofile.txt") # f - kintamojo darbui su failu įvedimas - bet koks REIKŠMINGAS KINTAMOJO VARDAS.
# neturi/gali sutapti su failo pavadinimu.
# demofile = open("demofile.txt", "rt")
# Abi eilutės atlieka tą patį veiksmą, kadangi “r” parodo, kad failas atidaromas
# skaitymui, o “t” - kad tekstinis, šios abi reikšmės taip pat yra priskiriamos pagal
# nutylėjimą, jei nenurodyta kitaip.

# Failo skaitymas
# read() - skaitomas visas failas arba size baitų kiekis (jei nurodytas)
# readline(size=-1) - skaitoma viena eilutė arba size simbolių skaičius (jei nurodytas)
# readlines() - skaito visas likusias eilutes iš failo objekto ir grąžina jas kaip sąrašą

# Skaitymas ir failo uždarymas
# Atidarius failą "open" ir atlikus norimus veiksmus, jį reikia uždaryti - "close".

# demofile = open("demofile.txt", "r", encoding="utf-8")
# print(demofile.readline())
# demofile.close()

# demofile = open("demofile.txt", "r")
# for eilute in demofile:
#     print(eilute)
# demofile.close()

# Failo rašymas
# .write(string) - teksto rašymas į failą
# .writelines(seq) - sekos rašymas į failą. Eilutės pabaigos simboliai nepridedami.

# Rašymas į egzistuojantį failą

# Reikia pakeisti open() metodo parametrą:
# "a" - Append - papildymas failo pabaigoje
# "w" - Write - failo turinio perrašymas

#demofile = open("demofile.txt", "w")
#demofile.write("Teksto papildymas faile!")
#demofile.close()

# atidaryti ir skaityti failą po papildymo:
#demofile = open("demofile.txt", "r")
#print(demofile.read())
#demofile.close()

# Vieta faile
# tell() - pagalba gaunama dabartinė vieta faile. Sekantis skaitymas ar rašymas prasidės nuo šios vietos

#seek(offset[, from]) - pakeičia vietą faile. Pirmas argumentas nurodo per kiek baitų pereiti pirmyn, 
# o antras - nuo kurios vietos.
# Galimos parametro from reikšmės:
# 0 - pradedama nuo failo pradžios
# 1 - pradedama nuo dabartinės vietos
# 2 - pradedama nuo failo pabaigos

# PAVIZDYS:

#demofile = open("demofile.txt", "r+") # be + not writable
#str = demofile.read(3)
#print ("Perskaitytas tekstas: ", str)

# Tikriname dabartinę vietą
#position = demofile.tell()
#print ("Vieta faile: ", position)

# Perkeliame rodyklę į pradžią
#position = demofile.seek(0, 1)
#str = demofile.read(6)
#print ("Dar kartą perkskaitytas tekstas: ", str)

#demofile.close()

# Failo sukūrimas
#file1 = open("file1.txt", "x")
#file2 = open("file2.txt", "w")

# Failų trynimas
# Norint ištrinti failą, reikia įtraukti OS modulį ir panaudoti os.remove() funkciją:
import os

#if os.path.exists("file1.txt"):
   # os.remove("file1.txt")
#else:
    #print("Filas neegzistuota")

# Sukurti kataloga
# os.mkdir("myfolder")

# Katalogo trinimas
# os.rmdir("myfolder")

# Failo pervadinimas
# os.rename(current_file_name, new_file_name)

# skirtas failo vardo keitimui. Naudojamas OS modulis, jį reikia įtraukti prieš naudojant rename.
# os.rename("file3.txt", "file.txt")

# Veiksmai su direktorijomis
# Naudojami OS objekto metodai:
# os.mkdir("newdir") - naujos direktorijos sukūrimas einamojoje direktorijoje.
# Kaip parametras perduodamas naujos direktorijos pavadinimas

# os.chdir("newdir") - einamosios direktorijos keitimas. Parametras nurodo į kurią direktoriją norima keisti.

# os.getcwd() - einamosios darbinės direktorijos gavimas.

# os.rmdir('dirname') - direktorijos šalinimas pagal nurodytą argumentą. Prieš trinant direktoriją,
#  visas jos turinys turi būti pašalintas.

# Sukurti direktoriją "dokumentai"
# os.mkdir("dokumentai")

# Pakeisti direktoriją į "/dokumentai/CA"
# os.chdir("C:/Users/ginta/OneDrive - Kaunas University of Technology/Darbalaukis/Code_Academy/Darbas_su_failais_ir_katalogais_(os_modulis)/dokumentai/CA")

# os.chdir("C:/Users/ginta/OneDrive - Kaunas University of Technology/Darbalaukis/Code_Academy/Darbas_su_failais_ir_katalogais_(os_modulis)")
# Dabartinė direktorija
# print(os.getcwd())

# Ištrinti direktoriją "/dokumentai/CA"
# os.rmdir("C:/Users/ginta/OneDrive - Kaunas University of Technology/Darbalaukis/Code_Academy/Darbas_su_failais_ir_katalogais_(os_modulis)/dokumentai/CA")
# os.rmdir("C:/Users/ginta/OneDrive - Kaunas University of Technology/Darbalaukis/Code_Academy/Darbas_su_failais_ir_katalogais_(os_modulis)/dokumentai")

# Kaip pažiūrėti, ką gali os modulis:
# print(dir(os))

# Kaip sužinoti katalogą, kuriame esame:
# print(os.getcwd())

# Kaip pakeisti aktyvų katalogą, kuriame esame:
# os.chdir('C:\\Users\\ginta\\OneDrive - Kaunas University of Technology\\Darbalaukis')

# Kaip pažiūrėti, kokie failai ir katalogai yra kataloge:
# print(os.listdir())

# Kaip sukurti naują katalogą:
# os.mkdir("Naujas katalogas")
# arba
# os.makedirs("Naujas katalogas/Katalogas kataloge")
# print(os.listdir())

# Kaip sužinoti failo/katalogo informaciją:
# print(os.stat("demofile.txt"))
# print(os.stat("Naujas katalogas"))

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
#print(os.stat("demofile.txt").st_size) # baitais

# Kaip sužinoti kada failas buvo paskutinį kartą modifikuotas:
#print(os.stat("demofile.txt").st_mtime) 

# Pakeitus suprantamu formatu:
#from datetime import datetime

#data = os.stat("demofile.txt").st_mtime
#print(datetime.fromtimestamp(data))

# irasimas i faila KITAS BUDAS
#with open("demofile.txt", 'w') as failas:
#    failas.write("Sveikas pasauli!")

# Kaip nuskaityti tekstą iš failo:
#with open("demofile.txt", 'r') as failas:
#    print(failas.read())

# Kaip įrašyti ir nuskaityti failą vienu metu:
#with open("demofile.txt", 'r+') as failas: # be + not writable   
#    print(failas.read())
#    failas.write("Labas rytas, pasauli!")

# Kaip į failą įrašyti lietuviškus rašmenis: Problema:
#with open("demofile.txt", 'w') as failas:
#    failas.write("Čia yra pirmas failo sakinys")
#UnicodeEncodeError: 'charmap' codec can't encode character '\u010c' in position 0: character maps to <undefined> 

# Sprendimas:
#with open("demofile.txt", 'w', encoding="utf-8") as failas:
#    failas.write("Čia yra pirmas failo sakinys")

# Kaip nuskaityti failą su lietuviškais rašmenimis:
#with open("demofile.txt", 'r') as failas:
#    print(failas.read())
# ÄŒia yra pirmas failo sakinys

#with open("demofile.txt", 'r', encoding="utf-8") as failas:
#    print(failas.read())

# Kaip pridėti, o ne perrašyti failo eilutę:
#with open("demofile.txt", 'w', encoding="utf-8") as failas:
#    failas.write("Test ")
#    failas.write("Kitas")
#   failas.write("\nTest")

# '''
# with open("demofile.txt", 'w', encoding="utf-8") as failas:
#     failas.write("Test")
#     failas.seek(0)
#     failas.write("BE")
# '''

#with open("demofile.txt", 'r', encoding="utf-8") as failas:
   # print(failas.readline())
   # print(failas.readline())

#with open("demofile.txt", 'r', encoding="utf-8") as failas:
   # print(failas.readlines())

# Iteravimas per failo eilutes:
#with open("demofile.txt", 'r', encoding="utf-8") as failas:
    #for eilute in failas:
       # print(eilute)

#with open("demofile.txt", 'r', encoding="utf-8") as failas:
    #print(failas.readlines())

# kad nebūtų tarpų tarp eilučių:
#with open("demofile.txt", 'r', encoding="utf-8") as failas:
    #for eilute in failas:
      #  print(eilute, end="")

# Kaip nuskaityti ribotą kiekį duomenų:
# with open("demofile.txt", 'r', encoding="utf-8") as failas:
#     print(failas.read(18))
#     print(failas.read(19))
#     print(failas.read(20))
#     print(failas.read(22))

# Darbas su dviem failais (teksto kopijavimas iš vieno į kitą):
# with open("demofile.txt", 'r', encoding="utf-8") as r_failas:
#     with open("demofile_kopija.txt", 'w', encoding="utf-8") as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)

# Dvejetainių failų kopijavimas:
# Problema:
# with open("logo.png", 'r') as r_failas:
    # with open("logo_kopija.png", 'w') as w_failas:
       #  for r_eilute in r_failas:
          #  w_failas.write(r_eilute)
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 238: character maps to <undefined>

#Sprendimas:
# with open("logo.png", 'rb') as r_failas:
#     with open("logo_kopija.png", 'wb') as w_failas:
#         for r_eilute in r_failas:
#             w_failas.write(r_eilute)

#Kaip į failą išsaugoti kintamuosius/objektus
import pickle
# Marinavimo modulis įgyvendina dvejetainius protokolus, skirtus Python objektų struktūros serializavimui 
# ir išserializavimui. 
# „Pickling“ yra procesas, kurio metu „Python“ objektų hierarchija konvertuojama į baitų srautą, 
# o „atrinkimas“ yra atvirkštinė operacija, kai baitų srautas (iš dvejetainio failo arba į baitus panašaus objekto) 
# paverčiamas atgal į objektų hierarchiją. 
# Marinavimas (ir išėmimas) kitaip vadinamas „serializavimu“, „rūšiavimu“, 1 arba „išlyginimu“ 
# (“serialization”, “marshalling,” or “flattening”); 
# tačiau, siekiant išvengti painiavos, čia vartojami terminai „marinavimas“ ir „išmarinavimas“ (“pickling” and “unpickling”).

# a = 1024
# with open("a.pkl", 'wb') as picle_out:
#     pickle.dump(a, picle_out)

# Nuskaitymas
# with open("a.pkl", "rb") as pickle_in:
#     naujas_a = pickle.load(pickle_in)

# print(naujas_a)

# Išsaugome masyvą:
# Įrašymas:
# zodynas = {1:"Pirmas", 2:"Antras", 3:"Trečias"}
# with open("zodynas.pkl", "wb") as pickle_out:
#     pickle.dump(zodynas, pickle_out)

# nuskaitymas
# with open("zodynas.pkl", "rb") as pickle_in:
#     naujas_zodynas = pickle.load(pickle_in)

# print(naujas_zodynas)

# Išsaugome daug kintamųjų (Pickle):
# a = 2
# b = 10
# c = 121

# with open("abc.pkl", "wb") as pickle_out:
#     pickle.dump(a, pickle_out)
#     pickle.dump(b, pickle_out)
#     pickle.dump(c, pickle_out)

# Nuskaitymas:
# with open("abc.pkl", "rb") as pickle_in:
#     nauja_a = pickle.load(pickle_in)
#     nauja_b = pickle.load(pickle_in)
#     nauja_c = pickle.load(pickle_in)

# print(nauja_a)
# print(nauja_b)
# print(nauja_c)

# arba 
# with open("abc.pkl", "rb") as pickle_in:
#     while True:
#         try:
#             print(pickle.load(pickle_in))
#         except EOFError: # Python sistemoje EOFEror yra išimtis, kuri iškyla, kai tokios funkcijos kaip input() ir raw_input() grąžina failo pabaigą (EOF), neskaitant jokios įvesties.
#             break

#Pavyzdys su vardų sąrašu:

# while True:
#     veiksmas = int(input("Pasirinkite veiksma: 1 - perziureti, 2 - irasyti, 3 - iseiti"))
#     if veiksmas == 1:
#         try:
#             with open("zmones.pkl", 'rb') as failas:
#                 print(pickle.load(failas))
#         except:
#             print("nera tokio failo")
#             with open("zmones.pkl", 'wb') as failas:
#                 zmones = []
#                 pickle.dump(zmones, failas)
#     if veiksmas == 2:
#         with open("zmones.pkl", 'rb') as failas:
#             zmones = pickle.load(failas)
#             vardas = input("Iveskite nauja varda")
#             with open("zmones.pkl", 'wb') as failas:
#                 zmones.append(vardas)
#                 pickle.dump(zmones, failas)
#     if veiksmas == 3:
#         print("Programa baigta")
#         break

# # Pavyzdys su objektų sarašu:

# class Automobilis:
#     def __init__(self, marke, modelis):
#         self.marke = marke
#         self.modelis = modelis

# automobiliai = [Automobilis("Toyota", "Avensis"), Automobilis("Toyota", "Corolla"), Automobilis("Toyota", "Camry")]

# with open("automobilis.pkl", 'wb') as gintare:
#     pickle.dump(automobiliai, gintare)

# with open("automobilis.pkl", 'rb') as paskauskaite:
#     automobiliai = pickle.load(paskauskaite)
#     for automobilis in automobiliai:
#         print("Marke", automobilis.marke)
#         print("modelis", automobilis.modelis)
