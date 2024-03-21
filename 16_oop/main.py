from coffee.menu import Menu, MenuItem
from coffee.coffee_maker import CoffeeMaker
from coffee.money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def run_machine():
    user_input = input("What would you like? Espresso, Latte, or Cappuccino").lower()
    if user_input == "off":
        return
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input not in menu.get_items():
        print("Please enter one of one of three listed options.")
        run_machine()
    else:
        drink = menu.find_drink(user_input)

        resource_check = coffee_maker.is_resource_sufficient(drink)
        if not resource_check:
            return

        print(f"Your {user_input} costs {drink.cost}.")
        money_check = money_machine.make_payment(cost=drink.cost)
        if not money_check:
            return

        coffee_maker.make_coffee(order=drink)
        run_machine()

run_machine()