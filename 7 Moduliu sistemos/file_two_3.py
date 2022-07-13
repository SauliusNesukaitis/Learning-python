# Tarkime, kad modulis file_two yra tikrai didelis 
# ir turi daug funkcijų (mūsų atveju – dvi), 
# ir jūs nenorite jų visų importuoti. 
# Pakeiskite file_two, kad atrodytų taip:

# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

def function_three():
   print("Function three is executed")

def function_four():
   print("Function four is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")