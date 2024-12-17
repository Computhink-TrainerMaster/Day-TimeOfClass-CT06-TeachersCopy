# Lesson 16 - Turtle (Part 2)

## Recap 1: Quadruple the Number
Create a function that takes in a number and quadruples it

1. Create a function named quadrupleNumber() that takes in 1 argument
2. The function should take in a number, and return the quadrupled
   value of the number
4. Using the quadrupleNumber() function, print the quadruples of the
   following numbers:
    105 (ans: 420)
    24 (ans: 96)
    402 (ans: 1608)
    594 (ans: 2376)

----------------------------------------------------------------------

## Recap 2: Shape Creator
You want to create a shape creator program that will draw any shape
you want simply by giving the program the length and number of sides
that the shape must have.

To do this, you need to create a function with 2 parameters:
1. 'length'
2. 'num_sides'

1. Create a function called drawShape() that takes in the length
   of the sides, as well as the number of sides.
2. The function should draw a shape with the length of sides and
   the number of sides given
3. Using the shapeDrawer() function, draw the following:
**Recap 2a**:
    Square (4 sides)
**Recap 2b**:
    Hexagon (6 sides)
**Recap 2c**:
    Octagon (8 sides)

Hint:
The interior angle of a shape with n sides is given with the formula
180 - (360 / n)

You may refer to the following as a guide:
1. Import 'turtle' library
2. Set up a window
3. Create a turtle object and lift the pen to move without drawing
4. Define 'drawShape' function to draw a regular polygon based on
   specified length and number of sides

----------------------------------------------------------------------

## Recap 3: Drawing a house
You have been tasked to draw a house (made of a square and a triangle)

Using the 'drawShape' function you have just created, create a house
by first drawing a square, then a triangle above the square.

1. The house is made up of a 100x100 square and a triangle that is
   100 units long each side.
2. The triangle must be connected to the square

You may refer to the following as a guide:
1. (Recap 2) - Import 'turtle' library
2. (Recap 2) - Set up a window
3. (Recap 2) - Create a turtle object and lift the pen to move
   without drawing
4. (Recap 2) - Define 'drawShape' function to draw a regular polygon
   based on specified length and number of sides
5. (NEW!) - Define 'drawHouse' function that uses the 'drawShape'
   function to combine a square and a triangle

----------------------------------------------------------------------

## Recap 4: Drawing a town
You would like to create a small town of houses.

Modify your answer to the previous task by turning it into a new
'drawHouse()' function.

Then using a nested 'for' loop and the 'drawHouse()' function that
you have just created, draw a grid of 3 x 3 houses.

You may refer to the following as a guide:
1. (Recap 2) - Import 'turtle' library
2. (NEW!) - Set up a 600x600 window
3. (Recap 2) - Create a turtle object and lift the pen to move
   without drawing
4. (Recap 2) - Define 'drawShape' function to draw a regular polygon
   based on specified length and number of sides
5. (Recap 3) - Define 'drawHouse' function that uses the 'drawShape'
   function to combine a square and a triangle
6. (NEW!) - Move turtle to starting position at (-200,200)
7. (NEW!) - Use loops to draw a 3x3 grid of houses, moving the turtle
   as needed between houses and rows

----------------------------------------------------------------------

## Task 1: Creating a turtle window
By creating and using the following function, create a turtle window
that is 300(w) x 500(h):

setup_screen(screenWidth, screenHeight)
* Returns a window that is screenWidth x screenHeight

You will require the following:
1. import turtle
2. turtle.Screen()
3. .setup(width=???, height=???)
4. return
5. 'screenWidth' variable
6. 'screenHeight' variable

----------------------------------------------------------------------

## Task 2: Creating a turtle object
By creating and using the following function, create a blue circular
turtle object with its pen lifted:

create_blue_ball()
* Returns a blue circular turtle object with pen lifted

You will require the following:
1. turtle.Turtle()
2. .shape()
3. .color()
4. .penup()
5. return

----------------------------------------------------------------------

## Task 3: Moving turtle object
By creating and using the following function, move the turtle object
by 'dx' and 'dy' in a forever loop:

move_ball(ball, dx, dy)
* Move ball by 'dx' and 'dy'

You will require the following:
1. .setx()
2. .xcor()
3. .sety()
4. .ycor()
5. 'dx' variable
6. 'dy' variable

----------------------------------------------------------------------

## Task 4: Detecting edge
**Task 4a: x-axis**
By creating and using the following function, reverse the x-direction
that the turtle object is moving when it touches the left/right side
of the window:

check_x(ball, screenWidth)
* Returns 'True' if ball is beyond window in the x-axis

You will require the following:
1. .xcor()
2. screenWidth/2
3. or
4. -screenWidth/2
5. *= -1

**Task 4b: y-axis**
By creating and using the following function, reverse the y-direction
that the turtle object is moving when it touches the top/bottom side
of the window:

check_y(ball, screenHeight)
* Returns 'True' if ball is beyond window in the y-axis

You will require the following:
1. .ycor()
2. screenHeight/2
3. or
4. -screenHeight/2
5. *= -1