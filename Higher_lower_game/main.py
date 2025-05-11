from art import logo, vs
from game_data import data
from random import choice
from os import system


def clear_screen():
    system('clear')


def format_account(account):
    account_name = account['name']
    account_desc = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(user_guess, follower_a, follower_b):
    if follower_a > follower_b:
        return user_guess == 'A'
    else:
        return user_guess == 'B'

def get_valid_guess():
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        if guess in ['A', 'B']:
            return guess
        print("Invalid input. Please type 'A' or 'B'.")

def main():
    score = 0
    print(logo)
    game_should_continue = True
    account_b = choice(data)

    while game_should_continue:

        account_a = account_b
        while True:
            account_b = choice(data)
            if account_b != account_a:
                break
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        guess = get_valid_guess()

        clear_screen()
        print(logo)

        follower_a_count = account_a["follower_count"]
        follower_b_count = account_b["follower_count"]

        is_correct = check_answer(guess, follower_a_count, follower_b_count)

        if is_correct:
            score += 1
            print(f"You are right! Correct score {score} \U0001F973")
        else:
            print(f"Sorry that's wrong. Final score: {score} \U0001F622")
            game_should_continue = False


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
