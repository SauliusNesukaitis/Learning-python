# 2_PAVELDEJIMAS_POLIMORFIZMAS. Nekilnojamojo turto agentūra. 
# Turite suvesti INPUT nekilnojamojo turto agentūrų duomenis (3 agentūros). 
# Pavadinimas, adresas, telefonas.
# Nekilnojamojo turto agentūra parduoda butus ir nuosavus namus. 
# Sukurkite klasę „RealEstate“ (savybės – miestas, mikrorajonas, gatvė, namo numeris, tipas, pastatymo metai, plotas, kambarių skaičius), 
# kurią paveldės klasės “Flat” (savybė - aukštas) ir “House” (savybė – šildymo būdas).
# *Raskite, kurioje gatvėje dudžiausias namas ir daugiausiai kambarių turintis butas (print išsivesti didžiausią ir daugiausia kambarių turintį objektą).
# *Raskite seniausią nekilnojamojo turto objektą kiekvienoje klasėje atskirai, ekrane atspausdinkite visą jo informaciją.




class Agentura():
    def __init__(self, pavadinimas, adresas, telefonas):
        self.pavadinimas = pavadinimas
        self.adresas = adresas
        self.telefonas = telefonas

    def __str__(self):
        return f"Agenturos PAVADINIMAS: {self.pavadinimas} AGENTUROS ADRESAS: {self.adresas} AGENTUROS TELEFONAS: {self.telefonas}"


class RealEstate():
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris, 
                tipas, pastatymo_metai, plotas, kambariu_skaičius):
        self.miestas = miestas
        self.mikrorajonas = mikrorajonas
        self.gatve = gatve
        self.namo_numeris = namo_numeris
        self.tipas = tipas
        self.pastatymo_metai = pastatymo_metai
        self.plotas = plotas
        self.kambariu_skaičius = kambariu_skaičius

    def _pastatymo_metu_masyvas(self):
        seniausias1 = []
        for n in seniausias1:
            seniausias1.append(self.pastatymo_metai)
        return seniausias1
    
    def seniausias_objektas(_pastatymo_metu_masyvas):
        seniausiasi_metai = self._pastatymo_metu_masyvas[0]
        for metai in self._pastatymo_metu_masyvas:
            if metai > seniausiasi_metai:
                metai = seniausiasi_metai
                return seniausiasi_metai
            else:
                return seniausiasi_metai

        if self.pastatymo_metai == seniausiasi_metai:
            print(f"Seniausias objektas {self.gatve}, jo pastatymo metai {self.pastatymo_metai}")

class Flat(RealEstate):
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris,
                tipas, pastatymo_metai, plotas, kambariu_skaičius, aukstas):
        super().__init__(miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kambariu_skaičius)
        self.aukstas =  aukstas

    
class House(RealEstate):
    def __init__(self, miestas, mikrorajonas, gatve, namo_numeris,
                tipas, pastatymo_metai, plotas, kambariu_skaičius, sildymo_budas):
        super().__init__(miestas, mikrorajonas, gatve, namo_numeris, tipas, pastatymo_metai, plotas, kambariu_skaičius)
        self.sildymo_budas = sildymo_budas



buto_objektas = []

irasas = Flat("Panevezys", "klaipedos", "Statybininku g.", 7, "Blokinis", 1972, 44.6, 2, 2)
irasas1 = Flat("Panevezys", "Klaipedos", "Statybininku g.", 20, 'Blokinis', 1975, 35.83, 1, 3)
irasas2 = Flat("Panevezys", "klaipedos", "Parko g.", 7, 'Blokinis', 1970, 47.71, 3, 2)
irasas3 = Flat("Panevezys", "klaipedos", "Klaipedos g.", 140, 'Blokinis', 1984, 82, 4, 1)
irasas4 = Flat("Panevezys", "klaipedos", "Parko g.", 45, "Murinis", 1982, 69.03, 3, 1)
buto_objektas.append(irasas)
buto_objektas.append(irasas1)
buto_objektas.append(irasas2)
buto_objektas.append(irasas3)
buto_objektas.append(irasas4)

namo_objektas = []

irasas5 = House("Panevezys", "Rozes", "Saules al.", 75, "Murinis", 1993, 391, 8, "Kita")
irasas6 = House("Panevezys", "Rozes", "Menulio g.", 13, "Murinis", 2010, 130, 4, "Dujini - kietu kuru")
irasas7 = House("Panevezys", "Rozes", "Roziu g.", 23, "Murinis", 1982, 198.02, 4, "Dujini - kietu kuru")
irasas8 = House("Panevezys", "Rozes", "Vyturio g.", 10, "Murinis", 1994, 256, 5, "Dujini - kietu kuru")
irasas9 = House("Panevezys", "Rozes", "Aguonu g.", 102, "Murinis", 1998, 343.22, 5, "Dujini")
namo_objektas.append(irasas5)
namo_objektas.append(irasas6)
namo_objektas.append(irasas7)
namo_objektas.append(irasas8)
namo_objektas.append(irasas9)

        #7
#House.didziausias_namas(namo_objektas)
#Flat.daugiausia_kambariu_Flat(buto_objektas)

#8
RealEstate.seniausias_objektas(namo_objektas)



# agenturos_duomenis = []

# while True:
#     pasirinkimas = input(""" MENIU 
#     1. Ivesti agenturos duomenis: 
#     2. Atspauzdinti agenturos duomenis:
#     3. Ivesti NAMO duomenis: 
#     4. Ivesti BUTO duomenis: 
#     5. Atspauzdinti parduodamus NAMUS: 
#     6. Atspauzdinti parduodamus BUTUS: 
#     7. Atspauzdinti gatve kur didžiausias namas(plotas) ir daugiausiai kambarių turintis butas:
#     8. Atspauzdinti seniausią nekilnojamojo turto objektą:  
#     9. Iseiti""")
#     if pasirinkimas == "1":
#         agenturos_duomenis.append(input("Ivesti PAVADINIMAS: ADRESAS: TELEFONAS:\n"))
#     if pasirinkimas == "2":
#         print(agenturos_duomenis)
#     if pasirinkimas == "3":
#         namas = input("""Ivesti MIESTAS: MIKRORAJONAS: GATVE: NAMO NUMERIS: TIPAS: PASTATYMO METAI: KVADRATURA: KAMBARIU SKAICIUS: AUKSTAS:\n""")
#         namo_objektas.append(namas)
#     if pasirinkimas == "4":
#         butas = input("""Ivesti MIESTAS: MIKRORAJONAS: GATVE: NAMO NUMERIS: TIPAS: PASTATYMO METAI: 
#                     KVADRATURA: KAMBARIU SKAICIUS: SILDYMO BUDAS:""")
#     if pasirinkimas == "5":
#         print(namo_objektas)
#     if pasirinkimas == "7":
#         print(Flat.daugiausia_kambariu_Flat(buto_objektas))
#         print(House.daugiausia_kambariu(namo_objektas))
#     if pasirinkimas == "8":
#         RealEstate.seniausias_objektas(namo_objektas)
#     if pasirinkimas == "9":
#         break
    
 

