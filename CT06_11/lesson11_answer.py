# 11.Recap1
px = int(input("What is the price of the item? "))

if px <= 5:
    print("Sounds good!")
elif px <= 50:
    print("Are you sure you need this?")
elif px <= 500:
    print("Where are you getting this money from?!")
else:
    print("Don't even think about it!")



# 11.1
rider1 = 125
rider2 = 150
result = rider1 > 120 and rider2 > 120
print(result)  # Output: True



# 11.2
num = int(input("Input a number: "))
if (num % 3) == 0 and (num % 7) == 0:
    print("The number is divisible by 3 and 7!")



# 11.3
firstName = input("What is your first name? ")
lastName = input("What is your last name? ")
if firstName == "James" and lastName == "Leong":
    print("YOU ARE WANTED")
    


# 11.4
rider1 = 25
rider2 = 6
result = (rider1 >= 18) or (rider2 >= 18)
print(result)



# 11.5
age = int(input("What is your age? "))
if age < 12 or age > 65:
    print("Ticket Price: $15")
else:
    print("Ticket Price: $20")



# 11.6
input = input("Enter input: ")
if input == "M" or "Male":
    print("Valid Input")
else:
    print("Invalid Input")
    


# 11.7
user_input = input("Input colour: ")
if not user_input == "Green":
    print("Try again")



# 11.8
# Step 1: Ask the user for the day of the week
day_of_week = input("What is the day of the week? ")

# Step 2: Using the 'not' operator, check if the input is not "Saturday"
# Step 3: If true, print "It's not the weekend yet!"
if not day_of_week.lower() == "saturday":
    print("It's not the weekend yet!")



# 11.9
# Step 1: Prompt the user for a password
entered_password = input("Please enter your password: ")

# Step 2 and 3: Using the 'not' operator to check if the password is not "Python123", 
# and display "Access Denied" if the condition is true
if not entered_password == "Python123":
    print("Access Denied.")



# 11.10
want_burger = input("Do you want a burger? (Yes/No) ") == "Yes"
want_drink = input("Do you want a drink? (Yes/No) ") == "Yes"
want_fries = input("Do you want fries? (Yes/No) ") == "Yes"

if want_burger and want_fries and not want_drink:
    print("Won't you get thirsty?")



# 11.11
# Predefined username and password
stored_username = "John123"
stored_password = "pw123"

# Asking the user for their username and password
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

# Checking conditions
if entered_username == stored_username and entered_password == stored_password:
    print("Access Granted")
elif entered_username == stored_username or entered_password == stored_password:
    print("Either username or password is incorrect")
else:
    print("Access Denied")



# 11.12
game_status = "active"

if game_status == "active" or not game_status == "paused":
    print("Game in progress...")
else:
    print("Game is paused or inactive.")