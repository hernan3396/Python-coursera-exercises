score = input("Enter Score: ")

try:
    fscore = float(score)
except:
    print("Write a number")
    quit()

if 0.0 <= fscore <= 1.0:
    if fscore >= 0.9:
        print("A")
    elif fscore >= 0.8:
        print("B")
    elif fscore >= 0.7:
        print("C")
    elif fscore >= 0.6:
        print("D")
    else:
        print("F")
else:
    print("Your number is out of range")
    quit()
