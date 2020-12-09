name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
file = open(name)

counts = dict()

for line in file:
    if line.startswith("From "):
        words = line.split()
        whours = words[5]
        hours = whours.split(":")
        counts[hours[0]] = counts.get(hours[0], 0) + 1

# sorts counts by key(hour of the day)
hours_sorted = sorted([(value, key) for value, key in counts.items()])

for hour in hours_sorted:
    print(hour[0], hour[1])
