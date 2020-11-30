counts = dict()
line = input("Enter a line of text: ")
words = line.split()

print("Escribiste:", words)

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
for key in counts:
    print(key)

stuff = dict()
print(stuff.get("candy", -1))
