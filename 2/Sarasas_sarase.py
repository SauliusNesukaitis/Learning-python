# # Sąrašas yra tam tikras „kratinys“ duomenų, kurie nėra vienas su kitu susiję nei tipu, nei priklausomybe
# # Sąrašas gali būti sąraše. 
# # Skirtingai nei matricoje, čia nėra reikalavimų išlaikyti griežtą eilučių ar stulpelių tvarką.
# # Bendra struktūra: sar=[[1_eilutės elementai],[2 eilutės elementai]]

# sarasai_sarase = [[5, 1, 2], [2, 4], ['Jonas', 'Andrius'], [-7.59, -7, 0, 2.5]]
# #                     0         1             2                   3
# for sarasas in sarasai_sarase:
#     print(sarasas)
# print('NAUJA UZDUOTIS')
# # Sąrašas turi eilutes ir stulpelius. 
# # Elementus jame galima nurodyti eilutės ir stulpelio numeriu.
# print('Elementu isrinkimas is saraso')
# print('Noriu issirinkti -7.59')
# print(sarasai_sarase[3][0]) #[3] - eilutes indeksas, [0] - stulpelio indeksas
# print('Noriu issirinkti Andrius')
# print(sarasai_sarase[2][1])
# print('Neteisingai')
# #print(sarasai_sarase[2][5])

# # Masyvo papildymas naujais elementais
# # Yra trys pagrindiniai sąrašo pildymo metodai:
# # - append
# # - extend
# # - insert
# # - aritmetinis sąrašo papildymas

# # Append ir Extend yra lygiaverčiai.
# # Galima naudoti tiek vieną, tiek kitą. 
# # Elementus prideda iš sąrašo galo. 
# # Taip pat galima pridėti atskirą sąrašą. Elementai gali būti bet kokio tipo.

# # Insert funkcija leidžia sąrašą papildyti bet kurioje pozicijoje 
# # Norėdami pridėti elementą į masyvą, naudojamas metodas append(), extend() arba +[sąrašas].

# # sarasas_1 = [9, 0, -7]
# # sarasas_2 = ['-7', '4', 'd']
# # print('Pradinis sarasas_1: ', sarasas_1)
# # print('Pradinis sarasas_2: ', sarasas_2)
# # sarasas_3 = sarasas_1 + ['as', 'esu', 'Gintare']
# # print('Naujas sarasas_3: ', sarasas_3)
# # print('Saraso_3 ilgis: ', len(sarasas_3))
# # print('Sarasai_sarase ilgis: ', len(sarasai_sarase))
# # sarasas_1.extend(sarasas_2)
# # print('Sarasas_1 extend sarasas_2 rezultatas: ', sarasas_1)
# # print('Saraso_1 naujas ilgis: ', len(sarasas_1))
# # sarasas_2.append('7896')
# # print('Naujas sarasas_2', sarasas_2)

# # Norint įtraukti naują sąrašą, naudojama append() funkcija
# # PVZ:
# # masyvas_A = [-8, 5, 6]
# # masyvas_A.append(['Gintare', 'Lauciene'])
# # print('Naujas masyvas', masyvas_A)
# # print('Mayvo_A elementu skaicius: ', len(masyvas_A))
# # masyvas_A.extend([-0.99, 0])
# # print('Naujas masyvas: ', masyvas_A)
# # print('Mayvo_A elementu skaicius: ', len(masyvas_A))

# # Kaip pastebėjote, extend() funkcija sąrašo elementus tiesiog prideda. 
# # Append() funkcija prideda kaip atskirą sąrašą.
# # print('===============================================================')
# # print('Funkcija insert():')
# # #Norint įtraukti elementą į bet kurią sąrašo poziciją, naudojama funkcija insert()
# # masyvas_B0 = [-5, 6, 9, 2, 4]
# # masyvas_B1 = ['RRR','KKK', 'SSS', 'VVV']
# # masyvas_B2 = [-20, -30, -70]

# # masyvas_B0.insert(2, 0.99)
# # print(masyvas_B0)

# # masyvas_B0.insert(-2, masyvas_B2) # su pozicija "-" pire indekso (-2) skaičiuojasi nuo galo
# # print(masyvas_B0)

# # masyvas_B0[1:1] = masyvas_B1 #prieš skliaustus nurodžius "įpjovos" (slice) pozociją, įtraukia elementus, o ne sąrašą
# # print(masyvas_B0)

# # masyvas_B0[1::3] = masyvas_B1
# # print(masyvas_B0)

# # Masyvo elementų pašalinimas
# # Norėdami pašalinti elementą iš masyvo, galite naudoti metodą kelis metodus. 
# # Vienas iš jų yra pop ().

# # Jeigu norime ištrinti antrąjį mėnesių masyvo elementą:
# # menesiai = ["Sausis", "Vasaris", "Kovas", "Balandis", "Geguze"]
# # print(menesiai)
# # menesiai.pop(1) # pop(index) trina pagal indeksa
# # print(menesiai)

# # Kitas metodas kurį galima naudoti norint pašalinti elementą iš masyvo yra - remove().
# # Pavyzdžiui ištrinkime elementą, kurio reikšmė „Geguze“:
# # menesiai.remove("Geguze") # remove(value) trina pagal reiksme 
# # print(menesiai) 

