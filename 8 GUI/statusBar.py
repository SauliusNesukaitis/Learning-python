# Statuso juostos (status bar) kūrimas:

# from tkinter import *
# langas = Tk()

# status = Label(langas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)
# langas.mainloop()

# Su mygtuku:


from tkinter import *
langas = Tk()

def daryti():
    status["text"] = "Dabar daro"

mygtukas = Button(langas, text="Daryti", command=daryti)
status = Label(langas, text="Nieko nedaro...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

mygtukas.pack()

langas.mainloop()