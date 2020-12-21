def function():
    principle = float(input("What is the principle? "))
    rate = float(input("What is the rate(%)? "))
    time = float(input("What is the time(in months)? "))
    simple_interest = (principle * rate * time)/100
    print("The simple interest is: ", "Tsh.", simple_interest)
function()