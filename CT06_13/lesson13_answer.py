# 13.Recap1
balance = 1000

while True:
    print("Choose from one of the options (1-4):")
    print("1: Withdraw")
    print("2: Deposit")
    print("3: Check Balance")
    print("4: Exit")
    userChoice = int(input("Choice: "))
    if userChoice == 1:
        withdrawAmt = int(input("How much would you like to withdraw? "))
        if withdrawAmt <= balance:
            balance -= withdrawAmt
            print("You have withdrawn $" + str(withdrawAmt))
            print("Balance: $" + str(balance))
        else:
            print("You have insufficient funds")
    elif userChoice == 2:
        balance += int(input("How much would you like to deposit? "))
        print("Your new balance: " + str(balance))
    elif userChoice == 3:
        print("Your current balance is: $" + str(balance))
    elif userChoice == 4:
        break



# 13.1a
groceries = [
    "Apples",
    "Bread",
    "Carrots",
    "Dates",
    "Eggs",
    "Flour",
    "Grapes",
    "Honey"
]

# 13.1b
groceries[7] = "Herbs"

# 13.1c
groceries.append("Ice")
groceries.insert(1, "Bananas")

# 13.1d
del(groceries[2])



# 13.2
# Iterating through the list of grocerys and printing out messages based on conditions
for grocery in groceries:
    if grocery == "Apples":
        print(f"{grocery} : I need 5 of these")
    elif grocery == "Carrots":
        print(f"{grocery} : I need 3 of these")
    elif grocery == "Grapes":
        print(f"{grocery} : Get the FarmFresh brand")



# 13.3
basket = []

while True:
    item = input("What item have you added to your basket? ")
    if item == "end":
        break
    else:
        basket.append(item)

for i in basket:
    print("I have bought " + i)



# 13.4a
catalogue = []

while True:
    item = input("What item do you want to add to the online catalogue? ")
    if item == "end":
        break
    else:
        catalogue.append(item)

print("The final menu is:")
for item in menu:
    print("- " + item)

# 13.4b
customer_choice = input("What are you looking for? ")

# Initialize a variable to track if the item is found
item_found = False

# Loop through each item in the menu to check if the item exists
for item in menu:
    if item == customer_choice:
        item_found = True
        break  # Exit loop if item is found

# Checking if the food is in the menu using the flag
if item_found:
    print("Yes we sell that.")
else:
    print("Sorry, we don't have that.")



# 13.5
# Re-importing the 'random' library and regenerating the lucky draw numbers after reset
import random

# Initialize an empty list to store the lucky draw numbers
lucky_numbers = []

# Using a 'for' loop to add 10 random numbers into the list
for i in range(10):
    number = random.randint(1, 9999)
    lucky_numbers.append(number)

# Preparing to display the winners in the specified format
for i in len(lucky_numbers):
    print("Winner #" + str(i+1) + ": " + str(lucky_numbers[i]))



# 13.6
# Step 1: Create a list of pizza toppings
pizza_toppings = ["Mushrooms", "Pepperoni", "Pineapple", "Onions", "Sausage", "Bacon", "Extra cheese", "Black olives", "Green peppers", "Fresh garlic"]
user_toppings = []

# Step 2: Use a 'for' loop to print the list of pizza toppings without using len() or enumerate()
print("Available pizza toppings:")
i = 1  # Manually track the index
for topping in pizza_toppings:
    print(str(i) + ". " + topping)
    i += 1  # Increment the index manually

# Step 3: Ask the user which pizza topping they want (By index)

while True:
    user_choice = input("Please choose your pizza topping by number: ")
    if user_choice == "end":
        break
    else:
        user_toppings.append(pizza_toppings[int(user_choice) - 1])

for i in user_toppings:
    print(i)