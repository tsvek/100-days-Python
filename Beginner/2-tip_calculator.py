# This program returns how much should pay each person including tips

print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
persons = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

amount = bill * (1 + percentage/100) / persons

print(f"Each person should pay: ${round(amount, 2)}")
