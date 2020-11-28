words = list()
file_name = input("Enter file name: ")
file = open(file_name)

for line in file:
    # gets lines in the file
    wline = line.split()
    # checks for repeated words, if not repeated it adds it to the words array
    for word in wline:
        if word not in words:
            words.append(word)


words.sort()
print(words)
