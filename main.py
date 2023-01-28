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


def billing(coffee):
    """
    Receives money, processes and either dispenses a drink or reports that there is not enough money.
    :param coffee: str, a coffee type
    :return: int, profit from this billing
    """
    cash = 0
    cash += int(input("how many quarters?:")) * 0.25
    cash += int(input("how many dimes?:")) * 0.1
    cash += int(input("how many nickles?:")) * 0.05
    cash += int(input("how many pennies?:")) * 0.01
    if cash == MENU[coffee]["cost"]:
        print(f"Here is your {coffee} ☕️. Enjoy!")
        resource_reducer(coffee)
        return MENU[coffee]["cost"]
    elif cash > MENU[coffee]["cost"]:
        change = cash - MENU[coffee]['cost']
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {coffee} ☕️. Enjoy!")
        resource_reducer(coffee)
        return MENU[coffee]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0


def check_resources(coffee_name):
    """
    Checks if there are enough resources to prepare drinks.
    :param coffee_name: str
    :return: bool
    """
    try:
        milk = MENU[coffee_name]["ingredients"]["milk"]
    except KeyError:
        milk = 0
    water = MENU[coffee_name]["ingredients"]["water"]
    coffee = MENU[coffee_name]["ingredients"]["coffee"]

    if resources["water"] < water:
        print("Sorry there is not enough water.")
        return False
    elif resources["milk"] < milk:
        print("Sorry there is not enough milk.")
        return False
    elif resources["coffee"] < coffee:
        print("Sorry there is not enough coffee.")
        return False
    return True


def resource_reducer(coffee_name):
    """
    Decreases the value of the amount of resources, depending on how much is needed to create coffee.
    :param coffee_name: str
    :return: None
    """
    try:
        resources["milk"] -= MENU[coffee_name]["ingredients"]["milk"]
    except KeyError:
        pass
    resources["water"] -= MENU[coffee_name]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_name]["ingredients"]["coffee"]


def report():
    """
    Prints a report.
    :return: None
    """
    print(f"Water: {resources['water']}ml\n"
          f"Milk: {resources['milk']}ml\n"
          f"Coffee: {resources['coffee']}g\n"
          f"Money: ${profit}")


while True:
    request = input("What would you like? (espresso/latte/cappuccino):")
    if request == "off":
        exit()
    elif request == "report":
        report()
    elif request in MENU:
        if check_resources(request):
            profit += billing(request)
        else:
            continue
    else:
        print("Wrong!")
