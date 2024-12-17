# Lesson 14 - Turtle (Part 1)

## Recap 1: Die Rolling Simulator
**Recap 1a**:
Create a program that simulates the rolling of a die 5 times by
storing each roll in a list.

At the end of the 5 rolls, print the list.

Example Output:
[4, 6, 5, 3, 4]

1. Import the 'random' library
2. Create an empty list called 'rolls'
3. Using a 'for' loop, and the 'random.randint()' function, append
   a random number generated into the list. Repeat 5 times.
4. Print the 'rolls' list.

**Recap 1b**:
Using a 'for' loop, expand on your answer in Recap 1a to add up all
the numbers in the list generated

Example Output:
[4, 6, 5, 3, 4]
Sum: 22

1. Create a variable 'sum' with the value of 0
2. Using a 'for' loop, loop through the 'rolls' list:
        Add each item in the list into the variable 'sum'
3. Print the sum of all values in the list using string concatenation.

---------------------------------------------------------------------

## Task 1: Creating a window
**Task 1a**:
By importing the 'turtle' library and using the following functions,
create a blank window that stays:
1. turtle.Screen()
2. .mainloop()

**Task 1b**:
Modify your code to create a window that is 600 in width and 400 in
height

Hint:
???.setup(width=???, height=???)

---------------------------------------------------------------------

## Task 2: Creating a Turtle
By modifying the code you have done previously, create the
following agents:

**Your new code must be between the turtle.screen() and .mainloop()
function**

**Task 2a**:
Create an orange turtle

1. Using 'import', import the 'turtle' library
2. Using the 'turtle.Turtle()' function, create an agent called "turtle"
3. Using the '.shape()' function, set the shape of the "turtle" agent
   to a turtle
4. Using the '.fillcolor()' function, turn "turtle" orange

**Task 2b**:
Create a green square

1. Using 'import', import the 'turtle' library
2. Using the 'turtle.Turtle()' function, create an agent called "square"
3. Using the '.shape' function, set the shape of the "square" agent
   to a square
4. Using the '.fillcolor()' function, turn "square" green

---------------------------------------------------------------------

## Task 3: Drawing
Given the number of sides and each interior angle, draw each of the
following shapes using a loop and the following functions:
    .seth()
    .up()
    .down()
    .forward()
    .backward()
    .left()
    .right()

**Task 3a**: Draw a line
Number of sides: 1
Interior angle: NA

**Task 3b**: Draw a triangle
Number of sides: 3
Interior angle: 120

**Task 3c**: Draw a square
Number of sides: 4
Interior angle: 90

**Task 3d**: Draw a pentagon
Number of sides: 5
Interior angle: 72

**Task 3e**: Draw a hexagon
Number of sides: 6
Interior angle: 60

**Task 3f**: Draw a circle
Number of sides: 360
Interior angle: 1

---------------------------------------------------------------------

## Task 4: Creating a Crosshair (.goto(), .setx() and .sety())
Write a program that moves the turtle to draw a horizontal line
across the middle of the screen and then a vertical line down the
centre of the screen, creating a crosshair pattern.

1. Import the 'turtle' library
2. Using 'turtle.Screen()', create a turtle screen and set the window
   size to 600x400 using the following line of code:
        Hint: ???.setup(width=???, height=???)
3. Create a turtle, and use '.penup()'
4. Use '.goto()' to position your turtle at x = -300 and y = 0
5. Use '.pendown()' and use '.setx()' to set your turtle's x position
   to x = 300
6. '.penup()' and using '.goto()', reposition your turtle to
   x = 0 and y = 200
7. Use '.pendown()' and '.sety()' to set your turtle's y position
   to y = -200
8. End off with a '.mainloop()' function to keep the window open

---------------------------------------------------------------------

## Task 5: Random Points (.write())
Write a program where the turtle moves to 10 random positions on the
screen, drawing a small square at each spot. Display the x and y
coordinates of each position next to the squares.

1. Import 'turtle' and 'random' library
2. Create a 600x600 turtle screen using 'turtle.Screen()' and
   '.setup(width=,height=)' function
3. Within a 'for' loop,
        a. Create 'x' variable and assign a random value between
           -280 and 280.
        b. Create 'y' variable and assign a random value between
           -280 and 280.
        c. Using '.goto()', position your turtle at the random
           coordinate 'x' and 'y' generated.
        d. Using a 'for' loop and the movement commands, draw a 5x5
           small square
        e. Reposition your turtle object 40 steps lower than the
           randomly generated x and y coordinate
        f. Write the coordinate of the square using '.write()'
   

---------------------------------------------------------------------

## Task 6: Follow the Edge I (algorithm to detect edge)
Using .xcor() and .ycor() to detect the edge, make the turtle move
around the perimeter of the screen, turning at the corners.

1. Import the 'turtle' library
2. Create a 400x400 screen using '.Screen()' and '.setup()'
3. Create 2 variables that holds the x and y limit
4. Using .goto(), position the turtle at the lower left corner of the
   limit
5. Within a forever loop, use the following format for each direction,
   turn the turtle at each of the 4 corners:
        While 'x' coordinate of turtle is less than 'x' limit,
             Move forward
        Turn left 90