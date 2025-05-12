from game_data import MENU
from os import system

def clear_screen():
    system('clear')

def check_resources(drink, resources):
    if drink not in MENU:
        print("Invalid drink choice.")
        return False
    drink_requirements = MENU[drink]["ingredients"]
    for resource, amount_needed in drink_requirements.items():
        if resource in resources and resources[resource] < amount_needed:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True

def print_report(resources):
    print(f"Water: {resources.get('water', 0)}ml")
    print(f"Milk: {resources.get('milk', 0)}ml")
    print(f"Coffee: {resources.get('coffee', 0)}g")
    print(f"Money: ${resources.get('money', 0):.1f}")

def check_transaction(drink, payment, resources):
    if drink not in MENU:
        print("Invalid drink choice.")
        return False
    drink_cost = MENU[drink]["cost"]
    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    resources["money"] = resources.get("money", 0) + drink_cost
    change = payment - drink_cost
    if change > 0:
        print(f"Here is ${change:.2f} dollars in change.")
    return True

def process_coins():
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
        return total
    except ValueError:
        print("Invalid input. Please enter whole numbers for coins.")
        return 0




def main():
    # Main program
    resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            print_report(resources)
        elif choice in MENU:
            if check_resources(choice, resources):
                payment = process_coins()
                if payment > 0 and check_transaction(choice, payment, resources):
                    for resource, amount in MENU[choice]["ingredients"].items():
                        resources[resource] -= amount
                    print(f"Here is your {choice}. Enjoy!")
            else:
                print("Cannot make drink.")
        else:
            print("Invalid choice.")

def play_again():
    while True:
        response = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
        if response in ['y', 'n']:
            return response == 'y'
        print("Invalid input. Please type 'y' or 'n'.")

while True:
    play_game = input("Do you want to play this game? Type 'y' or 'n': ").lower()
    if play_game in ['y', 'n']:
        break
    print("Invalid input. Please type 'y' or 'n'.")
while play_game == 'y':
    clear_screen()
    main()
    play_game = 'y' if play_again() else 'n'