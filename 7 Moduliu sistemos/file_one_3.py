# Ir norėdami importuoti konkrečias funkcijas iš modulio file_two_3, 
# faile file_one_3 naudokite bloką from import:

# Python module to execute
from file_two_3 import function_three, function_four

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
   function_one()
   function_two()
   function_three()
   function_four()
else:
   print("File one executed when imported")

# Išvada
# Yra tikrai puikus kintamojo __name__ naudojimo atvejis, 
# nesvarbu, ar norite failo, kurį būtų galima paleisti 
# kaip pagrindinę programą, 
# ar importuoti kitų modulių. 
# Galime naudoti if __name__ == "__main__" bloką, 
# kad leistų arba neleistų paleisti kodo dalių, 
# kai moduliai importuojami.

# Kai Python interpretatorius nuskaito failą, 
# kintamasis __name__ nustatomas kaip __main__, 
# jei vykdomas modulis, arba kaip modulio pavadinimas, 
# jei jis importuojamas. 
# Skaitant failą vykdomas visas aukščiausio lygio kodas, 
# bet ne funkcijos ir klasės (nes jos bus tik importuojamos).

