# Kintamųjų naudojimas Tkinter programoje:
# Jei kuriant programą su Tkinter, prireiks funkcijose panaudoti kintamąjį, standartiniai kintamieji (pvz. kintamasis = "") nesuveiks. Todėl patartina naudoti StringVar, IntVar kintamuosius. Jie turi set() (reikšmės nustatymui) ir get() (kintamojo reikšmės gavimui) funkcijas. Atkreipkite dėmesį, kad jos gali būti kviečiamos tik funkcijose. Pvz:

# StringVar panaudojimo pavyzdys:


from tkinter import *

langas = Tk()

kintamasis = StringVar()
# kintamasis = ""

def funkcija():
    kintamasis.set("Naujas tekstas")
    print(kintamasis.get())

funkcija()