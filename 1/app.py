# python -m venv venv

print("labas")

a = 8
print(a)

a = int(5)
print(a)

a = a - 4
print(a)

a = 8
print(float(a))

print("Labas \nvakaras")

zodis = "Code Academy"
print(zodis[1])
print(zodis[-2])
print(zodis[5:12])
print(zodis[5:12:2])
print(zodis[5::2])
print(zodis[:12:2])
print(zodis[::-1])
print(zodis.split())
print(zodis.upper())
print(zodis.replace('c', 'k'))
print(zodis.replace('Code', 'Music'))

a = 5
zodis = "Labas"
dar_vienas = "Sitas zodis"
print("a lygu: " + str(a) + ", zodis: " + zodis + ", dar vienas zodis - " + dar_vienas)
print("a lygu: " + str(a) + ", žodis: " + zodis + ", dar vienas žodis – " + dar_vienas)
print(f"a lygu {a}, žodis: {zodis}, dar vienas žodis – {dar_vienas}")

a = int(input("Įveskite pirmą skaičių "))
b = int(input("Įveskite antrą skaičių "))
print("Jūsų skaičių suma: ", a + b)