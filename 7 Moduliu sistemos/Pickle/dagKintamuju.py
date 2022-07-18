import pickle

a = "10"
b = 7
c = 23

with open("abc.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)
    pickle.dump(b, pickle_out)
    pickle.dump(c, pickle_out)

# with open("abc.pkl", "rb") as pickle_in:
#     naujas_a = pickle.load(pickle_in)
#     naujas_b = pickle.load(pickle_in)
#     naujas_c = pickle.load(pickle_in)

with open("abc.pkl", "rb") as pickle_in:
    while True:
        try:
            print(pickle.load(pickle_in))
        except EOFError:
            break

# print(naujas_a)
# print(naujas_b)
# print(naujas_c)