print("Welcome to Tip Calculator")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10,12,15 or 20?"))
split = int (input("How many people to split the bill?"))

tip_amount = (tip/100)* bill
total_bill = bill + tip_amount

amount_per_person = total_bill / split
print(f"\nTip amount: ${tip_amount:.2f}")

print(f"Total amount (including tip): ${tip_amount:.2f}")

print(f"Each person should pay: ${amount_per_person:.2f}")

print("Thanks for using Tip Calculator Take love from Mahatab :3")


