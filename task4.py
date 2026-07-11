import random
user_score = 0
computer_score = 0

print("*"*50)
print("   ROCK PAPER SCISSORS GAME")
print("*"*50)
print("Instructions:")
print("Type Rock, Paper, or Scissors")
print()
while True:
    user=input("Enter your choice (Rock/Paper/Scissor:)").lower()
    if user not in ("rock","paper","scissor"):
        print("Invalid choice! Please try again.\n")
        user_score+=1
        continue
    computer=random.choice(["rock","paper","scissor"])
    
    print("\nYou chose      :",user.capitalize())
    print("Computer chose :", computer.capitalize())
    
    if user==computer:
        print("Result: It's a Tie!")
    elif((user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")):
      print("Result: You Win!")
      user_score += 1
    else:
        print("Result : COMPUTER WINS!")
        computer_score+=1
    print("\nCurrent Score")
    print("You      :", user_score)
    print("Computer :", computer_score)
    again = input("\nDo you want to play again? (yes/no): ").lower

    if again != "yes":
        break

    print()
print("\n*"*50)
print("          FINAL SCORE")
print("*"*50)
print("You      :", user_score)
print("Computer :", computer_score)

if user_score > computer_score:
    print("\nCongratulations! You won the game.")
elif computer_score > user_score:
    print("\nComputer won the game.")
else:
    print("\nThe game ended in a tie.")

print("\nThank you for playing!")
    