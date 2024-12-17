# 8.Recap1
tally = 1

for i in range(1, 6):
    tally = tally * int(input("Input number #" + str(i) + ": "))
print("Multiplication of all the numbers is: " + str(tally))



# 8.1a
import time

for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
    
# 8.1b
import time

timer = int(input("From what number do you want to countdown from? "))

for i in range(timer, 0, -1):
    print(i)
    time.sleep(1)



# 8.2a
import random

print(random.randint(1,6))

# 8.2b
import random

for i in range(20):
    print(random.randint(0,9999))



# 8.3a
var = True

print(var)

# 8.3b
var1 = True
var2 = True

result = var1 == var2

print(result)

# 8.3c
var1 = True
var2 = False

result = var1 == var2

print(result)



# 8.4a
import random

num1 = random.randint(1, 50)
num2 = random.randint(1, 50)
ans = num1 + num2

user_ans = int(input("What is " + str(num1) + " + " + str(num2) + "? " ))

print(user_ans == ans)

# 8.4b
import random

rand_num = random.randint(1, 50)

start = int(input("Guess the start range (smaller number): "))
end = int(input("Guess the end range (bigger number): "))

is_within_range = start <= rand_num <= end

print(is_within_range)



# 8.5
# Assigning a number to 'guess'
guess = int(input("What is your guess? "))

# Assigning a random integer between 1 and 10 to 'num1'
num1 = random.randint(1, 10)

# Checking if 'guess' is equal to 'num1'
is_correct = guess == num1

print(is_correct)



# 8.6
import random

num_qn = int(input("How many multiplication questions would you like? "))

for i in range(num_qn):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    ans = num1 * num2
    
    user_ans = int(input("What is " + str(num1) + " x " + str(num2) + "? " ))
    
    print(user_ans == ans)



# 8.7
number = int(input("Enter a number: "))

is_even = number % 2 == 0

print("The number is even: " + str(is_even))



# 8.8
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

is_multiple = number1 % number2 == 0

print("Is the first number a multiple of the second? " + str(is_multiple))