# # Sukurkite ir išsibandykite funkcijas, kurios:

# # 1. Gražinti trijų paduotų skaičių sumą.

# def skaiciu_suma(sk1, sk2, sk3):
#     return sk1 + sk2 + sk3


# print(skaiciu_suma(45, 5, 6))


# # 2. Gražintų paduoto sąrašo iš skaičių, sumą.

# def saraso_suma(sarasas):
#     suma = 0
#     for skaicius in sarasas:
#         suma += skaicius
#     return suma


# sarasas = [4, 5, 78, 8]
# print(saraso_suma(sarasas))


# # 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).

# # def didziausias_skaicius(*args):
# #     didziausias = args[0]
# #     for sk in args:
# #         if sk > didziausias:
# #             didziausias = sk
# #     return didziausias

# # arba

# def didziausias_skaicius(*args):
#     return max(args)


# print(didziausias_skaicius(5, 8, 789, 94, 78))


# # 4. Gražintų paduotą stringą atbulai.

# def stringas_atbulai(stringas):
#     return stringas[::-1]


# print(stringas_atbulai("Donatas Noreika"))


# # 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.

# def info_apie_sakini(stringas):
#     print(f"Šiame sakinyje yra {len(stringas.split())} žodžių")
#     didziosios = 0
#     mazosios = 0
#     skaiciai = 0
#     for simbolis in stringas:
#         if simbolis.isupper():
#             didziosios += 1
#         if simbolis.islower():
#             mazosios += 1
#         if simbolis.isnumeric():
#             skaiciai += 1
#     print(f"Didžiosios: {didziosios}, mažosios: {mazosios}, skaičiai: {skaiciai}")

# info_apie_sakini("Laba diena laba diena lab 522")


# # 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.

# def unikalus_sarasas(sarasas):
#     naujas_sarasas = []
#     for skaicius in sarasas:
#         if skaicius not in naujas_sarasas:
#             naujas_sarasas.append(skaicius)
#     return naujas_sarasas


# print(unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))


# # 7. Gražintų, ar paduotas skaičius yra pirminis.

# def test_prime(n):
#     if (n == 1):
#         return False
#     elif (n == 2):
#         return True;
#     else:
#         for x in range(2, n):
#             if (n % x == 0):
#                 return False
#         return True


# print(test_prime(5))


# # 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

# def isrikiuoti_nuo_galo(sakinys):
#     zodziai = sakinys.split()[::-1]
#     return " # ".join(zodziai)


# print(isrikiuoti_nuo_galo("Vienas du trys keturi"))

# # 9. Gražina, ar paduoti metai yra keliamieji, ar ne.

# import calendar


# def ar_keliamieji(metai):
#     return calendar.isleap(metai)


# print(ar_keliamieji(2020))
# print(ar_keliamieji(2100))
# print(ar_keliamieji(2000))

# # 10. Gražina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.

# import datetime


# def patikrinti_data(sukaktis):
#     ivesta_data = datetime.datetime.strptime(sukaktis, "%Y-%m-%d %X")
#     now = datetime.datetime.now()
#     skirtumas = now - ivesta_data

#     print("Praėjo metų: ", skirtumas.days // 365)
#     print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)
#     print("Praėjo savaičių: ", skirtumas.days // 7)
#     print("Praėjo dienų: ", skirtumas.days)
#     print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
#     print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
#     print("Praėjo sekundžių: ", skirtumas.total_seconds())


# patikrinti_data("2000-01-01 12:12:12")
# patikrinti_data("1991-03-11 12:12:12")

# 2 užduotis
# Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.

# Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją) pagal įvestą lytį, gimimo datą ir eilės numerį).

def grazinti_asmens_kodo_kontrolinį(asmens_kodas):
    kodas = str(asmens_kodas)
    A = int(kodas[0])
    B = int(kodas[1])
    C = int(kodas[2])
    D = int(kodas[3])
    E = int(kodas[4])
    F = int(kodas[5])
    G = int(kodas[6])
    H = int(kodas[7])
    I = int(kodas[8])
    J = int(kodas[9])
    S = A * 1 + B * 2 + C * 3 + D * 4 + E * 5 + F * 6 + G * 7 + H * 8 + I * 9 + J * 1
    if S % 11 != 10:
        return S % 11
    else:
        S = A * 3 + B * 4 + C * 5 + D * 6 + E * 7 + F * 8 + G * 9 + H * 1 + I * 2 + J * 3
        if S % 11 != 10:
            return S % 11
        else:
            return 0


def asmens_kodo_validacija(asmens_kodas):
    paskutinis_sk = int(str(asmens_kodas)[-1])
    return paskutinis_sk == grazinti_asmens_kodo_kontrolinį(asmens_kodas)


def asmens_kodo_generavimas(lytis, gimimo_data, eiles_numeris):
    pirmas_skaicius = ""

    data_split = gimimo_data.split("-")
    metai = int(data_split[0][:2])

    if lytis == "vyras":
        pirmas_skaicius = str((int(metai) - 18) * 2 + 1)
    else:
        pirmas_skaicius = str((int(metai) - 18) * 2 + 2)

    metai = data_split[0][2:]
    menuo = data_split[1]
    diena = data_split[2]

    be_paskutinio = pirmas_skaicius + metai + menuo + diena + eiles_numeris

    return int(be_paskutinio + str(grazinti_asmens_kodo_kontrolinį(be_paskutinio)))


print(asmens_kodo_validacija(45102129987))
print(asmens_kodo_validacija(61907108400))

print(asmens_kodo_generavimas("vyras", "2000-12-12", "512"))