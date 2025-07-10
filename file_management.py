from io import open

file_text = open("file.txt", "r")

someText = "Hello friends, this is a txt file \n This is other text"
# file_text.write(someText)
print(file_text.read())
file_text.close()