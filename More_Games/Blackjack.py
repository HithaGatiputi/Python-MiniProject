import refer
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(card):
    choice = random.sample(cards, 2)
    return choice

def score(choice):
    if sum == 21 and len(choice) == 2:
        return 0
    if 11 in choice and sum(choice) > 21:
        choice.remove(11)
        choice.append(1)

    return sum(choice)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif user_score == 0:
        return "LOSE. opponent has the Blackjack."
    elif computer_score == 0:
        return "WIN with a Blackjack."
    elif user_score > computer_score:
        return "You WIN"
    elif user_score < computer_score:
        return "Computer win"
    elif user_score ==  21:
        return "You LOSE to your opponent"
    else:
        return "You WIN"



def play_game():
    user_card = deal_card(cards)
    computer_card = deal_card(cards)

    user_score = score(user_card)
    computer_score = score(computer_card)

    is_game_over = False
    while not is_game_over:
        print()
        print(refer.logo_bj)
        print(f"    Your cards: {user_card}, current score : {user_score}")
        print(f"    Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue =  input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                user_card.append(random.choice(cards))
                user_score = score(user_card)
            else:
                is_game_over = True

    while computer_score != 0 and sum(computer_card) <17:
        computer_card.append(random.choice(cards))
        computer_score = score(user_card)

    print(f"Your final hand: {user_card}")
    print(f"Computer's final hand: {computer_card}")
    print(compare(user_score,computer_score))

game_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
if game_play == 'y':
    play_game()
else:
    print("Thank You ;)")
    print("You have exited the game.")