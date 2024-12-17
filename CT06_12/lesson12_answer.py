# 12.Recap1
num = int(input("Number to check if multiple of 3 and 5: "))

if (num % 3 == 0) and (num % 5 == 0):
    print("The number is divisble by 3 and 5!")
else:
    print("The number is not divisble by 3 and 5")



# 12.1a
visitors = 0

while visitors < 50:
    visitors += 1
    print("Visitors admitted: " + str(visitors))

# 12.1b
visitors = 18

while visitors < 30:
    visitors += 1
    print("Visitors admitted: " + str(visitors))

# 12.1c
visitors = 4

while visitors < 25:
    visitors += 1
    print("Visitors admitted: " + str(visitors))



# 12.2
visitors = 0

while visitors < 50:
    visitors += 1
    print("Visitors admitted: " + str(visitors))
    if visitors >= 30:
        break



# 12.3
order = input("What would you like to order? ")

while True:
    user_input = input("What would you like to order? ")
    if user_input == "end":
        break
    else:
        order = order + ", " + user_input

print("You have ordered: " + order)



# 12.4a
count = 10

while count >= 1:
    print(count)
    count -= 1
else:
    print("Happy New Year!")

# 2.4b
count = 10

while count >= 1:
    if count == 5:
        break
    print(count)
    count -= 1
else:
    print("Happy New Year!")



# 12.5a
import random

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    ans = num1 + num2
    user_ans = int(input("What is " + str(num1) + " + " + str(num2) + "? "))
    if user_ans == ans:
        print("That's correct!")
        break
    else:
        print("Wrong! Try again")

# 12.5a (with bonus)
import random

# Initialize the user's score
score = 0

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op_choice = random.randint(1, 3)  # Randomly choose between 1 and 3

    # Determine the operation and calculate the answer based on op_choice
    if op_choice == 1:
        operator = '+'
        ans = num1 + num2
    elif op_choice == 2:
        operator = '-'
        ans = num1 - num2
    else:
        operator = '*'
        ans = num1 * num2

    # Ask the user for their answer, using "+" for concatenation
    user_ans = int(input("What is " + str(num1) + " " + operator + " " + str(num2) + "? "))

    # Check if the user's answer is correct
    if user_ans == ans:
        print("That's correct!")
        score += 1  # Increment score
    else:
        print("Wrong! Try again")
        break

# Once the loop ends (game over), print the user's score
print("Game over! Your score is: " + str(score))



# 12.5b
import random

correct_answers = 0

while correct_answers < 5:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    ans = num1 + num2
    user_ans = int(input(f"What is {num1} + {num2}? "))
    if user_ans == ans:
        print("That's correct!")
        correct_answers += 1
    else:
        print("Wrong! Try again")

print("Congratulations! You've got 5 correct answers.")


# 15.5b (with bonus)
import random

# Initialize the user's score and skip/wrong answer count
score = 0
skip_count = 0

while score < 5 and skip_count <= 5:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op_choice = random.randint(1, 3)  # Randomly choose between 1 and 3

    # Determine the operation and calculate the answer based on op_choice
    if op_choice == 1:
        operator = '+'
        ans = num1 + num2
    elif op_choice == 2:
        operator = '-'
        ans = num1 - num2
    else:
        operator = '*'
        ans = num1 * num2

    # Ask the user for their answer, using "+" for concatenation
    user_input = input("What is " + str(num1) + " " + operator + " " + str(num2) + "? ")

    # Allow user to skip
    if user_input.lower() == "skip":
        skip_count += 1
        print("Question skipped.")
        if skip_count > 5:
            print("Disqualified for skipping too many questions.")
            break
    elif user_input.isdigit():
        user_ans = int(user_input)
        # Check if the user's answer is correct
        if user_ans == ans:
            print("That's correct!")
            score += 1
        else:
            print("Wrong! Try again.")
            skip_count += 1  # Treat wrong answers as skips for disqualification purposes
            if skip_count > 5:
                print("Disqualified for too many wrong answers.")
                break
    else:
        print("Invalid input, please enter a number or 'skip'.")

# Check reason for game ending
if score >= 5:
    print("Game over! You have answered 5 questions correctly.")
else:
    print("Game over! Disqualified.")



# 12.6
import random

num = 0

while num != 4:
    num = random.randint(1,6)
    print(num)

# 12.6 (With bonus)
import random

roll_till = int(input("What number would you like to roll until (1 to 6)? "))
num = 0
counter = 0

while num != roll_till:
    num = random.randint(1,6)
    print(num)
    counter += 1
    if counter > 10:
        print("You have won the jackpot!")
        break


print("Number of rolls: " + str(counter))