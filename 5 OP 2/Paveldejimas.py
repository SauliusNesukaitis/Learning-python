# Paveldėjimas

# Paveldėjimas (Inheritance) – galimybė apjungti panašių objektų funkcionalumą, naudojant tėvines klases. 
# Tai leidžia nekartoti panašaus ar to paties kodo. 
# Taip pat nekeičiant paties objekto kodo, papildyti arba keisti jo funkcionalumą.

# Paveldėjimas – esamo programinio kodo (klasių) panaudojimo forma, 
# kai esamas kodas papildomas naujais duomenimis (kintamaisiais, savybėmis) ir naujais veiksmais (metodais).
# Paveldimumas realizuojamas, išvedant naujas klases iš jau esamų klasių.
# Esama klasė vadinama bazine klase (super klase, tėvo klase).
# Nauja klasė, išvedama esamos pagrindu, vadinama išvestine klase (poklasiu, vaiko klase).
# Išvestinė klasė gali būti bazine tolimesnei klasei.

# Esminės savybės
# Paveldėjimas naudojamas, kai reikia sukurti naują klasę,
# kuri nedaug skiriasi nuo kitos, anksčiau sukurtos.
# Išvestinė klasė paveldi visas bazinės klasės savybes (kintamuosius) ir elgseną (metodus). 

# Klasių hierarchija
# Klasės, tarpusavyje susietos paveldimumu, sudaro klasių hierarchiją.
# Klasių hierarchijos viršuje yra abstraktesnės klasės, o einant žemyn klasės darosi konkretesnės.
# Klasės, esančios hierarchijos viduryje, yra kartu ir bazinės ir išvestinės.
# Dažnai išvestinės klasės turi "...yra tam tikros rūšies..." ryšį su bazine klase:
# Knyga yra tam tikros rūšies SpausdintasDokumentas,
# KnygaMinkstaisVirseliais yra tam tikros rūšies Knyga.

# Paveldėjimo nauda
# Klasių hierarchijos mechanizmas leidžia bendrąsias
# panašių klasių savybes ir funkcionalumą apjungti
# bazinėse klasėse, o išvestinėse klasėse palikti tik specifines. 
# Tai:
# palengvina uždavinio struktūrizavimą;
# leidžia sumažinti kodo pasikartojimą, sutaupyti atminties ir laiko sąnaudas.

# Papildomos sąvokos
# Tiesioginė bazinė klasė – tai klasė, iš kurios išreikštai išvestinė klasė paveldi.
# Netiesioginė bazinė klasė – tai klasė, iš kurios paveldima per klasių hierarchiją.
# Vienetinis paveldėjimas – tiesiogiai paveldima tik iš vienos klasės.
# Neišreikštas daugybinis paveldėjimas įmanomas, paveldint sąsajas.

# Paveldėjimo pavyzdžiai
# Gyvūnas – šuo, katinas, arklys.
# Paukštis – žvirblis, erelis, pingvinas.
# Forma – apskritimas, trikampis, stačiakampis.
# Paskola – paskolaAutomobiliui, paskolaButui.
# Tarnautojas – pagrindinis, valandinis, kviestinis.
# Sąskaita – einamoji, terminuota.

# Konstruktorių paveldimumas
# Išvestinė klasė nepaveldi bazinės klasės konstruktorių.
# Bazinės klasės konstruktorius visada įvykdomas, kai sukuriamas naujas išvestinės klasės objektas.

# Išvestinės klasės objekto sukūrimas
import this

class Gyvunas():
    def __init__(self, vardas, spalva):
        self.vardas = vardas
        self.spalva = spalva

    def begti(self):
        print("Begu")

class Kate(Gyvunas):
    def miaukseti(self):
        print("Miau")

class Suo(Gyvunas):
    def loti(self):
        print("Au")

vezlys = Gyvunas("Toto", "Rudas")
vezlys.begti()

# vezlys.miaukseti() # AttributeError: 'Gyvunas' object has no attribute 'miaukseti'
kate1 = Kate("Muza", "Pilka")
kate1.begti()
kate1.miaukseti()
#kate1.loti() #AttributeError: 'Kate' object has no attribute 'loti'

suo1 = Suo("Gile", "Sidabrine")
suo1.begti()
suo1.loti()
# suo1.miaukseti() # AttributeError: 'Suo' object has no attribute 'miaukseti'

#Nenurodžius, objekto konstravimo metu vykdomas numatytasis bazinės klasės konstruktorius (prisiminkite: tai konstruktorius be parametrų).
# Kai bazinėje klasėje nėra konstruktoriaus be parametrų, būtina nurodyti, kurį bazinės klasės konstruktorių vykdyti.
# Konstruktoriaus iškvietimo formatas:
# __init__ Išvestinės_klasės_konstruktorius(parametrai) : super().__init__(argumentai) - bazinės klasės konstruktorius
# Tai ypač svarbu, jei turim perduoti parametrą (-us) bazinės klasės konstruktoriui