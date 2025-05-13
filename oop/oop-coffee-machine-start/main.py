from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from game_controller import GameController
from os import system


def clear_screen():
    system('clear')


def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    is_on = True
    while is_on:
        options = menu.get_items()
        my_choice = input(f"What would you like? {options}: ").lower()
        if my_choice == "off":
            is_on = False
        elif my_choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif my_choice == "clear":
            clear_screen()
        elif my_choice == "menu":
            print(menu.get_items())
        else:
            drink = menu.find_drink(my_choice)
            if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    game_controller = GameController()
    game_controller.run(main, clear_screen)
