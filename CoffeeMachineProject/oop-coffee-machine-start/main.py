from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
CoffeeMachine = CoffeeMaker()
CashHandler = MoneyMachine()
menu1 = Menu()
machine_on = True
while machine_on:
    selection = input("What would you like to order?"+"("+menu1.get_items()+")")
    if selection == "off":
        machine_on = False
    elif selection == "report":
        CoffeeMachine.report()
        CashHandler.report()
    else:
        drink = menu1.find_drink(selection)
        if drink is not None:
            serve_status = CoffeeMachine.is_resource_sufficient(drink)
            if serve_status:
                pay_status = CashHandler.make_payment(drink.cost)
                if pay_status:
                    CoffeeMachine.make_coffee(drink)
        else:
            print("Invalid entry")
