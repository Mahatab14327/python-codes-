print("Welcome to the countdown timer")
import time

def countdown(t):
    while t:
        mins,secs = divmod(t,60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer,end="\r")
        time.sleep(1)
        t -= 1
        

seconds = int(input("Enter time in seconds: "))
countdown(seconds)

print("Time is up!")

print("thanks for using the countdown timer take love from Mahatab :3")

