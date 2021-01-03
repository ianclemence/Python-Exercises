# Python3 program to find compound
# interest for given values.


def compound_interest():
    principle = float(input("Enter Principle: "))
    rate = float(input("Enter Rate: "))
    time = int(input("Enter Time: "))
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", "Tsh.", CI)


compound_interest()