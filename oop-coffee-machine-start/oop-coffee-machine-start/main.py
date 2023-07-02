class MenuItem:

    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:

    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        options = ""
        for i in self.menu:
            options += (i.name + "/")
        options = options[:-1] + ": "
        return options

    def find_drink(self, order_name):
        for i in self.menu:
            if order_name == i.name:
                return i
        return None


class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resources_sufficient(self, drink):
        for i in self.resources:
            if self.resources[i] <= drink.ingredients[i]:
                print(f"sorry, there is not enough {i}")
                return False
        return True

    def make_coffee(self, order):
        for i in self.resources:
            self.resources[i] -= order.ingredients[i]
        print(f"Here is your {order.name}, enjoy!")


class MoneyMachine:

    def __init__(self, money):
        self.money = money

    def report(self):
        print(f"Money: ${self.money}")

    def make_payment(self, cost):
        quarters = float(input("please insert quarters: "))
        dimes = float(input("please insert dimes: "))
        nickles = float(input("please insert nickles: "))
        pennies = float(input("please insert pennies: "))
        change = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
        if cost <= change:
            self.money += cost
            print(f"here is your change ${change:.2f}")
            return True
        print("Sorry, there is not enough money")
        return False


menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine(0)

while True:
    choice = input(f"what would you like for today? {menu.get_items()}")
    if choice == "off":
        break
    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        choiceItem = menu.find_drink(choice)
        if coffeeMaker.is_resources_sufficient(choiceItem):
            if moneyMachine.make_payment(choiceItem.cost):
                coffeeMaker.make_coffee(choiceItem)











