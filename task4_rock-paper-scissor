import random


choices = ["rock", "paper", "scissors"]


user_score = 0
computer_score = 0

print("Welcome to Rock, Paper, Scissors!")

while True:
    
    user_choice = input("Choose rock, paper, or scissors: ")
    if(user_choice not in choices):
        print("Invalid choice. Please try again.")
        continue

    
    computer_choice = random.choice(choices)
    print("You chose: ",user_choice)
    print("Computer chose: ",computer_choice)

    
    if user_choice == computer_choice:
        print("It's a tie!")
        
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    
    print("Score -> You: " ,user_score , " Computer: ", computer_score)

    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again == "no":
        print("Thanks for playing!")
        break
