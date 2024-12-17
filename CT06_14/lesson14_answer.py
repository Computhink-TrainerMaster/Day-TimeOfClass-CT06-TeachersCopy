# 14.Recap1a
import random

rolls = []

for i in range(5):
    rolls.append(random.randint(1,6))

print(rolls)

# 14.Recap1b
import random

rolls = []

for i in range(5):
    rolls.append(random.randint(1,6))

print(rolls)

sum = 0

for i in rolls:
    sum = sum + i

print("Sum: " + str(sum))



# 14.1a
import turtle
window = turtle.Screen()
window.mainloop()

# 14.1b
import turtle
window = turtle.Screen()
window.setup(width=600, height=400)
window.mainloop()



# 14.2a
import turtle
window = turtle.Screen()

# 1. Create a turtle agent
t = turtle.Turtle()

# 2. Set the shape to a turtle
t.shape("turtle")

# 3. Fill the turtle with orange color
t.fillcolor("orange")

window.mainloop()

# 14.2b
import turtle
window = turtle.Screen()

# 1. Create a turtle agent
t = turtle.Turtle()

# 2. Set the shape to a turtle
t.shape("square")

# 3. Fill the turtle with orange color
t.fillcolor("green")

window.mainloop()



# 14.3
import turtle

window = turtle.Screen()
t = turtle.Turtle()

# 14.3a
t.forward(100)
t.right(60)

window.mainloop()

# 14.3b
for i in range(3):
    t.forward(100)
    t.right(120)

window.mainloop()

# 14.3c
for i in range(4):
    t.forward(100)
    t.right(90)

window.mainloop()

# 14.3d
for i in range(5):
    t.forward(100)
    t.right(72)

window.mainloop()

# 14.3e
for i in range(6):
    t.forward(100)
    t.right(60)

window.mainloop()

# 14.3f
for i in range(360):
    t.forward(100)
    t.right(1)

window.mainloop()



# 14.4
import turtle

# Create turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=400)  # Set the window size to 600x400 for demonstration

# Create a turtle named "crosshair_turtle"
crosshair_turtle = turtle.Turtle()

# Move the turtle to the starting position for the horizontal line (left edge)
crosshair_turtle.penup()  # Lift the pen to move the turtle without drawing
crosshair_turtle.goto(-300, 0)  # Assuming the middle y-coordinate is 0
crosshair_turtle.pendown()  # Put the pen down to start drawing

# Draw the horizontal line
crosshair_turtle.setx(300)  # Move to the right edge

# Move the turtle to the starting position for the vertical line (top edge)
crosshair_turtle.penup()
crosshair_turtle.goto(0, 200)  # Assuming the center x-coordinate is 0 and top edge y-coordinate is 200
crosshair_turtle.pendown()

# Draw the vertical line
crosshair_turtle.sety(-200)  # Move to the bottom edge

# Hide the turtle after drawing
crosshair_turtle.hideturtle()

# To keep the window open until you close it manually
screen.mainloop()



# 14.5
import turtle
import random

# Create turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle for drawing
draw_turtle = turtle.Turtle()

# Repeat 10 times for 10 random positions
for _ in range(10):
    # Generate random x, y coordinates
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)

    # Move turtle to the random position
    draw_turtle.penup()
    draw_turtle.goto(x, y)
    draw_turtle.pendown()

    # Draw a small square
    for i in range(4):
        draw_turtle.forward(5)
        draw_turtle.right(90)

    # Display the x and y coordinates next to the circle
    draw_turtle.penup()
    draw_turtle.goto(x, y - 40)  # Adjust position for text to not overlap the circle
    draw_turtle.write(f"({x}, {y})", align="center")

    # Move back to the circle to continue the loop
    draw_turtle.goto(x, y)

# Hide the turtle after drawing
draw_turtle.hideturtle()

# Keep the window open until it is manually closed
screen.mainloop()



# 14.6
import turtle

# Create turtle screen
screen = turtle.Screen()
screen.setup(width=400, height=400)

# Create a turtle for drawing
perimeter_turtle = turtle.Turtle()

# Define screen boundary limits
x_limit = 150
y_limit = 150

# Move the turtle to the starting position
perimeter_turtle.penup()
perimeter_turtle.goto(-x_limit, -y_limit)
perimeter_turtle.pendown()

# Moving the turtle around the perimeter
while True:
    # Move forward along the bottom edge
    while perimeter_turtle.xcor() < x_limit:
        perimeter_turtle.forward(1)
    # Turn and move up the right edge
    perimeter_turtle.left(90)
    while perimeter_turtle.ycor() < y_limit:
        perimeter_turtle.forward(1)
    # Turn and move left along the top edge
    perimeter_turtle.left(90)
    while perimeter_turtle.xcor() > -x_limit:
        perimeter_turtle.forward(1)
    # Turn and move down the left edge
    perimeter_turtle.left(90)
    while perimeter_turtle.ycor() > -y_limit:
        perimeter_turtle.forward(1)
    perimeter_turtle.left(90)  # Prepare for next iteration, if any

# Hide the turtle after drawing
perimeter_turtle.hideturtle()

# Keep the window open until it is manually closed
screen.mainloop()
