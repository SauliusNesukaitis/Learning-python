# 1 uzduotis
a = int(input("Įveskite pirmą skaičių "))
b = int(input("Įveskite antrą skaičių "))
if a < b:
    print("a mazesnis uz b")
elif a > b:
    print("a didesnis uz b")
else:
    print("a lygu b")

# 2 uzduotis

x = "Zen of Python"
print(x[-1])
print(x[-6])
print(x.split()[0])
print(x.split()[-1])
print(x.split()[0])
print(x.split()[1])
print(x.split()[2])
print(x.replace("Python", "Programming"))

# 3 uzduotis

print(x.upper())
print(x.casefold())
print(x.capitalize())
print(x.count("o"))
print(x.find("o"))

# 4 užduotis

a = int(input("Įveskite pirmą skaičių "))
b = int(input("Įveskite antrą skaičių "))
x = input("Kokį matematinį veiksmą reiktų atlikti? ")

if x == "+":
    print(a + b)
if x == "-":
    print(a - b)
if x == "/":
    print(a / b)


# 5 užduotis

skaicius = int(input("Įveskite skaičių: "))

if skaicius % 2 == 0:
    print("Įvestas skaičius yra lyginis!")
else:
    print("Įvestas skaičius yra nelyginis!")

if skaicius % 3 == 0:
    print("Įvestas skaičius dalinasi iš trijų") 