import random

user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper","scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

for i in range(3):
    if(user_action==possible_actions[i]):
        if(i==2):
            k=0
        else:
            k=i+1

        if(i==0):
            l=2
        else:
            l=i-1

        if user_action==computer_action:
            print(f"\nBoth players selected {user_action}. It's a tie!\n")
        elif computer_action==possible_actions[k]:
            print(f"\nComputer chose {computer_action}, you chose {user_action}.\n\n")
            print("YOU LOSE!")
        elif computer_action==possible_actions[l]:
            print(f"\nComputer chose {computer_action}, you chose {user_action}.\n\n")
            print("YOU WIN!!!")
            print()
