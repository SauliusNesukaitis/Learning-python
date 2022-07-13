# Python failų pavadinimo taisyklės
# Įprastas __name__ ir __main__ naudojimo būdas atrodo taip:
# if __name__ == "__main__":
   # Do something here

# Pažiūrėkime, kaip tai veikia realiame gyvenime ir kaip iš tikrųjų naudoti šiuos kintamuosius.
# Python module to execute
import file_two_1

print("File one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")

# Vėlgi, paleisdami file_one pamatysite, 
# kad programa atpažino, kuris iš šių dviejų modulių 
# yra __main__, ir įvykdė kodą pagal mūsų teiginius 
# „first if else“.

# Kai tokie moduliai yra importuojami ir vykdomi, 
# jų funkcijos bus importuojamos ir vykdomas 
# aukščiausio lygio kodas.