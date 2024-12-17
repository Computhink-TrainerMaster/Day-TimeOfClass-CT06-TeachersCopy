# Lesson 10 - If-Else Statements

# Recap 1: Random Number Guesser II
**Recap 1a**:
Draw out the flowchart (on a piece of paper) of a program for the
user to guess a magic number.

Your program will need to:
1. Generate a random integer between 1 to 15
2. Ask the user to guess a number
3. If the user guesses correctly:
    print "That's it!"

**Recap 1b**:
Translate the pseudocode that you have written for the
program (shown on screen) into python code.

-------------------------------------------------------------------

# Task 1: Positive or Negative Numbers
Write a program that will let the user know if the number they
have entered is positive or negative.

1. Ask the user to input a number
2. Using an 'if' statement, check if the number is greater than 0
        If it is, print "{number} is positive."
3. Use an 'else' statement for when the number is not greater than 0.
        In this case, print "{number} is negative."

-------------------------------------------------------------------

# Task 2: Random Number Guesser III
Create a Random Number Guesser program

1. Generate a random integer between 1 to 10
2. Ask the user to guess a number
3. If the user guesses correctly:
    print "Congratulations!! You did it!"
4. If the user guesses wrongly: 
    print "Oops, better luck next time!"

-------------------------------------------------------------------

# Task 3: Password Checker
Code a password checker to protect your code!

1. Assign a password to a variable
2. Ask the user to enter a password
3. If the password matches, print "Login Successful"
4. If the password does not match, print "Password Incorrect"

-------------------------------------------------------------------

# Task 4: Even or Odd?
Code a program to tell the user if a number is even or odd

1. Ask the user to input a number
2. Using the '%' operator, find out if a number is divisible by 2
   (A number that is divisible by 2 will leave no remainder when
   divided by 2)
3. If the number is even, print "This number is even"
4. If the number is odd, print "This number is odd"

-------------------------------------------------------------------

# Task 5: Simple Age Checker (nested if..else)
Using nested if..else condition, write a program that categorizes
a person's age as 'Child', 'Teen', or 'Adult'.

1. Initialize an 'age' variable and ask user for their age.
2. Use an 'if' statement to check if the age is less than 13.
        If true, print "Child"
3. Within the 'else' statement of the 1st 'if' statement, use
   another 'if' statement to check if the age is between 13 and 19.
        If true, print "Teen"
4. Else:
        Print "Adult"

-------------------------------------------------------------------

# Task 6: Activity Advisor (nested if..else)
Using nested 'if..else' statements, write a program that suggests
an activity based on the temperature:
1. Suggest reading indoors if temperature is below 20 degrees
2. Suggest cycling if temperature is between 20 and 30 degrees
3. Suggest swimming if temperature is above 30 degrees

1. Initialize a 'temperature' variable and ask user for temperature
2. Use an 'if' statement to check if the temperature is below 20
   degrees.
        If true, print "Consider reading indoors."
3. Within the else statement of the 1st 'if' statement, use another
   'if' statement to check if the temperature is between
   20 and 30 degrees.
        If true, print "It's a great day for cycling"
4. Else:
        Print "How about a swimming session?"

-------------------------------------------------------------------

# Task 7: Random Number Guesser IV (nested if..else)
Using nested 'if..else' conditions, code a Random Number Guesser
Program that tells the user if their guess is higher or lower,
and checks if they have guessed correctly. If not, the program
will assume invalid input.

Hint: You will need 3 separate 'if..else' conditions for this.

1. Generate a random integer betweeen 1 to 10
2. Ask the user to guess the number
3. If the correct number is greater than the guessed number:
        If true, print "Higher!"
4. Within the 'else' statement of the 1st 'if' statement, use
   another 'if' statement to check if the correct number is lower
   than the guessed number:
        If true, print "Lower!"
5. Within the 'else' statement of the 2nd 'if' statement, use
   another 'if' statement to check if the correct number is the
   same as the guessed number:
        If true, print "You got it!"
6. Else:
        Print "Invalid input!"

-------------------------------------------------------------------

# Task 8: Random Number Guesser V (if..elif..else)
Modify your answer in Task 7 to make use of 'elif' instead of
nested else..if statements.

-------------------------------------------------------------------

# Task 9: Grading System (if..elif..else)
Implement a grading system where grades are assigned as follows:
1. 'A' for scores 90-100
2. 'B' for scores 80-89
3. 'C' for scores 70-79
4. 'D' for scores 60-69
5. 'F' for scores below 60

1. Create a 'score' variable and ask user to input score
2. Use 'if..elif..else' to assign grades based on the score
   range.
3. Print the grade.

-------------------------------------------------------------------

# Task 10: Validating User Input (if..elif..else)
**Task 10a**:
Write a program that asks for the user's age and validate that it
is a positive integer before checking if they are eligible to vote.

1. Ask the user for their age and store it into the 'age' variable
2. First, check if age is less than 0
        If true, print "Age cannot be negative"
3. Then, check if age is more than or equals to 18
        If true, print "Eligible to vote"
4. Else, print "Not eligible to vote"

**Task 10b**: Login to vote (nested if..elif..else)
Modify your code to prompt user to enter a password upon confirming
that they are eligible to vote.

1. Create a 'password' variable that holds the password "passme"
2. Add a nested 'if' condition for if user's age is more than or
   equals to 18.
3. In the nested 'if' condition, ask eligible voters for the
   password.
4. If password entered is correct, print "Welcome, please cast your
   vote."
5. Else, print "Access Denied"