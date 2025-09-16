import random,string

def generate_random_string(lenght):
    lenght = 10
    letters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(letters) for _ in range(lenght))
    print("Password:",password)

generate_random_string(10)

print("thanks for using Password generator take love from mahatab :3")

    



