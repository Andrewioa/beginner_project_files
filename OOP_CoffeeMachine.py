# create the same Coffee machine project, using OOP

class Coins:
    def __init__(self):
        self.quarters = 25
        self.dimes = 10
        self.nickels = 5
        self.pennies = 1


class CoffeeMachine:
    def __init__(self):
        self._milk = 200
        self._water = 300
        self._coffee = 100
        self.bank = 0
        self._menu = {"espresso": {
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
            }
        }

    def report(self):
        print(f"The coffee machine has {self._coffee}g coffee, {self._water}mls water and {self._milk}mls milk left!")

    def make_coffee(self):
        while True:
            choice = input("What would you like? (press 'q' to quit)\nEspresso(1.50)/Latte(2.50)/Cappuccino(3.00)").casefold()
            cost = 0
            if choice in self._menu:
                if self._menu[choice]["water"] > self._water:
                    print("Not enough water! Sorry, try again later.")
                    break
                if self._menu[choice]["milk"] > self._milk:
                    print("Not enough milk! Sorry, try again later.")
                    break
                if self._menu[choice]["coffee"] > self._coffee:
                    print("Not enough coffee! Sorry, try again later.")
                    break
                print(f'{choice} costs {self._menu[choice]["cost"]}')
                try:
                    quarters = int(input("How many quarters? "))
                    self.bank += quarters * Coins().quarters
                    cost += quarters * Coins().quarters
                    dimes = int(input("How many dimes? "))
                    self.bank += dimes * Coins().dimes
                    cost += dimes * Coins().dimes
                    nickels = int(input('How many nickels? '))
                    self.bank += nickels * Coins().nickels
                    cost += nickels * Coins().nickels
                    pennies = int(input("How many pennies? "))
                    self.bank += pennies * Coins().pennies
                    cost += pennies * Coins().pennies
                except ValueError:
                    print("ERROR - Machine only accepts numbers of coins! Try again from the start.")
                    continue
                if cost > self._menu[choice]["cost"]:
                    change = cost - self._menu[choice]["cost"]
                    print(f"Here is your change -> {change}\nPreparing coffee...")
                elif cost == self._menu[choice]["cost"]:
                    print("Preparing coffee...")
                else:
                    print("Not enough money. Sorry, try again later with the correct amount of money!")
                    break
                self._coffee -= self._menu[choice]["coffee"]
                self._milk -= self._menu[choice]["milk"]
                self._water -= self._menu[choice]["water"]
                print(f"Here's your hot cup of {choice}! Enjoy!")
                self.report()
                continue
            elif choice == 'q':
                print("Come again!")
                break
            else:
                print("Please only choose from our menu! Try again!")
                continue


cafe = CoffeeMachine()
cafe.make_coffee()







