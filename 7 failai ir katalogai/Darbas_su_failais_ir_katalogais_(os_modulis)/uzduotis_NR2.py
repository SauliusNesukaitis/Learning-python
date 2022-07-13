
# 2_PAVELDEJIMAS_POLIMORFIZMAS. Nekilnojamojo turto agentūra. 
# Turite suvesti INPUT nekilnojamojo turto agentūrų duomenis (3 agentūros). 
# Pavadinimas, adresas, telefonas.
# Nekilnojamojo turto agentūra parduoda butus ir nuosavus namus. 
# Sukurkite klasę „RealEstate“ (savybės – miestas, mikrorajonas, gatvė, namo numeris, tipas, pastatymo metai, plotas, kambarių skaičius), 
# kurią paveldės klasės “Flat” (savybė - aukštas) ir “House” (savybė – šildymo būdas).
# *Raskite, kurioje gatvėje dudžiausias namas ir daugiausiai kambarių turintis butas (print išsivesti didžiausią ir daugiausia kambarių turintį objektą).
# *Raskite seniausią nekilnojamojo turto objektą kiekvienoje klasėje atskirai, ekrane atspausdinkite visą jo informaciją.


class Agenturos:
    def __init__(self, pavadinimas, adresas, telefonas):
        self.pavadinimas = pavadinimas
        self.adresas = adresas
        self.telefonas = telefonas

    def __str__(self):
        return f"Agenturos pavadinimas:{self.pavadinimas}, adresas:{self.adresas}, telefonas:{self.telefonas}"

    def __repr__(self):
        return f"Agenturos pavadinimas:{self.pavadinimas}, adresas:{self.adresas}, telefonas:{self.telefonas}"

agenturu_ivedimas = []

while True:
    meniu = int(input("""Pasirinkite
    1 iveskite pavadinima-adresa-telefona
    2 iveskite ???
    3 iveskite ???
    0 iseikite is programos
    Pasirinkite:
    """))
    if meniu == 1:
        pavadinimas = input("Iveskite Agenturos pavadinima: ")
        adresas = input("Iveskite Agenturos adresa: ")
        telefonas = input("Iveskite Agenturos telefona: ")
        agentura = Agenturos(pavadinimas, adresas, telefonas)
        agenturu_ivedimas.append(agentura)
    if meniu == 2:
        print("Dar neapibreztas punktas ka ivedinesime ")
        # for agentura in agenturu_ivedimas:
    if meniu == 3:
        print("Dar neapibreztas punktas ka ivedinesime ")
    if meniu == 0:
        print("Viso gero! Programa uzdatyra.")
        break

class RealEstate:
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris, tipas , pastatymo_metai, plotas, kmabarius_skaicius):
        self.miestas = miestas
        self.mikrorajonas = mikrorajonas
        self.gatve = gatve
        self.namo_numeris = namo_numeris
        self.tipas = tipas
        self.pastatymo_metai = pastatymo_metai
        self.plotas =  plotas
        self.kambariu_skaicius = kmabarius_skaicius

    def __str__(self):
        return f"Pastato savybes:{self.miestas}, {self.mikrorajonas}, {self.gatve}, {self.namo_numeris}, {self.tipas}, {self.pastatymo_metai}, {self.plotas}, {self.kambariu_skaicius}"

butas1 = RealEstate("Vilnius", "N.Vilnia", "Darzelio", 1, "Daugiabutis", 1950, 44, 2)
butas2 = RealEstate("Vilnius", "N.Vilnia", "Darzelio", 3, "Daugiabutis", 1960, 56, 3)
butas3 = RealEstate("Vilnius", "N.Vilnia", "Parko", 5, "Daugiabutis", 1980, 65, 4)
butas4 = RealEstate("Vilnius", "N.Vilnia", "Geroves", 3, "Daugiabutis", 1975, 35, 2)
namas1 = RealEstate("Pabrade","Neturi pavadinimo", "Bajoreliu", 2, "Namas", 1982, 135, 4)
namas2 = RealEstate("Pabrade","Neturi pavadinimo", "Kalno", 4, "Namas", 1983, 140, 4)
pastatai = [butas1, butas2, butas3, butas4, namas1, namas2]
butai = [butas1, butas2, butas3, butas4]
namai = [namas1, namas2]
def didziuaisas_plotas():
    ploto_masyvas = []
    for d_plotas in pastatai:
        ploto_masyvas.append(d_plotas.plotas)
        didziausias = max(ploto_masyvas)
    # max_plot = ploto_masyvas[0]
    # for skaicius in range(0, len(ploto_masyvas), 1):
    #     if max_plot < ploto_masyvas[skaicius]:
    #         max_plot = ploto_masyvas[skaicius]
    # print(max_plot)

    # for namas in namai:
    #     if max_plot == namas.plotas:
    #         print(namas)
    for namas in pastatai:
        if didziausias == namas.plotas:
            print(f"Didziausiasi namas randasi: {namas.gatve} gatveje.")

didziuaisas_plotas()

def butas_dougiausia_kamb():
    kamb_masyvas = [] 
    for kambariai in butai:
        kamb_masyvas.append(kambariai.kambariu_skaicius)
        dougiausia_kamb = max(kamb_masyvas)
    print(f"Didziausias butas turi {dougiausia_kamb} kambarius.")

butas_dougiausia_kamb()

def seniausi_pastatai():
    amzius_butai = []
    for amzius in butai:
        amzius_butai.append(amzius.pastatymo_metai)
        sen_butas = min(amzius_butai)
        
    for amzius in butai:
        if sen_butas == amzius.pastatymo_metai:
            print(f"Seniausias butas pastatytas {sen_butas} metais.")

# def seniausias_namas():
    amzius_namai = []
    for amzius in namai:
        amzius_namai.append(amzius.pastatymo_metai)
        sen_namas = min(amzius_namai)
        
    for amzius in namai:
        if sen_namas == amzius.pastatymo_metai:
            print(f"Seniausias namas pastatytas {sen_namas} metais.")

seniausi_pastatai()

class Flat(RealEstate):
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kmabarius_skaicius, aukstas):
        super().__init__(miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kmabarius_skaicius)
        self.aukstas = aukstas


class House(RealEstate):
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kmabarius_skaicius, sildymo_budas):
        super().__init__(miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kmabarius_skaicius)
        self.sildymo_budas = sildymo_budas








