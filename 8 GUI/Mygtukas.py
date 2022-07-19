from tkinter import *
langas = Tk()

def spausdinti():
    print("Spausdina!")

mygtukas = Button(langas, text="Spausdinti", command=spausdinti)
mygtukas.pack()
langas.mainloop()

# Spausdina!