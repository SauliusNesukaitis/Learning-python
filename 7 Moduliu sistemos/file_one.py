# Python file one module
import file_two

# Dar kartą paleidus failą_one kodą, pamatysite, 
# kad failo file_one kintamasis __name__ nepasikeitė 
# ir vis tiek išlieka nustatytas į __main__. 
# Bet dabar kintamasis __name__ faile_two 
# yra nustatytas kaip modulio pavadinimas - faile_two.

# Bet paleiskite failą_two tiesiogiai ir pamatysite, kad jo pavadinimas nustatytas į __main__


print("File one __name__ is set to: {}" .format(__name__))