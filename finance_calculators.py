import math

# Ask the user which calculator he/she would like to access.
which_calculator = input("""
Choose either 'investment' or 'bond' from the menu below to proceed:\n\n
investment - to calculate the amount of interest you'll earn or your investment.\n
bond       - to calculate the amount you'll have to pay on a home loan.
""").lower()

# Direct user to the chosen calculator.
if which_calculator == "investment":

    # Getting user's details about their investment.
    deposit = float(input("Please enter the amount of money you'd like to deposit: $"))
    interest_rate = float(input("Please enter your interest rate (%): ")) / 100
    duration = float(input("For how long are you investing (years)? "))
    interest = input("Would you like to apply 'simple' or 'compound' interest? ").lower()

    # Calculating total amount for simple interest (formulas provided on the exercise).
    # I used .2f throughout the program to format the final value to display cents.
    if interest == "simple":
        total_with_interest = deposit * (1 + interest_rate * duration)
        print(f"The total amount you'll receive is ${total_with_interest:.2f}.")

    # Calculating total amount for compound interest (formulas provided on the exercise).
    elif interest == "compound":
        total_with_interest = deposit * math.pow((1 + interest_rate), duration)
        print(f"The total amount you'll receive is ${total_with_interest:.2f}.")

    # Error message to be displayed when the user selects an invalid interest type for calculation.
    else:
        print("Sorry, invalid interest type.")

elif which_calculator == "bond":

    # Getting user's details about their mortgage.
    house_value = float(input("Please enter the value of your house: $"))
    interest_rate = float(input("Please enter your interest rate (%): ")) / 100
    duration = float(input("For how long are you repaying the bond (months)? "))
    monthly_interest_rate = interest_rate / 12          # gets the monthly interest rate to be used on the calculation.

    # Calculating total amount for mortgage payment (formulas provided on the exercise).
    monthly_payment_amount = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** (-duration))
    print(f"The monthly amount you have to pay is ${monthly_payment_amount:.2f}.")

# Error message to be displayed when the user selects an invalid option on the menu.
else:
    print("You chose an invalid option.")
