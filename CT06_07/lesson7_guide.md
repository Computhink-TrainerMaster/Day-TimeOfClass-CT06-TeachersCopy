# Lesson 7 - For Loop (Part 2)

## Recap 1: Debugging Average Score Program

### There is a total of 3 bugs in the following program.
### Identify and fix the bugs:

score_one = 80
score_two = 90
score_three = 75

total = score_one + score_two score_three

average_score = totl / 3

student_name = "Alex"

print("Average score for " + student_name + " is: " + average_score)

---------------------------------------------------------------

## Task 1: For Loop: 1 to 10 using range(start, stop)

Use a 'for' loop to print numbers from 1 to 10.

---------------------------------------------------------------

## Task 2: Even Numbers 2-20 Loop using
##         range(start, stop, step)

Print all even numbers between 2 and 20 using a 'for' loop and
range().

---------------------------------------------------------------

## Task 3: Countdown From 10 For Loop

Use a 'for' loop and range() to count down from 10 to 1.

---------------------------------------------------------------

## Task 4: Word Repetition Input Loop

Ask the user for a word and a number n. Print the word repeated
n times (on separate lines).

Example:
What word would you like to repeat? <<burger>>
How many times would you like to repeat? << 3 >>

output:
burger
burger
burger

---------------------------------------------------------------

## Task 5: Personalized Greeting Loop

Ask for a user's name and an integer n, then print a
personalized greeting n times.

Example:
What is your name? <<burger>>
How many times would you like to repeat? << 3 >>

output:
Nice to meet you, burger
Nice to meet you, burger
Nice to meet you, burger

---------------------------------------------------------------

## Task 6: Sum of Five User Inputs

Ask the user to input 5 numbers, one at a time, and print the
sum of these numbers.

Example:
What is number #1? <<5>>
What is number #2? <<2>>
What is number #3? <<4>>
What is number #4? <<1>>
What is number #5? <<7>>

output:
Sum of the 5 numbers is 19 

---------------------------------------------------------------

## Task 7: Multiplication Table Generator

Ask the user for a number, then print the multiplication table
for that number from 1 to 12.

Example:
What number for the timestable? > << 5 >>
output:
5 x 1 = 5
5 x 2 = 10
....
..
5 x 12 = 60

---------------------------------------------------------------

## Task 8: Number Pyramid Pattern

1. Ask the user for a number
2. Using the 'for' loop, print out the number like the
   following:

1
22
333
4444
55555

Hint: You can use a code like this >>> print("a" * 5)

---------------------------------------------------------------

## Task 9: Average Calculator of 5 numbers
Ms Tan would like to calculate the average score of her 5
students in class 6A.

Write a program to calculate the average of 5 numbers.

1. Using a 'for' loop, ask the user for 5 numbers one at a
   time.
2. Calculate the average for these 5 numbers and print it
   out.

You will need to 
a. sum up the numbers
b. divide the sum by the total count.

**DISCUSS with your Code Mentor and Class on how to
calculate the average**

---------------------------------------------------------------

## Task 10: Dynamic Average Calculator
Ms Tan also teaches class 6B and 6C, but all of them have
different number of students. Modify your program so that Ms
Tan can use the same program to calculate the average score
for all her classes.

Design a program that will calculate the average of the
numbers based on the number of students.

1. Ask the user for the number of score to find the
   average of.
2. Using a 'for' loop, ask the user for each student's score
   one at a time.
3. Calculate the average for the scores and print it out.

You will need to:
a. ask user for the number of students
b. sum up the numbers
c. divide the sum by the number of students