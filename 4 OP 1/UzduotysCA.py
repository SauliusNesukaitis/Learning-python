# Uzduotis 1
# class Sakinys:
#     def __init__(self, tekstas="Zen of Python"):
#         self.tekstas = tekstas

#     def atbulai(self):
#         return self.tekstas[::-1]

#     def didziosiomis(self):
#         return self.tekstas.upper()

#     def mazosiomis(self):
#         return self.tekstas.lower()

#     def ieskoti(self, ieskomas):
#         return self.tekstas.count(ieskomas)

#     def pakeisti(self, senas, naujas):
#         return self.tekstas.replace(senas, naujas)

#     def atspausdintiZodi(self, skaicius):
#         suskirstytas = self.tekstas.split()
#         return suskirstytas[skaicius]

#     def info(self):
#         zodziu_kiekis = len(self.tekstas.split())
#         skaiciai = sum(i.isnumeric() for i in self.tekstas)
#         didziosios = sum(i.isupper() for i in self.tekstas)
#         mazosios = sum(i.islower() for i in self.tekstas)
#         print(
#             f"Zodziu kiekis: {zodziu_kiekis}, Skaiciai: {skaiciai}, Didziosios: {didziosios}, Mazosios: {mazosios}"
#         )

#     def __str__(self):
#         return ("Tekstas: " + self.tekstas)

# mano_sakinys = Sakinys("Mano tekstas yra toks")
# print(mano_sakinys.atbulai())
# print(mano_sakinys.mazosiomis())
# print(mano_sakinys.didziosiomis())
# print(mano_sakinys.ieskoti("a"))
# print(mano_sakinys.pakeisti("Mano", "Savo"))
# print(mano_sakinys.atspausdintiZodi(2))
# mano_sakinys.info()
# print(mano_sakinys)

# Uzduotis 2

# import datetime
# import calendar
# from this import d

# class Sukaktis:
#     def __init__(self, metai=2000, menuo=12, diena=12, valandos=12, minutes=12):
#         self.metai = metai
#         self.menuo = menuo
#         self.diena = diena
#         self.valandos = valandos
#         self.minutes = minutes
#         self.data = datetime.datetime(metai, menuo, diena, valandos, minutes)

#     def smulkiai(self):
#         now = datetime.datetime.now()
#         skirtumas = now - self.data
#         print(f"Praejo metu: ", skirtumas.days // 365)
#         print(f"Praejo menesiu: ", skirtumas.days // 365 * 12)
#         print(f"Praejo savaiciu: ", skirtumas.days / 7)
#         print(f"Praejo dienu: ", skirtumas.days)
#         print(f"Praejo valandu: ", skirtumas.total_seconds() / 3600)
#         print(f"Praejo minuciu: ", skirtumas.total_seconds() / 60)
#         print(f"Praejo sekundziu: ", skirtumas.total_seconds())

#     def arKeliamieji(self):
#         if calendar.isleap(self.metai):
#             print("Keliamieji metai")

#     def atimtiDienas(self, dienos):
#         return self.data - datetime.timedelta(days=dienos)

#     def pridetiDienas(self, dienos):
#         return self.data + datetime.timedelta(days=dienos)

#     def __str__(self):
#         return (
#             f"Data: {self.metai}-{self.menuo}-{self.diena} {self.valandos}:{self.minutes}")

    


# data1 = Sukaktis(2000, 1, 1, 12, 12)
# data1.arKeliamieji()
# data1.smulkiai()
# print(data1.atimtiDienas(5))
# print(data1.pridetiDienas(45))
# print(data1)