import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01,
}

def check_resources(drink):
    for resource, amount in MENU[drink]["ingredients"].items():
        available = resources[resource]
        required = amount
        if available < required:
            print(f"Sorry, there is not enought {resource}.")
            return False
        return True

work = True

while work:
    #os.system("cls")    

# TODO 1. Ask user "What would you like?"
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

# TODO 2. Turn off machine by "off"
    if choice == "off":
        print("Coffe machine turns off. See you!")
        work = False

# TODO 3. Print report
    elif choice == "report":
        for item, amount in resources.items():
            unit = "ml"
            if item == "coffee":
                unit = "g"
            print(f"{item.capitalize()}: {amount}{unit}")
        print(f"Money: $ {profit}")
        continue

# TODO 4. Check resource sufficient
    elif choice in MENU.keys():
        if check_resources(choice):

        # TODO 5. Process coins
            print("Please insert coins.")
            amount = 0
            for coin, value in coins.items():
                insert = int(input(f"how many {coin}?: "))
                amount += insert * value

        # TODO 6. Check transaction successful
            if amount < MENU[choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
                continue
            elif amount > MENU[choice]["cost"]:
                change = amount - MENU[choice]["cost"]
                print(f"Here is ${change:.2f} dollars in change.")    

        # TODO 7. Make coffee
            profit += MENU[choice]["cost"]
            for resource in MENU[choice]["ingredients"]:
                resources[resource] -= MENU[choice]["ingredients"][resource]
            print(f"Here is your {choice}. Enjoy!")
        else:
            continue