# Veiksmai su matricos elementais, eilutėmis ir stulpeliais
# Kaip sąrašus, taip ir matricos elementus galime pasiekti naudodami indeksą.

import numpy as klase

A = klase.array([[-12, 0, 23], [7, 3, -2], [0.1, 0.2, 0.3]])
print('A matrica \n', A)
print('A matricos trecia eilute \n', A[2])
print('A antra eilute nuo galo \n', A[-2])
print('A matricos antros eilutes trecio stulpelio elementas: ', A[1][2])

#Turint vienmatį masyvą, elementai skaičiuojami tik vienu parametru - eilute
B = klase.array([-12, 0, 23, 7, 3, -2, 0.1, 0.2, 0.3])
print(B[5])

C = klase.array([[-12, 0, 23], [7, 3, -2], [0.1, 0.2, 0.3]])
print('C matrica\n', C)
#Atspausdinti pirmą visą stulpelį:
print('\nPirmas stulpelis: ', C[:,0]) #C[eilute,stulpelis]
#Atspausdinti pirmą visą eilutę:
print('Pirma eilute: ', C[0,:]) # : - VISKA
#Atspausdinti paskutinę eilutę:
print('Paskutine eilute: ', C[-1,:])
#Atspausdinti paskutinį stulpelį:
print('Paskutinis stulpelis: ', C[:,-1])
#Atspausdinti visų eilučių, 2-3 stulpelius
print('Visu eiluciu, 2-3 stulpelis\n', C[:,[1,2]])
#Atspausdinti visų stulpelių, 2-3 eilutes
print('visu stulpeliu, 2-3 eilutes\n', C[[1,2],:])
#Atspausdinti nuo antros iki paskutines eilutes, nuo pirmo iki trecio stulpelio
print('Nuo antros iki paskutines eilutes, nuo pirmo iki antro stulpeliai\n', C[1:,:2])
#Atspausdinti nuo antros iki paskutines eilutes, nuo antro iki trecio stulpelio
#print('Nuo antros iki paskutines eilutes, nuo antro iki trecio stulpeliai\n', C[1:],[2:3]]) KLAIDA

#SANTRAUKA
# Sąrašai – tai tarpusavy nesusietų kintamųjų rinkinys. 
# Ribota veiksmų laisvė tiek dėl Python bibliotekos, tiek dėl duomenų panaudojimo
# Norint susieti duomenis, naudojamos matricos ir masyvai
# Skirtumas nuo sąrašų – eilučių/stulpelių skaičius turi būti vienodas
# Sąrašai labiausiai tinka duomenų kaupimui, matricos – duomenų apdorojimui
# Viena labiausiai naudojamų išorinių bibliotekų veiksmams su matricomis ir masyvais – NumPy. 
# Labiausiai taikoma elektronikoje ir finansuose.

