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


def get_drink_info(drink):
    """Returns the cost and ingredient of the drink."""
    drink_cost = MENU[drink]["cost"]
    drink_ingredients = MENU[drink]['ingredients']
    return drink_cost, drink_ingredients

def make_report(available_resources):
    """Returns report string."""
    result = ""
    for item, amount in available_resources.items():
            unit = "ml"
            if item == "coffee":
                unit = "g"
            result += f"{item.capitalize()}: {amount}{unit} \n"
    result += f"Money: $ {profit}"
    return result

def check_resources(drink_ingredients):
    """Returns True if resources is enought for drink making."""
    for resource, amount in drink_ingredients.items():
        if resources[resource] < amount:
            print(f"Sorry, there is not enought {resource}.")
            return False
    return True

def process_coins():
    """Returns the sum of coins inserted."""
    print("Please insert coins.") 
    amount = 0
    for coin, value in coins.items():
        insert = int(input(f"how many {coin}?: "))
        amount += insert * value
    return amount

def payment_check(payment, drink_cost):
    """Return True if money insert is enought."""
    if payment < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else: 
        change = payment - drink_cost
        print(f"Here is ${change:.2f} dollars in change.")
        global profit
        profit += cost
        return True
    
def make_drink(drink_ingredients, drink):
    """Update avaible resources and make the coffee."""
    for resource in drink_ingredients:
        resources[resource] -= drink_ingredients[resource]
    print(f"Here is your {drink}. Enjoy!")
    

work = True

while work: 
    
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower() # TODO 1. Ask user "What would you like?"
    if choice == "off": # TODO 2. Turn off machine by "off"
        print("Coffe machine turns off. See you!")
        work = False
    elif choice == "report": # TODO 3. Print report
        report = make_report(resources)
        print(report)
        continue
    elif choice in MENU.keys():        
        cost, ingredients = get_drink_info(choice)
        if check_resources(ingredients): # TODO 4. Check resource sufficient           
            total = process_coins() # TODO 5. Process coins
            if payment_check(total, cost): # TODO 6. Check transaction successful
                make_drink(ingredients, choice) # TODO 7. Make coffee
        else:
            continue
    else:
        print("Please, enter valid word!")