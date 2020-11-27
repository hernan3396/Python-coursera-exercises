filename = input("Enter file name: ")
try:
    file = open(filename)
except:
    print("File", filename, " does not existe")
    quit()

for line in file:
    line = line.rstrip()
    line = line.upper()
    print(line)
