# Kaip sukurti atvaizduojamą sąrašą:

# from tkinter import *

# langas = Tk()
# boksas = Listbox(langas)
# sarasas = range(1, 200)
# boksas.insert(END, *sarasas)
# boksas.pack(side=LEFT)
# langas.mainloop()

# Kaip pridėti sąrašo slinkimo juostą:

# from tkinter import *
# langas = Tk()
# masyvas = range(1, 200)
# scrollbaras = Scrollbar(langas)
# boksas = Listbox(langas,
# yscrollcommand=scrollbaras.set)
# scrollbaras.config(command=boksas.yview)
# boksas.insert(END, *masyvas)
# scrollbaras.pack(side=RIGHT, fill=Y)
# boksas.pack(side=LEFT)
# langas.mainloop()

# Kaip pasiimti duomenis iš pažymėtos sąrašo vietos:


from tkinter import *

langas = Tk()
sarasas = range(1, 200)

def spausdinti():
    pasirinkta = sarasas[boksas.curselection()[0]]
    uzrasas["text"] = pasirinkta

mygtukas = Button(langas, text="Spausdinti",
command=spausdinti)

uzrasas = Label(langas, text="Nieko")
boksas = Listbox(langas, selectmode=SINGLE)
boksas.insert(END, *sarasas)
boksas.pack(side=LEFT)
mygtukas.pack()
uzrasas.pack()
langas.mainloop()