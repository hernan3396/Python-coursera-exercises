largest = None
smallest = None

while True:
    num = input("Enter a number")

    if num == "done":
        break

    try:
        num_int = int(num)
    except:
        print("Invalid input")
        continue

    if smallest is None and largest is None:
        smallest = num_int
        largest = num_int
        continue

    if smallest > num_int:
        smallest = num_int
        continue

    if largest < num_int:
        largest = num_int
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
