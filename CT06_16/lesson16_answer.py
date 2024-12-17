# 16.Recap1
def quadrupleNumber(num):
    quadNum = num * 4
    return quadNum

print(quadrupleNumber(105))
print(quadrupleNumber(24))
print(quadrupleNumber(402))
print(quadrupleNumber(594))



# 16.Recap2
import turtle
window = turtle.Screen()
t = turtle.Turtle()

def drawShape(length, num_sides):
    for i in range(num_sides):
        t.forward(length)
        t.right(360/num_sides)

# 16.Recap2a
drawShape(100,4)

window.mainloop()

# 16.Recap2b
drawShape(100,6)

window.mainloop()

# 16.Recap2c
drawShape(100,8)

window.mainloop()



# 16.Recap3
import turtle
window = turtle.Screen()
t = turtle.Turtle()

def drawShape(length, num_sides):
    for i in range(num_sides):
        t.forward(length)
        t.right(360/num_sides)

drawShape(100,4)
t.left(60)
drawShape(100,3)

window.mainloop()



# 16.Recap4
import turtle
window = turtle.Screen()
window.setup(width=600, height=600)
t = turtle.Turtle()
t.penup()

def drawShape(length, num_sides):
    for i in range(num_sides):
        t.forward(length)
        t.right(360/num_sides)

def drawHouse():
    t.pendown()
    drawShape(100,4)
    t.left(60)
    drawShape(100,3)
    t.right(60)
    t.penup()

t.goto(-200, 200)

for i in range(3):
    for i in range(3):
        drawHouse()
        t.forward(150)
    t.right(180)
    t.forward(450)
    t.left(90)
    t.forward(200)
    t.left(90)

window.mainloop()



# We are creating a bouncing ball program and will be
# splitting the program into different functions.

# We will be working on each of the different functions
# separately before putting all of the functions together
# to bring the bouncing ball program to life.



# 16.1 Setting Up the Screen
import turtle

# Returns a window that is screenWidth x screenHeight
def setup_screen(screenWidth, screenHeight):
    screen = turtle.Screen()
    screen.setup(width=screenWidth, height=screenHeight)
    return screen

# Setup code
screenWidth = 300
screenHeight = 500
screen = setup_screen(screenWidth, screenHeight)

# Keeps window open
screen.mainloop()



# 16.2 Creating a turtle object
# (Existing code)

# Existing code to create setup_screen function

# Returns a blue circle turtle object
def create_blue_ball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("blue")
    ball.penup()
    return ball

# Setup code
screenWidth = 300 # Existing code
screenHeight = 500 # Existing code
screen = setup_screen(screenWidth, screenHeight) # Existing code
ball = create_blue_ball() 

# Keeps window open
screen.mainloop() # Existing code



# 16.3 Moving the turtle
# (Existing code)

# Existing code to create create_ball function

# Moves 'ball' turtle object by 'dx' and 'dy'
def move_ball(ball, dx, dy):
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)

# Setup code
dx = 2
dy = 2

# Main loop
while True:
    move_ball(ball, dx, dy)

# (Existing code)



# 16.4a Detecting edges (y-axis)
# (Existing code)

# Existing code to create move_ball function

# Checking for border (x-axis)
def check_x(ball, screenWidth):
    if ball.xcor() > (screenWidth/2) or ball.xcor() < (-screenWidth/2):
        return True

# Setup code
...
dx = 2 # Existing code
dy = 2 # Existing code
...
# Main loop
while True:
    move_ball(ball, dx, dy) # Existing code
    if check_x(ball, screenWidth):
        dx *= -1


        
# 16.4b Detecting edges (y-axis)
# (Existing code)

# Existing code to create check_x function

# Checking for border (y-axis)
def check_y(ball, screenHeight):
    if ball.ycor() > (screenHeight/2) or ball.ycor() < (-screenHeight/2):
        return True

# Setup code
...
dx = 2 # Existing code
dy = 2 # Existing code
...
# Main loop
while True:
    move_ball(ball, dx, dy) # Existing code
    if check_x(ball, screenWidth): # Existing code
        dx *= -1 # Existing code
    if check_y(ball, screenHeight):
        dy *= -1