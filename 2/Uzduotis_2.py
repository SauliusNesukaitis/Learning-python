# Random - atsitiktinių skaičių suformuotame nurodyto input pagalba dydžio sąraše 
# didžiausią elemento reikšmę pakeiskite 
# input pagalba nurodytu skaičiumi

import random
b=random.sample(range(10),10)
print(b)

skc=int(input('kokiu skaiciumi pakeisti maksimuma? '))

max=b[0] #imituojama pradine maksimali saraso elemto reiksme 
t=0 
i=0

for s in b:
    if s > max:
        max = s

print('Maksimali reiksme', max)

for e in b:
    if e == max:
        b[i] = skc
        print('Maksimalios reiksmes pozicija', i+1)
    i+=1

print(b)

