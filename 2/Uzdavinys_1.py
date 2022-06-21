#UZDUOTIS_1
#Visus sąraše minimumus pakeiskite input pagalba pasirinkta raide
#1 etapas: suformavome X elemntu dydzio atsitiktiniu skaiciu masyva pagal nurodytus rezius Nuo - iki naudodami funkcija input.
import random
masyvo_dydis = int(input('Iveskite teigiama sveikaji skaiciu nurodanti masyvo dydi: ')) #teigiama sveikaji skaiciu
atsistiktiniu_skaiciu_formavimo_pradzia = int(input('Iveskite skaiciu nurodanti skaiciu masyvo formavimo elemnetu pradzia: '))
atsistiktiniu_skaiciu_formavimo_pabaiga = int(input('Iveskite skaiciu nurodanti skaiciu masyvo formavimo elemnetu pabaiga: '))
atsitiktiniu_skaiciu_masyvas = [random.randrange(atsistiktiniu_skaiciu_formavimo_pradzia,atsistiktiniu_skaiciu_formavimo_pabaiga) for i in range(masyvo_dydis)]
print('atsitiktiniu skaiciu masyvas \n', atsitiktiniu_skaiciu_masyvas)

#2 etapas: paprasome vartotojo ivesti raide kuria naudosime maziausiu reiksmiu atsitiktiniu skaiciu masyve sukeitimui
raide = input('Kokia raide norite pakeisti maziausias atsitiktiniu skaiciu masyvo vertes? ') # kaip patikrinti kad nebutu skaicius o tikrai raide

#3 etapas: susirandame maziausia reiksme atsitiktiniu skaiciu masyve
maziausia_reiksme = atsitiktiniu_skaiciu_masyvas[0]

for skaicius in atsitiktiniu_skaiciu_masyvas:
    if skaicius < maziausia_reiksme:
        maziausia_reiksme = skaicius
print('Maziausia masyvo reiksme: ', maziausia_reiksme)

#4 etapas: suskaiciuoju kiek tokiu reiksmiu yra
print("Maziausiu rieksmiu atsistiktiniu skaiciu masyve yra: ", atsitiktiniu_skaiciu_masyvas.count(maziausia_reiksme))

#5 etapas: pakeiciame visas maziausias reiksmes nurodyta raide
indeksas = 0
for skaicius in atsitiktiniu_skaiciu_masyvas:
    if skaicius == maziausia_reiksme:
        atsitiktiniu_skaiciu_masyvas[indeksas] = raide
        print('Maziausios reiksmes vieta: ', indeksas+1)
    indeksas+=1 # indeksas = indeksas + 1

#6 etapas: atspausdiname nauja atsistiktiniu skaiciu masuva su pakeistomis maziausiomis reiksmemis
print('Naujas atsitiktiniu skaiciu masyvas: ', atsitiktiniu_skaiciu_masyvas)

