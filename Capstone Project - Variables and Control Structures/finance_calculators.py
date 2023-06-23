#Capstone Project

import math

print("\nFinancial Calculator!\n")
print("Please select the following options:\n")

calculator_type = input("investment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan\nEnter either 'investment' or 'bond' from the menu above to proceed: ")

if calculator_type == 'investment':
    print("\nYou have selected investment.\n")
    p = float(input("Enter the amount you want to deposit: "))
    r = float(input("Please enter the interest rate: "))
    t = float(input("Number of years do you plan on investing: "))
    interest_type = input("Do you want simple or compound interest?: ")
    
    if interest_type == 'simple':
        a = p * (1 + r * t)
        print(f"Here is the calculation of your simple investment: {a}")
    else:
        a = p * math.pow((1 + r), t)
        print(f"Here is the calculation of your compound investment: {a}")
    
elif calculator_type == 'bond':
    print("\nYou have selected bond.\n")
    p = float(input("Present value of the house: "))
    i = float(input("Interest rate?: "))
    n = float(input("Number of months do you plan on repaying the bond: "))
    bond = p * (i * (1 + i) ** n) / (((1 + i) ** n) - 1)
    print(f"Here is the calculation of your bond: {bond}")

else:
    print("You have selected an invalid option, please enter either 'Investment' or 'Bond'")