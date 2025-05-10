import art, os, random

hard_level = 5
easy_level = 10


def clear_screen():
    os.system('clear')

def starting_message():
    clear_screen()
    print(art.logo)
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100.")


def set_difficulty():
    while True:
        difficulty_level = input("\nChoose a difficulty. Type 'easy' or 'hard': ").lower()

        if difficulty_level == 'easy'or difficulty_level == 'e':
            return easy_level
        elif difficulty_level == 'hard' or difficulty_level == 'h':
            return hard_level
        else:
            print("Invalid choice. Please try again.")

def guessing_logic(user_guess, answer, turns):
        if user_guess < answer:
            print("\nToo low.")
            return turns -1
        elif user_guess > answer:
            print("\nToo high.")
            return turns -1
        else:
            print(f"\nYou got it! The answer was {answer}.")
            return turns

def main():
    random_number = random.randint(1, 100)
    starting_message()
    turns = set_difficulty()

    guess = 0
    while guess != random_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = guessing_logic(guess,random_number,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != random_number:
            print("Guess again.")



def play_again():
    return input("\nDo you want to play another game of Number Guessing? Type 'y' or 'n': ").lower() == 'y'

play_game = input("Do you want to play Number guessing game? Type 'y' or 'n': ").lower()
while play_game == 'y':
    main()
    play_game = 'y' if play_again() else 'n'