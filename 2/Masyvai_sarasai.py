# „Python“ neturi integruoto masyvų palaikymo, tačiau vietoj jų galima naudoti „Python“ sąrašus.
# Taigi, tolimesniais pavyzdžiais parodysime, kaip naudoti Python sąrašus kaip masyvus.

# Kas yra masyvai?

# Masyvas yra specialus kintamasis, kuriame vienu metu gali būti daugiau nei viena reikšmė.
# Jei turite elementų sąrašą (pavyzdžiui, mėnesių sąrašą), mėnesių saugojimas
# masyve atskirais kintamaisiais, atrodytų taip:
# m0 = „Rugsėjis"
# m1 = „Sausis"
# m2 = „Liepa"

# Veiksmai su masyvo elementais
# Masyvas gali turėti daug reikšmių po vienu masyvo pavadinimu, ir tuomet masyvo
# reikšmes galite pasiekti nurodydami indekso numerį.

# Pvz. ieškome pirmojo masyvo elemento reikšmę:
masyvas = ["Rugsejis", "Spalis", "Lapkritis"]
pirmas_masyvo_elementas = masyvas[0]
print(pirmas_masyvo_elementas)

# Pakeiskime pirmojo masyvo elemento reikšmę:
masyvas[0] = "Sausis"
print(masyvas)

# Masyvo ilgis
# Norėdami rasti masyvo ilgį (masyvo elementų skaičių) reikalinga naudoti metodą
menesiai = ["Sausis", "Vasarins", "Kovas", "Balandis", "Geguze"]
print("Masyva sudaro ", len(menesiai), " elementai")

# Masyvo elementų ciklai
# Norint peržiūrėti visus masyvo elementus, galima naudoti ciklą for kas in kazkas.
# Norėdami atspausdinti kiekvieną masyve menesiai esantį elementą, aprašome taip:

for elementas in menesiai: #elemntas kintamasis gali buti i , n , m , sk, kt.
    print(elementas)
