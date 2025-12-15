print("Welcome to Study Time Analyzer")

days = int(input("Enter the number of days you studied:"))

total_hours = 0
for i in range(days):
      hours = float(input(f"Enter hours studied on day {i+1}:"))
      total_hours += hours
average_hours = total_hours /days
print(f"Total hours studied: {total_hours}")

if average_hours <=3:
       print("Exellent!good job")
elif average_hours <= 2:
        print("Good! but you can do better")
elif average_hours <= 1:
        print("You need to improve your study habits")
else:
     comment = print("Consider Very bad! improve your study schedule")  
print("\n----- Study Report -----")
print("Total Study Time:", total_hours, "hours")
print("Average Per Day:", average_hours, "hours")
print("Comment:",comment)

print("Thanks for using Study Time Analyzer take love from Mahatab!")