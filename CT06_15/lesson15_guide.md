# Lesson 15 - Functions

## Recap 1: Turtle drawing
**Recap 1a**:
Using the 'turtle' library, create a 200x200 window

1. Import 'turtle' library
2. Using '.setup()', create a window 200 in width and 200 in height
3. Add a '.mainloop()' function to keep the window open

**Recap 1b**:
Modify your previous code to create a blue arrow as your turtle.

1. Create a turtle called "artist" using 'turtle.Turtle()'
2. Using '.shape()', change the turtle shape to "arrow"
3. Using '.color()', change the turtle color to "blue"

**Recap 1c**:
Modify your previous code to draw the shape of a compass rose (shown
on screen)

1. Use '.penup()' and position turtle to (0, 0) using '.goto()'
2. Point turtle towards North ("90") using '.seth()'
3. Use '.pendown()' and draw "60" towards North
4. Using '.right()', turn turtle 90 degrees to the right 
5. Using a 'for' loop, draw a circle by moving 1 step each time
   before turning 1 degree to the right for 360 times.

**Recap 1d**:
Modify your previous code to print the position of your turtle at the
end of the drawing.

1. Using '.xcor()' and 'ycor()', print onto the console your turtle's
   last coordinates in the following format:

   "Current turtle position: <x>, <y>"

---------------------------------------------------------------------

## Task 1: Self-introduction
You are at a party, and you expect to see your friend Ethan and 3 of
his friends you have never met before. They are Ben, Gracie, and
Javior.

Write a program (with or without functions) that will ask the user
for their name and print 1 of 3 ways to greet the person:
1. If the person is Ethan, greet him by saying:
        "Hi Ethan. How are you?"
2. If the person is either Ben, Gracie, or Javior, greet them by
   saying:
        "Hi there!"
        "My name is Freddo"
        "I like to swim and eat chicken wings!"
        "Nice to meet you!"
3. If the person is none of the above, say:
        "I don't think you belong here..."

---------------------------------------------------------------------

## Task 2: Square
Using the 'turtle' library, create a function that draws a square.
Use the function you have created to draw the pattern shown on the
screen.

1. Import the 'turtle' library
2. Set up the screen using 'turtle.Screen()'
3. Create a function, "draw_square" that will draw a 20x20 square
4. Using 'for' loops and the "draw_square" function you have created,
   draw the pattern shown on the screen.
5. You will have to reposition your turtle before calling the
   "draw_square" function each time.

---------------------------------------------------------------------

## Task 3: Increment Counter
Create a function that will increase the 'counter' variable by 1 each
time it is called.

1. Create a 'counter' variable and assign it '0'
2. Define a function 'increment_counter()':
        a. Declare 'counter' as 'global'
        b. Add 1 to 'counter'
3. Test your program out by calling the 'increment_counter()' function
4. 3 times before printing out the value of the 'counter' variable.

Your output should be "3"

---------------------------------------------------------------------

## Task 4: Square to Square
Use a function with parameters to draw 7 squares to form the pattern
shown on the screen.

1. Import the 'turtle' library
2. Create a 400x400 screen
3. Create a function "draw_square" with a "size" parameter
4. The "draw_square" function will draw a square of size*size around
   the (0,0) coordinate.
5. Within a 'for' loop, use the draw_square function you have created
   to draw 7 squares around the (0,0) coordinate with the following
   sizes:
        50, 100, 150, 200, 250, 300, 350

---------------------------------------------------------------------

## Task 5: Double the Number
Create a function that takes in a number and doubles it

1. Create a function named 'doubleNumber()'
2. The function should return the doubled number
3. Using the 'doubleNumber()' function, print the doubles of the
   following numbers:
    4
    9
    1530
    284

---------------------------------------------------------------------

## Task 6: Greetings III
Create a function that takes in a name and returns a greeting

1. Create a function named 'greet()'
2. The function should return a greeting
    Example: "Hello there <name>!"
3. Ask the user for their name
4. Using the 'greet()' function, print the greeting

----------------------------------------------------------------------

## Task 7: Even or Odd? III
Create a function that takes in a number and returns whether it is
even

1. Create a function named isEven()
2. If the number is even, the function should return True
3. If the number is odd, the function should return False
4. Using the 'isEven()' function, loop through a list of numbers and
   print them out in this format:
    "3 is an odd number"
    "9 is an odd number"
    "2 is an even number"

----------------------------------------------------------------------
   
## Task 8: Age Group
Create a function that will take in someone's age and return either
'Child' (Below 13), 'Teen' (14-20), 'Adult' (21-64), or
'Senior' (65 and above) based on the age provided.

1. Define the function 'ageGroup()' with one parameter: 'age'.
2. Use 'if-elif-else' statements to return the appropriate age group
   based on the 'age' parameter

----------------------------------------------------------------------

## Task 9: Calling a function within a function
**Task 9a**:
Create a function 'square()' that will take in a number and return
the squared value of the number. Squared is when the number is
multiplied by itself.

For example, "5 squared" is 5x5, giving us 25.

Example:
square(3) >>> 9

**Task 9b**:
Create a function 'sum_of_squares()' that will take in 2 numbers and
return the sum of each of the number squared. You must use the
'square()' function within the 'sum_of_squares()' function.

Example:
sum_of_squares(3, 4) >>> 25