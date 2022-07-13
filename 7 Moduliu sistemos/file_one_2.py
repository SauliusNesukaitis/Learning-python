# Kai tokie moduliai yra importuojami ir vykdomi, 
# jų funkcijos bus importuojamos ir vykdomas aukščiausio lygio kodas. 
# Norėdami pamatyti, kaip šis procesas veikia, pakeiskite failus, 
# kad jie atrodytų taip:

# Python module to execute
import file_two_2

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

# if __name__ == "__main__":
#   print("File one executed when ran directly")
# else:
#   print("File one executed when imported")

# Norėdami paleisti vieną iš šių funkcijų, pakeiskite file_one dalį if __name__ == "__main__", kad ji atrodytų taip:

# if __name__ == "__main__":
#   print("File one executed when ran directly")
#   function_two()
# else:
#   print("File one executed when imported")

# Be to, galite paleisti funkcijas iš importuotų failų. 
# Norėdami tai padaryti, pakeiskite file_one dalį 
# if __name__ == "__main__", kad atrodytų taip:

if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
   file_two_2.function_three()
else:
   print("File one executed when imported")