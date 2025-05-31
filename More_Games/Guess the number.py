import random
print("WELCOME TO GUESS THE NUMBER GAME")

def compare(guess,ans,turn):
    if guess > ans:
        print("Too High")
        return turn - 1
    elif guess < ans:
        print("Too Low")
        return turn - 1
    else :
        print(f"You got it! The answer was {ans}.")

easy_level = 10
difficult_level = 5

def difficulty_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level
    else:
        return difficult_level

def game():
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100) 
    turns = difficulty_level()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = compare(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()

