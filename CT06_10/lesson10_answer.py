# 10.Recap1a
### Answer to flowchart is shown on the slides ###

# 10.Recap1b
import random
rand_int = random.randint(1, 15)
guess = int(input("Guess an integer between 1 and 15: "))

if guess == rand_int:
    print("That's it!")



# 10.1
number = -5
if number > 0:
    print(f"{number} is positive.")
else:
    print(f"{number} is negative.")



# 10.2
import random
rand_int = random.randint(1, 10)
guess = int(input("Pick a number between 1 and 10: "))

if guess == rand_int:
    print("Congratulations!! You did it!")
else:
    print("Oops, better luck next time!")



# 10.3
password = "passme"
user_input = input("Enter password: ")

if user_input == password:
    print("Login Successful")
else:
    print("Password Incorrect")



# 10.4
num = int(input("Input a number: "))
remainder = num % 2

if remainder == 0:
    print("This number is even")
else:
    print("This number is odd")



# 10.5
age = 20
if age < 13:
    print("Child")
else:
    if age <= 19:
        print("Teen")
    else:
        print("Adult")



# 10.6
temperature = int(input("What is the temperature? "))
if temperature < 20:
    print("Consider reading indoors.")
else:
    if temperature <= 30:
        print("It's a great day for cycling.")
    else:
        print("How about a swimming session?")



# 10.7
import random
rand_int = random.randint(1, 10)
guess = int(input("Pick a number between 1 and 10: "))

if rand_int > guess:
    print("Higher!")
else:
    if rand_int < guess:
        print("Lower!")
    else:
        if rand_int == guess:
            print("You got it!")
        else:
            print("Invalid input!")



# 10.8
import random
rand_int = random.randint(1, 10)
guess = int(input("Pick a number between 1 and 10: "))

if rand_int > guess:
    print("Higher!")
elif rand_int < guess:
    print("Lower!")
elif rand_int == guess:
    print("You got it!")
else:
    print("Invalid input!")



# 10.9
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")



# 10.10a
age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative")
elif age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 10.10b
age = int(input("Enter your age: "))
password = "passme"

if age < 0:
    print("Age cannot be negative")
elif age >= 18:
    print("Eligible to vote")
    user_pw = input("Enter password: ")
    if user_pw == password:
        print("Welcome, please cast your vote")
    else:
        print("Access Denied")
else:
    print("Not eligible to vote")