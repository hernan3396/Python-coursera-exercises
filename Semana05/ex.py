extraHoursLimit = 40
extraHoursRate = 1.5

hrs = input("Enter hours:")
rateString = input("Enter rate:")

try:
    h = float(hrs)
    rate = float(rateString)
except:
    print("Enter a number, bye")
    quit()


if h <= extraHoursLimit:
    payment = h*rate
    print(payment)
else:
    # solo las horas extras valen 1.5x
    # calculas la cantidad de horas extras
    extraHours = h - extraHoursLimit

    # get extra hours rate
    extraRate = rate*extraHoursRate

    # calculates payment acorrding to rates
    extraHoursPayment = extraHours*extraRate
    Normalpayment = extraHoursLimit*rate
    totalPayment = extraHoursPayment + Normalpayment
    print(totalPayment)
