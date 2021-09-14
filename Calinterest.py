import math

def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100), time))
    return result


prince = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time in years: "))
if time < 0:
    print("can't calculate")
else:
    amount = compound_interest(prince, rate, time)
    interest = amount - prince

    print("Compound interest is %.4f" % interest)