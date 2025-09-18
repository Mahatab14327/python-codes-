import random

print("Welcome to Dice Roller")

sides = int(input("Enter the number of sides on the dice:"))
sides=int(sides) if sides>0 else 6

rolls= int(input("How mane time do you want to roll the dice?:"))
print("Rolling the dice...")
results=[]

for i in range (rolls):
    results.append(random.randint(1,sides))
results.append(rolls)
print(f"Roll {i+1}: {rolls}")

print("Results summary:")
for num in range(1,sides+1):
    count=results.count(num)
    if count>0:
        print(f"{num} was rolled {count} time(s)")
print("Thanks for using Dice Roller take love from mahatab :3")

        

