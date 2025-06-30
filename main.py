from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
todays_menu=Menu()
my_coffee_maker=CoffeeMaker()
my_money_machine=MoneyMachine()
is_on=True
while is_on:
    order = input(f"What drink would you like? {todays_menu.get_items()}")
    var = todays_menu.find_drink(order)
    if order=="report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif order=="latte" or order=="espresso" or order=="cappuccino":
        if my_coffee_maker.is_resource_sufficient(var):
            if my_money_machine.make_payment(var.cost):
                my_coffee_maker.make_coffee(var)
    else:
        is_on=False




