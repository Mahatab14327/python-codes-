import random

print("Welcome to number guessing game")
number = random.randint(1,10)
chances =2
print("You have only 2 chances to guess the number")
guess =int = int (input("Enter your guess number between 1 to 10:"))
if guess == number:
    print("congratulations,you won")
else:
    print("Oops! Wrong guess.")
    print("The secret number was:",number)
    play_again = input("Do you want to try again? (yes/no): ").lower()
    if play_again != 'yes':
     
     print("Thanks for playing! Take love from Mahatab :3")