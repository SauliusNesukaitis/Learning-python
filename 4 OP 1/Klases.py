
# Kaip sukuriama objekto klasė: (Kaip sukurti objektą su skirtingu kiekiu savybių:)
class Kate:
    def __init__(self, spalva, kojos): # self lieka visada - gali vadintis kitaip
        self.spalva = spalva
        self.kojos = kojos 

#Kaip sukuriamas metodas (objekto funkcija):
    def miaukseti(self):
        print("Miau")
    
    def _judinti_kojas(self):
        print("Judinu visas kojas")

    def _ziureti_kur_begi(self):
        print("Neziuriu ku begu")

    def begti(self):
        self._judinti_kojas()
        self._ziureti_kur_begi()
        print("Begu")
    # Kaip sukurti metodą su skirtingu kiekiu argumentų:
    def miaukseti1(self, zinute = "miau", kiekis = 1):
        print(zinute*kiekis)
    
    def __str__(self):
        return f"Spalva: {self.spalva}, kojos: {self.kojos}"


# Objekto klasė duomenų nesaugo. 
# Ji yra lyg instrukcija, pagal kurią sukuriamas objektas 
# (kuris saugo objekto duomenis).
# init metodas (konstruktorius) yra automatiškai įvykdomas kuriant objektą.
# Jame gali būti inicijuojamos savybės (objekto kintamieji), 
# paleidžiami metodai (funkcijos) ir t. t.
# Objekto kintamieji vadinami savybėmis (Property), 
# o funkcijos – metodais (Methods)

# Kaip sukuriami objektai:
kate1 = Kate("pilka", 4)
kate2 = Kate("Juoda", 3)

print(kate1.spalva)
print(kate1.kojos)
kate1.miaukseti()
kate1.begti()

print(kate2.spalva, kate2.kojos)
kate2.kojos = 4
print(kate2.spalva, kate2.kojos)

kate3 = Kate("pilka", 4)
print(kate3.spalva, kate3.kojos)

#kate4 = Kate()
#print(kate4.spalva, kate4.kojos)

kate5 = Kate("Juoda", 4)
print(kate5.miaukseti())
print(kate5.miaukseti1("Mr", 5))
# print(kate5) # rodo klaida => <__main__.Kate object at 0x000001EBDE82B9D0>
print(kate5) # taip galima spausdinti/kviesti objekta, kai objekto klaseje sukuriame spausdinimo metoda _str_




# OP principai:


# 1. Inkapsuliacija (Encapsulation) – 
# vidiniai objekto (klasės) duomenys yra slepiami 
# ir pasiekiami tik metodais (savybėmis, funkcijomis). 
# Tai leidžia neprisirišti prie vidinės objekto struktūros, 
# jį nesunkiai pakeisti kitu arba pakeisti jo struktūrą, 
# nekeičiant pirminio kodo.

# 2. Abstrakcija (Abstraction) – galimybė naudotis objektais, 
# nesigilinant į tai, kaip jie veikia. 
# Supaprastina objektų naudojimą, 
# sumažina pakeitimų poveikį likusiams kodui.


