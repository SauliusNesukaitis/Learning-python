import pickle
zodynas = {1:"Pirmas", 2:"Antras", 3:"Trecias"}

with open("zodynas.pkl", "wb") as pickle_out:
    pickle.dump(zodynas, pickle_out)

with open("zodynas.pkl", "rb") as pickle_in:
    naujas_zodynas = pickle.load(pickle_in)

print(naujas_zodynas)