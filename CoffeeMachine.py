# coffee machine ingredients -> water:300mls, milk:200mls, coffee: 100g
# three types of coffee -> espresso, latte, cappuccino
# espresso ->cost:1.50, water:50mls, coffee:18g
# latte -> cost:2.50, water:200mls, coffee:24g, milk:150mls
# cappuccino -> cost:3.00, water:250mls, coffee:24g, milk:100

# Create the menu with the ingredients and the quantities of product inside the machine.
menu = {"espresso": {
    "water": 50,
    "cost": 150,
    "coffee": 18,
    "milk": 0},
    "latte": {
        "water": 200,
        "cost": 250,
        "coffee": 24,
        "milk": 150
    },
    "cappuccino": {
        "water": 250,
        "cost": 300,
        "coffee": 24,
        "milk": 100
    },
    "machine": {
        "water": 300,
        "coffee": 100,
        "milk": 200
    }
}
# a dict of the coins the machine accepts.
coins = {
    "quarters": 25,
    "dimes": 10,
    "nickels": 5,
    "pennies": 1
}

# create a function that shows the ingredients left inside the machine.
def report():
    print(
        f"The machine has {menu['machine']['water']}mls water, {menu['machine']['milk']}mls milk and"
        f" {menu['machine']['coffee']}grams of coffee left.")


# create a loop that keeps the machine working, until it runs out of any, of the ingredients.

while True:
    print("What would you like to order?\nEspresso(1.50)/Latte(2.50)/Cappuccino(3.00)")
    order = input()
    if order in menu:
        money = []
        print(f"{order}! That will be {menu[order]['cost']}")
        if menu["machine"]["water"] < menu[order]["water"]:
            print("Not enough water. Sorry!")
            break
        elif menu["machine"]["milk"] < menu[order]["milk"]:
            print("Not enough milk! Sorry!")
            break
        elif menu["machine"]["coffee"] < menu[order]["coffee"]:
            print("Not enough coffee! Sorry!")
        try:
            quarters = int(input("How many quarters? "))
            money.append(quarters * coins["quarters"])
            dimes = int(input("How many dimes? "))
            money.append(dimes * coins["dimes"])
            nickels = int(input("How many nickels? "))
            money.append(nickels * coins["nickels"])
            pennies = int(input("How many pennies? "))
            money.append(pennies * coins["pennies"])
            total = sum(money)
        except ValueError:
            print("Please enter coins. Not words or letters!")
            continue
        print(f"You have paid {sum(money)}.")
        if menu[order]["cost"] < total:
            change = total - menu[order]["cost"]
            print(f"Thank you! Here's your change, {change}. Please wait...")
        elif menu[order]["cost"] == total:
            print("Thank you! Please wait...")
        else:
            print(f"You don't have enough money! Here's your money back. {total}. Please try again.")
            continue
        menu["machine"]['water'] -= menu[order]["water"]
        menu["machine"]['milk'] -= menu[order]["milk"]
        menu["machine"]['coffee'] -= menu[order]["coffee"]
        print("Here you go! Enjoy!")
        report()
        next_customer = input("Next customer - Press Enter.")
        continue
    else:
        print("Please choose from our menu only.")
        continue
