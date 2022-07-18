import pickle
# terminal => pip install pickle
# pythn => pip install pickle      suaktyvinti venv /print("labas")/

# Irasymas:
a = 1024

with open("a.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)

# Nuskaitymas:

with open("a.pkl", "rb") as pickle_in:
    naujas = pickle.load(pickle_in)

print(naujas)