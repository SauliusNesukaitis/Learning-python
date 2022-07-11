# 1 užduotis. Plytos ir namas.
# Gamykla gamina kelių skirtingų dydžių plytas. 
# Žinomas kiekvieno tipo plytų aukštis, plotis ir ilgis.
# Parašykite programą, kuri suskaičiuotų, kiek reikia kiekvieno tipo plytų, 
# norint išmūryti 4 vienodas namo sienas. 
# Langų ir durų nėra. 
# Sienos mūrijamos tik iš vieno tipo plytų.

#Programos kūrimo eiga:
# Sukuriama klasė vienos plytos duomenims saugoti.
# Pagrindiniame lauke skelbiami trys objektai, 
# skirti kiekvieno plytos tipo duomenims saugoti.
# Namo sienos ilgis, plotis ir aukštis perskaičiuojami plytomis. 
# Gauti skaičiai sudauginami. Gautas sienos tūris plytomis ir bus ieškomas plytų skaičius. 
# Visi rezultatai pateikiami sveikaisiais skaičiais. (int)
# Skaičiuojami kiekvieno tipo plytų kiekiai namo sienoms mūryti.
import this
import math
x = 5.1
print(math.ceil(x))

class Plyta:
    def __init__(self, aukstis, plotis, ilgis):
        self.aukstis = aukstis
        self.plotis = plotis
        self.ilgis = ilgis

    def __str__(self):
        return f"Turis: {self.aukstis*self.plotis*self.ilgis}"