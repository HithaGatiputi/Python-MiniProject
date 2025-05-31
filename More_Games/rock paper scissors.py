import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])
print("Computer chose:")
print(game_images[computer_choice])
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice ==0 and user_choice==2 :
    print("You win")
elif user_choice == 2 and user_choice==0 :
    print("You Lose")
elif computer_choice<user_choice:
    print("You Lose")
elif computer_choice>user_choice:
    print("You Win")
else :
    print("it's a Tie")