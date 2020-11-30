counts = dict()
name = input("Enter file:")

if len(name) < 1:
    name = "mbox-short.txt"

file = open(name)

# reads the file and gets the email from the line, then adds it to the dict
for line in file:
    if line.startswith("From "):
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) + 1

# records the key with the bigger number (most amount of times)
bigword = None
bignumber = None

for key, value in counts.items():
    if bignumber is None or value > bignumber:
        bigword = key
        bignumber = value

print(bigword, bignumber)
