from tkinter import *

langas = Tk()
langas.title("Pavadinimas")
langas.geometry("400x400")
langas.config(bg="#551144")

def parodo_pazymeta_sali():
    pasirinkta = boksas.get(boksas.curselection()[0])
    tekstas.set(pasirinkta)


boksas = Listbox(langas, selectmode=SINGLE)
boksas.pack()

tekstas = StringVar()

boksas.insert(0, "Islandija")
boksas.insert(1, "Vakietija")
boksas.insert(2, "Belarusija")
boksas.insert(3, "Australija")

uzrasas = Label(langas, textvariable = tekstas)
uzrasas.pack()
Button(langas, text="Rodyti pazymeta", command=parodo_pazymeta_sali).pack()

langas.mainloop()