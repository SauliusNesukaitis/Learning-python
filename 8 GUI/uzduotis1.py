# 1. Sukurti mini GUI su eventu ir peles mygtuku paspaudimais.

# 1.1  sukurit dvi funkcijas def, su print. Pirmoji informuoja apie viena peles paspaudima.

# Antroji uzdaro langa ir informuoja apie dviguba peles paspaudima.

# Su bind

from tkinter import *
import sys

langas = Tk()

def vienas_paspaudimas(event):
    print("Paspaudete keiri peles mygtuka viena karta")

def du_paspaudimai(event):
    print("Paspaudete keiri peles mygtuka du kartus")
    sys.exit()

mygtukas = Button(langas, text="Peles paspaudimai")
mygtukas.bind("<Button-1>", vienas_paspaudimas)
mygtukas.bind("<Double-1>", du_paspaudimai)
mygtukas.pack()

langas.mainloop()