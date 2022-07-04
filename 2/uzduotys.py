# mylist = ["apple", "banana", "cherry"]
# print(mylist[0])
# mylist.pop(2)
# print(mylist)
# mylist.insert(0, "pear")
# print(mylist)

# mydictionary = {"apple": 1, "banana": 5, "cherry": 3}
# print(mydictionary["apple"])
# print(mydictionary.get('apple'))
# mydictionary.update({'carrot': 4})
# print(mydictionary)
# mydictionary.pop("apple")
# print(mydictionary)
# mydictionary["banana"] = 8
# print(mydictionary)

# 2 uzduotis

# from numpy import true_divide

# sum = 0
# while True:
#     skaicius = int(input("Įveskite pirmą skaičių "))
#     if skaicius < 0:
#         break
#     sum += skaicius

# print(sum)

# 3 uzduotis

# zodziai = []

# while True:
#     ivedimas = (input("Įveskite žodį: "))
#     if ivedimas == "":
#         break
#     zodziai.append(ivedimas)

# for numeris, zodis in enumerate(zodziai):
#     print(f"{numeris + 1}: {zodis}, simbolių kiekis: {len(zodis)}")
# print("Žodžių kiekis:", len(zodziai))

# 4 uzduotis

# import random

# print("Bus sugeneruoti 3 skaičiai")
# print("Jei vienas iš jų – 5, tu pralaimėjai!")

# for x in range(3):
#     num = random.randint(1, 6)
#     print(num)
#     if num == 5:
#         print("Pralaimėjai...")
#         break
# else:
#     print("Laimėjai!")

# 5 uzduotis

# metai = int(input("Iveskite metus: "))
# if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
#     print("Keliamieji metai")
# else:
#     print("Nekeliamieji metai")

# 6 uzduotis

# for metai in range(2000, 2100):
#     if metai % 400 == 0:
#         print(metai)
#     elif metai % 100 == 0:
#         continue
#     elif metai % 4 == 0:
#         print(metai)
#     else:
#         continue