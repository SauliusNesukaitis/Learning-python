import N

print("File M__name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File M executed when ran directly")
else:
   print("File M executed when imported")