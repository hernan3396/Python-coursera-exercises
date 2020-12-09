import re

name = input("Enter file:")
if len(name) < 1:
    name = "regex_test.txt"
file = open(name)

total = 0

for line in file:
    line = line.rstrip()
    numbers_in_line = re.findall('[0-9]+', line)
    if len(numbers_in_line) > 0:
        for number in numbers_in_line:
            total = int(number) + total

print(total)
