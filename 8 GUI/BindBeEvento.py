# Kaip per bind iškviesti funkciją be "event" argumento?

from tkinter import *
langas = Tk()

def spausdinti():
    print("Spausdina!")

mygtukas = Button(langas, text="Spausdinti", command=spausdinti)
langas.bind("<Return>", lambda event: spausdinti())
mygtukas.pack()

langas.mainloop()