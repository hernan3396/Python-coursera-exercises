smallest = None
numbers = [3, 41, 12, 9]

for number in numbers:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number

print(smallest)
