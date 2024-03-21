from data.data import MENU, resources, COIN_VALUES, menu_abbreviations, INGREDIENT_UNITS


def calculate_coin_total(coin_dict):
    total = 0
    for coin_type, coin_count in coin_dict.items():
        coin_subtotal = COIN_VALUES[coin_type] * coin_count
        total += coin_subtotal
    return total


def process_payment():
    quarters = int(input("Enter the number of quarters."))
    dimes = int(input("Enter the number of dimes."))
    nickles = int(input("Enter the number of nickels."))
    pennies = int(input("Enter the number of pennies."))
    coin_dict = {
        "penny": pennies,
        "nickel": nickles,
        "dime": dimes,
        "quarter": quarters
    }
    return calculate_coin_total(coin_dict)


class CoffeeMachine:
    def __init__(self, resource_dict):
        self.resources = resource_dict
        self.resources["money"] = 0

    def print_report(self):
        for ingredient, amount in self.resources.items():
            prefix = "$" if ingredient == "money" else ""
            suffix = INGREDIENT_UNITS[ingredient]
            print(f"{ingredient.title()}: {prefix}{amount}{suffix}")

    def check_resources(self, required_resources):
        sufficient_resources = True
        for ingredient, amount in required_resources.items():
            if amount > self.resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                sufficient_resources = False
        return sufficient_resources

    def subtract_resources(self, required_resources):
        # TODO: this can be combined with above into one method?
        for ingredient, amount in required_resources.items():
            self.resources[ingredient] -= amount

    def process_drink_choice(self, drink_type):
        required_resources = MENU[drink_type]["ingredients"]
        cost = MENU[drink_type]["cost"]
        resource_check = self.check_resources(required_resources)
        if not resource_check:
            return
        print(f"Your {drink_type} costs {cost}. Please insert coins.")
        payment = process_payment()
        if payment < cost:
            print(f"Sorry, that's not enough money. You need {cost}. Money refunded.")
        else:
            change = round(payment - cost, 2)
            print("Thank you for your payment.")
            if change > 0:
                print(f"Here is your change: ${change}.")
            self.resources["money"] += cost
            self.subtract_resources(required_resources)
            print(f"Here is your {drink_type}, enjoy!")
            self.run()

    def run(self):
        user_input = input("What would you like? Espresso (E), Latte (L) or Cappuccino (C)").lower()
        if user_input == "off":
            return
        elif user_input == "report":
            self.print_report()
            self.run()
        elif user_input not in menu_abbreviations:
            print("Please enter one of E (espresso), L (latte) or C (cappuccino).")
            self.run()
        else:
            drink_type = menu_abbreviations[user_input]
            self.process_drink_choice(drink_type)


coffee_machine = CoffeeMachine(resource_dict=resources)
coffee_machine.run()
