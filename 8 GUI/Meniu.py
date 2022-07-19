# Kaip sukurti meniu:

# from tkinter import *
# langas = Tk()

# meniu = Menu(langas)
# langas.config(menu=meniu)
# submeniu = Menu(meniu, tearoff = 0)

# meniu.add_cascade(label="Meniu", menu=submeniu)
# submeniu.add_command(label="Pirmas")
# submeniu.add_command(label="Antras")
# langas.mainloop()
from tkinter import *
langas = Tk()

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)

def antras():
    print("Antras!")

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Pirmas")
submeniu.add_command(label="Antras",command=antras)
langas.mainloop()

# Antras!