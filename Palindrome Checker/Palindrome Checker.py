print("Welcome to Palindrome Checker")

def is_palindrome(text):
 cleaned = text.replace(" ", " ").lower()
 return cleaned == cleaned[::-1]
user_input = input("Enter a word or pharase:")
if is_palindrome(user_input):
    print("Its a Palindrome")
else:
   print("Its not a Palindrome")

print("Thanks for using The Palindrome Checker take love from Mahatab :3")
