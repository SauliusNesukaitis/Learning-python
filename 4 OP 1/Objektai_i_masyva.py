# Kaip objektus sudėti į masyvą ir iš jo išimti
class Kate:
    def __init__(self, spalva, veisle, amzius):
        self.spalva = spalva
        self.veisle = veisle
        self.amzius = amzius
  # Metodas:
    def miaukseti(self, miauksejimas="Miau", kartai=1):
        print(miauksejimas * kartai)

    def __str__(self):
        return f"Kates spalva: {self.spalva}, kates veisle: {self.veisle}, kates amzius: {self.amzius}"
    
    def __repr__(self):
        return f"Kates spalva: {self.spalva}, kates veisle: {self.veisle}, kates amzius: {self.amzius}"

    def Spausdinti_kates_duomenis(self):
        self._judinti_kojas()
        self._ziureti_kur_begi()
        print("Veikia metodas - Spausdinti kates duomenis")
        
kates = [] #kaciu diktas ar masyvas

#kate1 = Kate("Juoda", "laukine", 3)
#kate2 = Kate("Smeline", "Siamo", 4)
#kate3 = Kate("Pilka", "Rusu melinoji", 4)

#kates.append(kate1)
#kates.append(kate2)
#kates.append(kate3)

#for kate in kates:
    #print(kate.spalva, kate.veisle, kate.amzius)

#sum([kate.amzius for kate in kates]) tik amziaus sumai rasto is dikto masyvo


while True:
    pasirinkimas = int(input("Pasirinkite:\n1 - iveskite kate\n2 - perziureti visas kates \n3 - iseiti is programos \n"))
    if pasirinkimas == 1:
        spalva = input("Iveskite spalva: ")
        veisle = input("Iveskite veisle: ")
        amzius = input("Iveskite amziu: ")
        kate = Kate(spalva, veisle, amzius)
        kates.append(kate)
    if pasirinkimas == 2:
        print("Veikia")
        for kate in kates:
            print(kate)
    if pasirinkimas == 3:
        print("Viso gero")
        break


