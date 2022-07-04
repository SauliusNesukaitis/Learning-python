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

from numpy import true_divide


sum = 0
while True:
    skaicius = int(input("Įveskite pirmą skaičių "))
    if skaicius < 0:
        break
    sum += skaicius

print(sum)
