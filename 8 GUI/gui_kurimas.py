import imp
from tkinter import *

# langas = Tk()
# langas.geometry("250x200")
# langas.resizable(0,0)
# label = Label(langas, text="label tekstas")
# label.pack()
# langas.mainloop()


langas = Tk()
virsutinis = Frame(langas)
apatinis = Frame(langas)
mygtukas1 = Button(virsutinis, text="1 mygtukas")
mygtukas2 = Button(virsutinis, text="2 mygtukas")
mygtukas3 = Button(apatinis, text="3 mygtukas")
mygtukas4 = Button(apatinis, text="4 mygtukas")
virsutinis.pack()
apatinis.pack(side=BOTTOM)
mygtukas1.pack(side=LEFT)
mygtukas2.pack(side=LEFT)
mygtukas3.pack(side=LEFT)
mygtukas4.pack(side=LEFT)
langas.mainloop()