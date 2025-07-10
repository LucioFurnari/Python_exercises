import pickle

listNames = ["Alex", "Felipe", "Marcos", "Mrhotkey"]

binary_file = open("names_list", "wb")

pickle.dump(listNames, binary_file)

binary_file.close()