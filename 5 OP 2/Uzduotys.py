# 1 uzduotis

# from hashlib import new


# class Automobilis:
#     def __init__(self, metai, modelis, kuro_tipas):
#         self.metai = metai
#         self.modelis = modelis
#         self.kuro_tipas = kuro_tipas
#         self._informacija()

#     def vaziuoti(self):
#         print("Vaziuoja")

#     def stoveti(self):
#         print("Priparkuota")

#     def pildyti_degalu(self):
#         print("Degalai ipilti")

#     def _informacija(self):
#         print("Metai:", self.metai, "modelis:", self.modelis, "kuro tipas:", self.kuro_tipas)

# class Elektromobilis(Automobilis):
#     def pildyti_degalu(self):
#         print("Baterija ikrauta") 

#     def vaziuoti_autonomiskai(self):
#         print("Važiuoja autonomiškai")

# automobilis1 = Automobilis(2000, "modelis", "kuras")
# automobilis2 = Elektromobilis(1970, "modelis", "kuras")
# automobilis1.vaziuoti()
# automobilis1.stoveti()
# automobilis1.pildyti_degalu()
# automobilis2.vaziuoti()
# automobilis2.pildyti_degalu()
# automobilis2.vaziuoti_autonomiskai()

# 2 uzduotis
# import datetime

# class Darbuotojas:
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         self.vardas = vardas
#         self.valandos_ikainis = valandos_ikainis
#         self.dirba_nuo = dirba_nuo
    
#     def _dirbtos_dienos(self):
#         nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y, %m, %d, %H, %M, %S")
#         dabar = datetime.datetime.today()
#         skirtumas = dabar - nuo_kada_dirba
#         return skirtumas.days * 8

#     def paskaiciuoti_atlyginima(self):
#         atlyginimas = self.valandos_ikainis * self._dirbtos_dienos()
#         print(self.vardas + " " + str(atlyginimas))

# class NormalusDarbuotojas(Darbuotojas):
#     def _dirbtos_dienos(self):
#         nuo_kada_dirba = datetime.datetime.strptime(self.dirba_nuo, "%Y, %m, %d, %H, %M, %S")
#         dabar = datetime.datetime.today()
#         skirtumas = dabar - nuo_kada_dirba
#         return (skirtumas.days * 8) / 7 * 5

# darbuotojas1 = Darbuotojas("Vardas", 4.88, "2022, 06, 01, 12, 00, 00")
# darbuotojas2 = NormalusDarbuotojas("Vardas", 4.88, "2022, 06, 01, 12, 00, 00")
# darbuotojas1.paskaiciuoti_atlyginima()
# darbuotojas2.paskaiciuoti_atlyginima()

# 3 uzduotis

class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

class Biudzetas():
    def __init__(self):
        self.zurnalas = []

    def ivesti_pajamas(self, suma, siuntejas, papildoma_informacija):
        pajamu_irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamu_irasas)

    def ivesti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidu_irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidu_irasas)

    def gauti_biudzeto_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                balansas -= irasas.suma
        return balansas

    def gauti_ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos: {irasas.suma} {irasas.siuntejas} {irasas.papildoma_info}")
            if isinstance(irasas, IslaiduIrasas):
                print(f"Išlaidos: {irasas.suma} {irasas.atsiskaitymo_budas} {irasas.isigyta_preke_paslauga}")

mano_biudzetas = Biudzetas()

while True:
    print("Pasirinkite veiksmą: ")
    print("1 - Įvesti pajamas")
    print("2 - Įvesti išlaidas")
    print("3 - Gauti balansą")
    print("4 - Gauti ataskaitą")
    print("0 - Išeiti iš programos")
    pasirinkimas = input()
    if pasirinkimas == "1":
        print("Įveskite pajamas: ")
        suma = int(input("Suma: "))
        siuntejas = input("Siuntėjas: ")
        papildoma_informacija = input("Papildoma informacija: ")
        mano_biudzetas.ivesti_pajamas(suma, siuntejas, papildoma_informacija)
        print("Pajamos įvestos sėkmingai!")
    if pasirinkimas == "2":
        print("Įveskite išlaidas: ")
        suma = int(input("Suma: "))
        atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
        isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
        mano_biudzetas.ivesti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        print("Išlaidos įvestos sėkmingai!")
    if pasirinkimas == "3":
        print(f"Sąskaitos balansas: {mano_biudzetas.gauti_biudzeto_balansa()}")
    if pasirinkimas == "4":
        mano_biudzetas.gauti_ataskaita()
    if pasirinkimas == "0":
        break