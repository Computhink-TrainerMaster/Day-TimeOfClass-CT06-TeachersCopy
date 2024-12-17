# 9.Recap1
import random

# Generate three random numbers between 1 and 6
first_number = random.randint(1, 6)
second_number = random.randint(1, 6)
third_number = random.randint(1, 6)

# Print the numbers
print("1st number: " + str(first_number))
print("2nd number: " + str(second_number))
print("3rd number: " + str(third_number))

# Check if all numbers are even and print the result
first_even = first_number % 2 == 0
second_even = second_number % 2 == 0
third_even = third_number % 2 == 0

all_even_odd = first_even == second_even == third_even
print("All numbers are even/odd: " + str(all_even_odd))



# 9.1
### Answer to flowchart is shown on the slides ###



# 9.2
days = int(input("Number of days the book has been borrowed: "))

if days > 25:
    print("Remember to return your book!")



# 9.3a
### Answer to flowchart is shown on the slides ###

# 9.3b
import random

rand_num = random.randint(1,10)
guess = input("Guess an integer between 1 and 10: ")

if guess == rand_num:
    print("That's the magic number!")



# 9.4a
### Answer to flowchart is shown on the slides ###

# 9.4b
px_apple = 1
num_apples = int(input("How many apples would you like to buy? "))

if num_apples <= 10:
    total = num_apples * px_apple
    print("Total price is: " + str(total))

if num_apples > 10:
    print("You will get a 10% discount for buying that many apples!")
    total = num_apples * px_apple * 0.9
    print("Total price is: " + str(total))



# 9.5a
### Answer to flowchart is shown on the slides ###

# 9.5b
px_apple = 0.60
px_orange = 0.90
total = 0

num_apples = int(input("How many apples would you like to buy? "))
num_oranges = int(input("How many oranges would you like to buy? "))

if num_apples <= 5:
    total = total + (num_apples * px_apple)

if num_apples > 5:
    total = total + (num_apples * px_apple * 0.9)

if num_oranges <= 5:
    total = total + (num_oranges * px_orange)

if num_oranges > 5:
    total = total + (num_oranges * px_orange * 0.9)

print("Total price is: " + str(total))



# 9.6
### Answer to flowchart is shown on the slides ###



# 9.7
# Initialize counter
positive_days = 0

# Assuming 7 days of readings for simplicity
for _ in range(7):
    temperature = float(input("Enter the day's temperature: "))
    if temperature > 0:
        positive_days += 1

print("Number of positive temperature days: " + str(positive_days))

# 9.8a
### Answer to flowchart is shown on the slides ###

# 9.8b
# Initialize sum
sum = 0

# Loop through 7 days of savings
for _ in range(7):
    savings = float(input("Enter the day's savings: "))
    if savings > 0:
        sum += savings

print("Total savings: " + str(sum))



# 9.9a
### Answer to flowchart is shown on the slides ###

# 9.9b
# Initialize counters
desirable = 0
undesirable = 0

# Loop for user input
for _ in range(10):
    number = float(input("Enter a number: "))
    if number > 3:
        desirable += 1
    if number <= 3:
        undesirable += 1

print(f"Desirable ratings: {desirable}, Undesirable ratings: {undesirable}")
