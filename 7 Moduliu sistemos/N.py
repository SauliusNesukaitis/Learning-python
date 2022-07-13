
import file_one_3

print("File N __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File N executed when ran directly")
else:
   print("File N executed when imported")