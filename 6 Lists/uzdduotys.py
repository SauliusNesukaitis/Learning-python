# 1 užduotis:
# Sukurti programą, kuri:
# Prie kiekvieno sakinio „The Zen of Python tekstu“ žodžio pridėtų šauktuką ir atspausdintų naują sakinį.
# Patarimai:
# Naudoti map (su lambda) arba comprehension, " ".join()

# x = "The Zen of Python tekstu"
# y = [i + "!" for i in x.split()]
# print(" ".join(y))

# naujas = map(lambda i: i + "!", x.split())
# print(" ".join(naujas))


# 2 užduotis:
# Sukurti programą, kuri:
# Sukurtų sąrašą iš skaičių nuo 0 iki 50
# Padaugintų visus sąrašo skaičius iš 10 ir atspausdintų
# Atrinktų iš sąrašo skaičius, kurie dalinasi iš 7 ir atspausdintų
# Pakeltų visus sąrašo skaičius kvadratu ir atspausdintų
# Su kvadratų sąrašu atliktų šiuos veiksmus: atspausdintų sumą, mažiausią ir didžiausią skaičių, vidurkį, medianą
# Surūšiuotų ir atspausdintų kvadratų sąrašą atbulai
# Patarimai:
# Naudoti map, filter arba comprehension, sum, min, max, mean, median, %
# from statistics import mean, median

# list1 = list(range(0,50))

# padauginta10 = [i * 10 for i in list1]
# dalinasi7 = [i for i in list1 if i % 7 == 0]
# kvadratu = [i ** 2 for i in list1]
# # kvadratu = map(lambda x: x ** 2, list1)
# # print(list(kvadratu))
# print(sum(kvadratu))
# print(min(kvadratu))
# print(max(kvadratu))
# print(mean(kvadratu))
# print(median(kvadratu))
# print(sorted(kvadratu, reverse=True))


# 3 užduotis:
# Duotas sąrašas: sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# Sukurti programą, kuri:
# Paskaičiuotų ir atspausdintų visų sąrašo skaičių sumą
# Sudėtų ir atspausdintų visus sąrašo žodžius
# Suskaičiuotų ir atspausdintų, kiek sąraše yra loginių (boolean) kintamųjų su True reikšme
# Patarimai:
# Naudoti filter arba comprehension, sum, " ".join()



# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

# suma = sum(i for i in sarasas if type(i) == int or type(i) == float)
# zodziai = [i for i in sarasas if type(i) == str]
# log = sum([type(x) is bool for x in sarasas])
# print(suma)
# print("".join(zodziai))
# print(log)

# 4 užduotis:
# Sukurti programą, kuri:
# Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# Klasėje būtų repr metodas, kuris atvaizduotų vardą ir amžių
# Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# Įdėti sukurtus Zmogus objektus į naują sąrašą
# Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą ir pagal amžių (ir atbulai)
# Patarimai:
# Naudoti sorted, attrgetter, reverse, funkciją repr
from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.amzius = amzius
        self.vardas = vardas

    def __repr__(self):
        return(f"({self.vardas}, {self.amzius})")

zmogus1 = Zmogus("Petras", 200)
zmogus2 = Zmogus("Saulius", 100)

list1 = [zmogus1, zmogus2]
surusiuotas = sorted(list1, key=attrgetter("vardas"))
surusiuotas = sorted(list1, key=attrgetter("amzius"), reverse=True)
print(surusiuotas)