# 7.Recap1
score_one = 80
score_two = 90
score_three = 75

total = score_one + score_two + score_three

average_score = total / 3

student_name = "Alex"

print("Average score for " + student_name + " is: " + str(average_score))



# 7.1
# Printing numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)



# 7.2
# Printing all even numbers between 2 and 20 using a for loop and range()
for i in range(2, 21, 2):  # Start at 2, go up to 20, step by 2
    print(i)



# 7.3
# Counting down from 10 to 1 using a for loop and range()
for i in range(10, 0, -1):  # Start at 10, go down to 1, step by -1
    print(i)



# 7.4
word = input("What word would you like to repeat? ")
n = int(input("How many times would you like to repeat? "))

# Using a for loop to print the word n times
for _ in range(n):
    print(word)



# 7.5
name = input("What is your name? ")
n = int(input("How many times would you like to repeat? "))

for _ in range(n):
    print("Nice to meet you, " + name)



# 7.6
sum = 0

for i in range(1, 6):
    sum = sum + int(input("Input number #" + str(i) + ": "))
print("Sum of all the numbers is: " + str(sum))



# 7.7
num = int(input("What number for the timestable? "))

for i in range(1, 13):
    print(str(num) + " x " + str(i) + " = " + str(num*i))



# 7.8
num = int(input("How many layers do you want the pyramid to have: "))
for i in range(1, num + 1):
    print(str(str(i) * i))



# 7.9
sum = 0

for i in range(1, 6):
    sum = sum + int(input("Input number #" + str(i) + ": "))
average = sum / 5
print("Average of all the numbers is: " + str(average))
    



# 7.10
sum = 0
count = int(input("How many numbers would you like to find the average of: "))

for i in range(1, count + 1):
    sum = sum + int(input("Input number #" + str(i) + ": "))
average = sum / count
print("Average of all the numbers is: " + str(average))
