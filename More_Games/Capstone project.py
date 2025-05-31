import refer
import random

print()
print(refer.logo_bj)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def play(cards):
    game_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    choice = random.sample(cards,2)
    value = 0
    for num in choice:
        value += num
    player_score = value

    dealer_choice =  random.sample(cards,2)
    value1 = 0
    for num in dealer_choice:
        value1 += num
    dealer_score = value1

    should_continue = input("Do you want to continue? Type 'y' or 'n': ")
    if should_continue == 'n':
        print("Game over.")
        return
    else:
        third_choice = random.choice(cards)
        player_score += third_choice
        print(f"You drew a {third_choice}. Your new score is {player_score}.")

play(cards)

