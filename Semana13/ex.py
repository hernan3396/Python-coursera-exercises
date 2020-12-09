test = {"asd": "asd"}
print(test)

c = {"a": 10, "b": 20, "c": 1}

print(sorted([(value, key) for key, value in c.items()], reverse=True))

cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)
print(cars)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
