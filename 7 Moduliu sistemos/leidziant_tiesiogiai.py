# https://www.freecodecamp.org/news/if-name-main-python-example/
# Python if __name__ == __main__ Explained with Code Examples

# Kai Python interpretatorius nuskaito Python failą, pirmiausia jis nustato keletą specialių kintamųjų. Tada jis vykdo kodą iš failo.
# Vienas iš tų kintamųjų vadinamas __name__

# Jei atliksite šiuos žingsnis po žingsnio ir perskaitysite jo kodo fragmentus, 
# sužinosite, kaip naudoti if __name__ == "__main__" ir kodėl tai taip svarbu.

# Python modulių paaiškinimas

# Python failai vadinami moduliais ir identifikuojami pagal .py failo plėtinį. 
# Modulis gali apibrėžti funkcijas, klases ir kintamuosius.

# Taigi, kai inertpretatorius paleidžia modulį, kintamasis __name__ 
# bus nustatytas kaip __main__, jei vykdomas modulis yra pagrindinė programa.

# Bet jei kodas importuoja modulį iš kito modulio, 
# kintamasis __name__ bus nustatytas kaip to modulio pavadinimas.

# Pažiūrėkime į pavyzdį. Sukurkite Python modulį pavadinimu file_one.py ir įklijuokite šį aukščiausio lygio kodą: