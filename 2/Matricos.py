import numpy as np

# Matrica yra dvimatė duomenų struktūra, kurioje skaičiai yra išdėstyti į eilutes ir stulpelius.
# „Python“ neturi funkcijos tipo matricoms. 
# Tačiau sąrašo sąrašą galime traktuoti kaip matricą. Pavyzdžiui:
# A = [[1, 4, 5], 
#     [-5, 8, 9]]

# print(A)
# print(type(A))

# Naudojant sąrašus kaip matricą, atliekamos paprastos skaičiavimo užduotys,
# tačiau sudėtingesniems skaičiavimams atlikti patogiau dirbti su „Python“
# matricomis naudojant „NumPy“ paketą.
# NumPy pateikia daugiamatį skaičių masyvą (kuris iš tikrųjų yra objektas). 
# Paimkime pavyzdį:


# a = np.array([1, 2, 3])
# print(a)
# print(type(a)) # NumPy masyvo klasė vadinama ndarray

# Matrica su „NumPy“
import numpy as klase
# matrica_A = klase.array([[2, 3, -9],[2, 3, 5]])
# print(matrica_A)

# matrica_B = klase.array([[9.5, -3.4, 12.78],['k', 's', 'm']]) #matricoje galima saugoti skirtingų tipų duomenis
# print(matrica_B)

#matrica_C = klase.array([[2, 4, 5],[0, 3]]) #pagrindinis reikalavimas - išlaikyti vienodą eilučių/stulpelių skaičių

# Matricų sudėtis - dvimačių masyvų
# Veiksmai tarp kelių matricų galimi tik tada, kai matricos eilučių ir stulpelių skaičius sutampa. 
# Taip pat, kai jų tipai sutampa.

# matrica_A1 = klase.array([[-12, 15, 7],[0, 9, 7]])
# matrica_B1 = klase.array([[-7, 5, 0],[-9, 2, 10]])
# print('matrica_A1: \n', matrica_A1)
# print('matrica_B1: \n', matrica_B1)
# print('Matricu sudetis: \n', matrica_A1 + matrica_B1)
# matrica_C1 = klase.array([[7, 3],[0, 12]])
# print(matrica_A1+matrica_C1) #matricų dydis skirtingas

# Palyginimui. Jei matrica_A1 ir matrica_C1 kursime ne kaip matricas, 
# o kaip sąrašus, sudedami bus ne jų elementai, o tiesiog apjungiami sąrašai.
# matrica_A1 = [[-12, 15, 7],[0, 9, 7]]
# matrica_C1 = [[7, 3],[0, 12]]
# print(matrica_A1 + matrica_C1)

# Matricų dauginimas
# Svarbiausia sąlyga dauginant matricas – eilučių skaičius turi atitikti kitos matricos stulpelių skaičių
# Norėdami sudauginti dvi matricas, naudojame dot() metodą.

# M = klase.array([[-1,2],[2,2]])
# print('Matrica M \n', M)
# N = klase.array([[0,-3],[4,2]])
# print('Matrica N \n', N)
# print('Matricu daugyba \n', M.dot(N))

# Matricų transponavimas
# Matricų transponavimui naudosime numpy.transpose

D = klase.array([[1, 1],[2, 1],[3, -3]])
print('pries trasponavima matrica D \n', D)

print('po trasponavimo matrica D \n', D.transpose())