# # Masyvo metodai
# # append() Prideda elementą sąrašo/masyvo gale
# # clear() Pašalina visus elementus iš sąrašo/masyvo
# # copy() Gražina sąrašo/masyvo kopiją
# # count() Gražina nurodytos vertės elementų skaičių
# # extend() Įtraukia sąrašo/masyvo elementus
# # index() Gražina pirmojo elemento indeksą su nurodyta verte
# # insert() Prideda elementą nurodytoje vietoje
# # pop() Pašalina elementą nurodytoje vietoje
# # remove() Pašalina pirmąjį elementą su nurodyta verte
# # reverse() Pakeičia sąrašo/masyvo tvarką(iš galo į priekį)
# # sort() Rūšiuoja sąrašą/masyvą
# # type() nurodo tipą 


# #Masyvu kurimas
# # skaiciu_masyvas = [-12, 6, 9, -0.99, 15, -0.99, -0.99, -19] # pirmas masyvas
# # print('skaiciu masyvo ilgis', len(skaiciu_masyvas))
# # zodziu_masyvas_0 = ["Labas", "Rytas"] # antras masyvas
# # print('skaiciu masyvo ilgis', len(zodziu_masyvas_0))
# # zodziu_masyvas_1 = ["naujas", "pridetas", "elementas", "Naujas", "Pridetas", "Elementas"] # trecias masyvas

# # print('isbandome metodus')

# # reverse() Pakeičia sąrašo/masyvo tvarką(iš galo į priekį)
# print(skaiciu_masyvas)
# print('Skaiciu masyvas po reverse()')
# skaiciu_masyvas.reverse()
# print(skaiciu_masyvas)
# print('==================================')

# # sort() Rūšiuoja sąrašą/masyvą
# print('skaiciu masyvas')
# print(skaiciu_masyvas)
# skaiciu_masyvas.sort()
# print('Skaiciu masyvas po sort() rikiuoja nuo maziausios iki didziausios') # rikiuoja nuo maziausios iki didziausios reiksmes
# print(skaiciu_masyvas)
# print('Skaiciu masyvui pritaikius sort() reikia pritaikyti reverse() norint rikiuoti nuo didziausios iki maziausios')
# skaiciu_masyvas.reverse()
# print(skaiciu_masyvas)

# # Pasibandom su zodziais 
# print('Zodziu_masyvas_1 pries rikiavima sort()')
# print(zodziu_masyvas_1)
# print('zodziu_masyvas_1 po sort()')
# zodziu_masyvas_1.sort()
# print(zodziu_masyvas_1)
# print('==================================')

# # append() Prideda elementą sąrašo/masyvo gale
# skaiciu_masyvas.append(zodziu_masyvas_0)
# print('Skaiciu masyvas po append() (papildymu) zodziu_masyvas_0')
# print(skaiciu_masyvas)
# print('==================================')

# # insert() Prideda elementą nurodytoje vietoje pagal indeksa
# print('Skaiciu masyvas po insert()')
# skaiciu_masyvas.insert(4, zodziu_masyvas_1)
# print(skaiciu_masyvas)

# # pop() Pašalina elementą nurodytoje vietoje
# skaiciu_masyvas.pop(1)
# print('Skaiciu masyvas po pasalinimo su pop(1)') # nepasalina saraso sarase elemento. 
# print(skaiciu_masyvas)
# #skaiciu_masyvas.pop(-1)
# #print('Skaiciu masyvas po pasalinimo su pop(-1)') # nepasalina saraso sarase elemento. 
# #print(skaiciu_masyvas)

# # remove() Pašalina pirmąjį elementą su nurodyta verte
# print('Skaiciu masyvas po pasalinimo su remove([Labas, Rytas])')
# skaiciu_masyvas.remove(['Labas', 'Rytas']) #tik visą masyvą kaip elementą, jei nurodom tik viena koki nors elemta is masyvo netrina
# print(skaiciu_masyvas)

# # index() Gražina pirmojo elemento indeksą su nurodyta verte
# print('Skaiciu masyvo pirmojo elemento 6 indeksas su index()')
# print(skaiciu_masyvas.index(6)) # Jei nurodome elemento verte kurios sarase nera gauname klaida

# # extend() Įtraukia sąrašo/masyvo elementus
# print('Skauciu masuvas su extend papildytas zodziu_masyvas_0')
# skaiciu_masyvas.extend(zodziu_masyvas_0) # papildo ne kaip masyvu, o kaip elementais
# print(skaiciu_masyvas)

# # count() Gražina nurodytos vertės elementų skaičių
# x = -0.99
# nurodyto_elemento_kiekis_x = skaiciu_masyvas.count(x)
# print('Masyve elementas ', x, ' pasikartoja: ', nurodyto_elemento_kiekis_x, ' kartus.')
# y = 'Elementas'
# nurodyto_elemento_kiekis_y = skaiciu_masyvas.count(y)
# print('Masyve elementas ', y, ' pasikartoja: ', nurodyto_elemento_kiekis_y, ' kartus.')

# # copy() Gražina sąrašo/masyvo kopiją
# masyvo_kopija = skaiciu_masyvas.copy()
# print('Skaiciu masyvo kopija: ')
# print(masyvo_kopija)

# # type() nurodo kintamojo tipą 
# print(type(skaiciu_masyvas))
# print(type(x))
# print(type(y))