# Lesson 5 - Introduction to For Loop and range()

## Recap 1: Automated Birthday Invitation

You run a small business that creates personalized digital
birthday invitation cards. To automate the process, you decide
to write a Python program. 

This program should ask the user for:
1. birthday person's name
2. the age that they are turning that year
3. personal message from the sender

Finally, the program prints out a personalized invitation
message.

### Sample output:
"Happy <Age>th birthday <Name>! <Message>"

---------------------------------------------------------------

## Task 1: Name Cheer

Your school's Sports Day is coming up and you are coding a
program to cheer your schoolmates up.

Your program needs to:
1. Using input(), ask the user for their namee e.g. <Dave>
2. Print a cheer as shown below:
   
    ### Example:
    What is your name? [Input: "Dave"]
    Give me a D!
    Give me a a!
    Give me a v!
    Give me a e!
    What do we have?
    Dave is the best!

Note:
    Notice how "Give me a..." is repeated!
    Which function should you be using?

---------------------------------------------------------------

## Task 2: Repeated Sentence Loop

Print the sentence "I like chicken rice." 100 times using the
'for' loop

---------------------------------------------------------------

## Task 3: Sentence Repetition Loop with Order of Code
##         Sequence

Using the 'for' loop, print the following sentences sequence
100 times:
"I like cake."
"Give me more"

---------------------------------------------------------------

## Task 4: range(stop)

Using the 'for' loop, print the numbers from 0 - 59

Question:
How many numbers are printed? 

---------------------------------------------------------------

## Task 5: range(start, stop)

**Task 5a**:
Print numbers from 1 to 5 using a 'for' loop.

**Task 5b**:
Print numbers from 51 to 100 using a 'for' loop.

**Task 5c**:
Print numbers from 18 to 29 using a 'for' loop.

---------------------------------------------------------------

## Task 6: range(start, stop, step)

**Task 6a**:
Use a 'for' loop to print numbers from 2 to 24 in multiples of 2.

**Task 6b**:
Use a 'for' loop to print numbers from 8 to 96 in multiples of 8.

**Task 6c**:
Use a 'for' loop to print numbers from 5 to 1 in descending order.

---------------------------------------------------------------

## Task 7: Countdown timer

**Task 7a**:
Imagine you are the race official and to start the race, you
must say the following:

    Ready!
    3
    2
    1

Using a 'for' loop, recreate the above sequence.

**Task 7b**:
Create a countdown timer that counts from 10 to 1.
When the timer hits 1, print "Boo!"

---------------------------------------------------------------

## Task 8: User-Defined Range Counter

Using input(), ask the user for 2 numbers and store them in the
variables:
1. start
2. stop

Write a 'for' loop to count from **start** to **stop**

Note:
What happens if the user inputs a higher start number than stop?
Modify your code to be able to handle that scenario.

---------------------------------------------------------------

## Task 9: Accumulative Sum in Loop

1. Create a variable 'num' and assign the integer "0" to it
2. Create a 'for' loop that repeats 10 times
3. Add the sum of 'num' and the loop's parameter and print out
   the value.
4. Observe what happens.

Example:
1st iteration
    num = num + i
    print(num)

2nd iteration
    num = num + i
    print(num)

...

10th iteration
    num = num + i
    print(num)

Output:
    0
    1
    3
    6
    10
    15
    21
    28
    36
    45
