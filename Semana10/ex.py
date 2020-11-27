file_name = input("Enter the file name: ")
try:
    file = open(file_name + ".txt", "r")
except:
    print("El archivo", file_name, "no existe")
    quit()


for line in file:
    line = line.rstrip()
    print(line)
