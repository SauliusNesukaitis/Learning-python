# Kaip esant skirtingiems vartotojo veiksmams, paleisti skirtingas funkcijas:
from tkinter import *
langas = Tk()

def spausdinti(event):
    print("Paspaustas kairys pelės mygtukas!")

def spausdinti2(event):
    print("Paspaustas dešinys pelės mygtukas!")

def spausdinti3(event):
    print("Paspaustas ENTER!")

mygtukas = Button(langas, text="Spausdinti")
mygtukas.bind("<Button-1>", spausdinti)
mygtukas.bind("<Button-3>", spausdinti2)
langas.bind("<Return>", spausdinti3)
mygtukas.pack()

langas.mainloop()

# Paspaustas kairys pelės mygtukas!
# Paspaustas dešinys pelės mygtukas!
# Paspaustas ENTER!