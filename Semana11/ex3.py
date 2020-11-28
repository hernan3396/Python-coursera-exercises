mail_list = list()
file_name = input("Enter file name: ")
if len(file_name) < 1:
    file_name = "mbox-short.txt"

file = open(file_name)
counter = 0

for line in file:
    if line.startswith("From "):
        counter = counter + 1
        wline = line.split()
        print(wline[1])


print("There were", counter, "lines in the file with From as the first word")
