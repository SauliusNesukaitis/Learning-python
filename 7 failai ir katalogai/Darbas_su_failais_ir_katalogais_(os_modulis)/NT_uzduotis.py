# 2_PAVELDEJIMAS_POLIMORFIZMAS. Nekilnojamojo turto agentūra. 
# Turite suvesti INPUT nekilnojamojo turto agentūrų duomenis (3 agentūros). 
# Pavadinimas, adresas, telefonas.
# Nekilnojamojo turto agentūra parduoda butus ir nuosavus namus. 
# Sukurkite klasę „RealEstate“ (savybės – miestas, mikrorajonas, gatvė, namo numeris, tipas, pastatymo metai, plotas, kambarių skaičius), 
# kurią paveldės klasės “Flat” (savybė - aukštas) ir “House” (savybė – šildymo būdas).
# Raskite, kurioje gatvėje dudžiausias namas ir daugiausiai kambarių turintis butas 
# (print išsivesti didžiausią ir daugiausia kambarių turintį objektą).
# Raskite seniausią nekilnojamojo turto objektą kiekvienoje klasėje atskirai, ekrane atspausdinkite visą jo informaciją.



from operator import indexOf


class Agenturos():
    def __init__(self, pavadinimas, adresas, telefono_numeris):
        self.pavadinimas = pavadinimas
        self.adresas = adresas
        self.telefono_numeris = telefono_numeris

    def __str__(self): 
        return f"pavadinimas: {self.pavadinimas}, adresas: {self.adresas}, telefono numeris {self.telefono_numeris}"

    def __repr__(self):
        return f"pavadinimas: {self.pavadinimas}, adresas: {self.adresas}, telefono numeris {self.telefono_numeris}"

agentura1 = Agenturos("Travel", "Klaipeda, Artoju g., 17", 867700000)
agentura2 = Agenturos("Norai", "Silute, Architektu g. 19", 867895462)
agentura3 = Agenturos("Keliones", "Vilnius, Pilies g. 45", 869878945)
print(agentura1, "\n", agentura2, "\n", agentura3)


class RealEstate():
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kambarių_skaicius):
        self.miestas = miestas
        self.mikrorajonas = mikrorajonas
        self.gatve = gatve
        self.namo_numeris = namo_numeris
        self.tipas = tipas
        self.pastatymo_metai = pastatymo_metai
        self.plotas = plotas
        self.kamnariu_skaicius = kambarių_skaicius

    def __str__(self): 
        return f"{self.miestas}, {self.mikrorajonas}, {self.gatve}, {self.tipas}, {self.pastatymo_metai}, {self.plotas}, {self.kamnariu_skaicius}"

    def __repr__(self):
        return f"{self.miestas}, {self.mikrorajonas}, {self.gatve}, {self.tipas}, {self.pastatymo_metai}, {self.plotas}, {self.kamnariu_skaicius}"

class Flat(RealEstate):
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kambarių_skaicius, aukstas):
        super().__init__(miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kambarių_skaicius)
        self.aukstas = aukstas

class House(RealEstate):
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kambarių_skaicius, sildymo_budas):
        super().__init__(miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kambarių_skaicius)
        self.sildymo_budas = sildymo_budas

    def __str__(self): 
        return f"{self.miestas}, {self.mikrorajonas}, {self.gatve}, {self.tipas}, {self.pastatymo_metai}, {self.plotas}, {self.kamnariu_skaicius}"

    def __repr__(self):
        return f"{self.miestas}, {self.mikrorajonas}, {self.gatve}, {self.tipas}, {self.pastatymo_metai}, {self.plotas}, {self.kamnariu_skaicius}"

# Raskite, kurioje gatvėje didžiausias namas ir daugiausiai kambarių turintis butas 
# (print išsivesti didžiausią ir daugiausia kambarių turintį objektą).
# Raskite seniausią nekilnojamojo turto objektą kiekvienoje klasėje atskirai, ekrane atspausdinkite visą jo informaciją.


butas1 = Flat("Klaipeda", "Mazasis kaimelis", "Paryziaus g.", 17, "daugiabutis", 1990, 89, 5, 4)
butas2 = Flat("Klaipeda", "Pajurio", "Giliu", 41, "daugiabutis", 2000, 60, 1, 3)
butas3 = Flat("Priekule", "Centrinis", "Zirgo", 7, "daugiabutis", 2011, 68, 4, 3)
butas4 = Flat("Klaipeda", "Pajurio", "Giliu", 39, "daugiabutis", 1969, 40, 2, 2)
butai = [butas1, butas2, butas3, butas4]

namas1 = House("Klaipeda", "Misko", "Volunges", 17, "murinis", 1990, 100, 5, "centrinis")
namas2 = House("Klaipeda", "Pajurio","Giliu", 45, "murinis", 2000, 85, 4, "autonominis")
namas3 = House("Palanga", "centrinis", "Basanaviciaus", 54, "naujos statybos", 2011, 56, 3, "centrinis")

namai = [namas1, namas2, namas3]

def didziausias_plotas(namai):
    max_namo_plotas=namai[0].plotas
    imax=0
    for namas in namai:
        if namas.plotas > max_namo_plotas:
            max_namo_plotas = namas.plotas
            imax = indexOf(namai, namas.plotas)     
        else:
            max_namo_plotas
            imax = indexOf(namai, namas.plotas) 
    print(F"Sioje gatveje: {namai[imax].gatve}, yra didziausio ploto namas : {max_namo_plotas}")




didziausias_plotas(namai)




#while True:
    #pasirinkimas = int(input("""
    #1: Didziausias namas,
    #2: Daugiausiai kambariu turintis butas,
    #3: Didziusias ir daugiausiai kambariu turintis objektas
    #4: seniausias NT objektas,  
    #5: Iseiti is programos.
    #"""))
   # if pasirinkimas == 1:
       # didziausias_namas = []
        #for dydis in namai:
        #    didziausias_namas.append(dydis.plotas)
        #    plotas = max(namai)
        #print("didziausias namas: ", max)

