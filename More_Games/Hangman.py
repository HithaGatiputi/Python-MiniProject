import random
import refer
print(refer.logo)

lives = 6

chosen_word = random.choice(refer.list)

display = []
for letter in chosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = (input("Guess a letter: ")).lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if "_" not in display:
        print("you win")
    if guess not in chosen_word:
        lives -= 1
        print(refer.stages[lives])
        if lives == 0:
            print("You lose")
            end_of_game = True


