import random
print("Rock, Paper, Scissors Game!")
print("Type your choice: rock, paper, or scissors")
me = input("I choose: ").lower()
if me not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please type rock, paper, or scissors.")
    print("try again? (yes/no)")
    try_again = input().lower()
    if try_again == "yes":
        exec(open(__file__).read())
    else:
        exit()
computer = random.choice(["rock", "paper", "scissors"])
print("Computer chose:", computer)
if me == computer:
    print("It's a tie!")
elif (me == "rock" and computer == "scissors") or \
     (me == "paper" and computer == "rock") or \
     (me == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
    me = input("I choose: ").lower()
    me = input("I choose: ").lower()
print("thanks for using my first python game take love from mahatab")

print("try again? (yes/no)")
try_again = input().lower()
if try_again == "yes":
    exec(open(__file__).read())