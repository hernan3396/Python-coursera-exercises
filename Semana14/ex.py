import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.findall('^From: ', line):
        print(line)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
