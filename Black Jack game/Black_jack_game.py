import os
import random
import art

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear_screen():
    os.system('clear')


def deal_card():
    return random.choice(card)


def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score = sum(cards)
    return score


def deal_initial_cards():
    return [deal_card(), deal_card()], [deal_card(), deal_card()]


def check_blackjack(your_cards, computer_cards):
    your_score = calculate_score(your_cards)
    if len(your_cards) == 2 and your_score == 21:
        print(f"\n    Your cards: {your_cards}, current score: {your_score}")
        print(f"    Computer's first card: {computer_cards[0]}\n")
        print(
            f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
        return "Blackjack! You win! \U0001F973"
    return None


def player_turn(your_cards, computer_cards):
    your_score = calculate_score(your_cards)
    print(f"\n    Your cards: {your_cards}, current score: {your_score}")
    print(f"    Computer's first card: {computer_cards[0]}\n")
    new_card = input(
        "\nType 'y' to get another card, type 'n' to pass: ").lower()
    if new_card == 'y':
        new_card = another_card(new_card, your_cards, computer_cards)
    your_score = calculate_score(your_cards)
    if your_score > 21:
        print(f"\nYour final hand: {your_cards}, final score: {your_score}")
        print(
            f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
        return "\nYou went over. You lose \U0001F622"
    return None


def computer_turn(computer_cards):
    computer_score = calculate_score(computer_cards)
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    return computer_score, computer_cards


def compare_scores(your_score, computer_score, your_cards, computer_cards):
    print(f"\nYour final hand: {your_cards}, final score: {your_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    if computer_score > 21:
        return "\nYou win! \U0001F973"
    if your_score <= 21 and computer_score <= 21:
        max_score = max(your_score, computer_score)
        if max_score == your_score and max_score == computer_score:
            return "\nIt's a tie! \U0001F91D"
        elif max_score == your_score:
            return "\nYou win! \U0001F973"
        else:
            return "\nComputer wins! \U0001F622"
    return "\ngame Over! \U0001F622"


def play_again():
    return input("\nDo you want to play another game of Blackjack? Type 'y' or 'n': ").lower() == 'y'


def black_jack():
    clear_screen()
    print(art.logo)

    # Deal initial cards
    your_cards, computer_cards = deal_initial_cards()

    # Check for Blackjack
    result = check_blackjack(your_cards, computer_cards)
    if result:
        return result

    # Player's turn
    result = player_turn(your_cards, computer_cards)
    if result:
        return result

    # Computer's turn
    computer_score, computer_cards = computer_turn(computer_cards)

    # Compare scores
    your_score = calculate_score(your_cards)
    return compare_scores(your_score, computer_score, your_cards, computer_cards)


def another_card(new_card, your_cards, computer_cards):
    while new_card == 'y':
        your_cards.append(deal_card())
        your_score = calculate_score(your_cards)
        print(f"\n    Your cards: {your_cards}, current score: {your_score}")
        print(f"    Computer's first card: {computer_cards[0]}")
        if your_score > 21:
            return 'n'
        new_card = input(
            "\nType 'y' to get another card, type 'n' to pass: ").lower()
    return new_card


# Main game
play_game = input(
    "\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while play_game == 'y':
    game = black_jack()
    print(game)
    play_game = 'y' if play_again() else 'n'
