from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
my_coffee_machine = CoffeeMaker()
coin_module = MoneyMachine()

# print(drinks.get_items())
# print(drinks.find_drink('espresso').ingredients)
#
# my_coffee_machine.report()
# print(my_coffee_machine.is_resource_sufficient(drinks.find_drink('espresso')))
# my_coffee_machine.make_coffee(drinks.find_drink('espresso'))

# coin_module.report()
# print(coin_module.make_payment(1.5))

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'off': break
    elif user_input == 'report':
        my_coffee_machine.report()
        coin_module.report()
    elif user_input != 'espresso' and user_input != 'latte' and user_input != 'cappuccino':
        print("Wrong input! You can choose: espresso or latte or cappuccino only!")
    else:
        drink = drinks.find_drink(user_input)
        if my_coffee_machine.is_resource_sufficient(drink):
            if coin_module.make_payment(drink.cost):
                my_coffee_machine.make_coffee(drink)
