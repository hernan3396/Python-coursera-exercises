shift = 40.0


def computepay(h, r):
    if h <= shift:
        payment = h*r
        return payment
    else:
        overtime = h - shift
        normalpayment = shift*r
        overtimepayment = overtime*r*1.5
        return normalpayment + overtimepayment


hrs = input("Enter hours:")
rate = input("Enter rate:")

h = float(hrs)
r = float(rate)

p = computepay(h, r)

print("Pay", p)
