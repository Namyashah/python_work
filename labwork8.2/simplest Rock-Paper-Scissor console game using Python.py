ai_list = ["rock","paper","scissor"]
import random
while True:
    human_turn = input("Enter your choice from(rock,paper,scissor) = ")
    print(f"User = {human_turn}")
    ai_turn = random.choice(ai_list)
    print(f"AI = {ai_turn}")
    if human_turn==ai_turn:
        print(f"This is a Tie!")
        break
    elif (human_turn == "rock" and ai_turn == "scissor"):
        print("You win")
    elif (human_turn == "scissor" and ai_turn == "paper"):
        print("You Win")
    elif (human_turn == "rock" and ai_turn == "paper"):
        print("You Win")
    else :
        print("I Win sorry!")