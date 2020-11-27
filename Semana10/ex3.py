# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

spam_confidence = 0
counter = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # strips and only gets the number, adds it to a var and adds +1 to counter
    line = line.rstrip()
    position = line.find(":")
    line = line[position+1:]
    line = line.lstrip()

    floating_number = float(line)
    spam_confidence = spam_confidence + floating_number
    counter = counter + 1

average_spam_confidence = spam_confidence/counter

print("Average spam confidence:", average_spam_confidence)
