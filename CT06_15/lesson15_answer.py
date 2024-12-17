# 15.Recap1a (window setup)
import turtle

window = turtle.Screen()
window.setup(width=200, height=200)

# 15.Recap1b (turtle setup)
artist = turtle.Turtle()
artist.shape("arrow")
artist.color("blue")  # Change as needed for each shape

# 15.Recap1c (drawing)
artist.penup()
artist.goto(0, 0)

artist.seth(90)
artist.pendown()
artist.forward(60)
artist.right(90)
for _ in range(360):
    artist.forward(1)
    artist.right(1)

# 15.Recap1d (print the turtle's position)
print("Current turtle position: " + str(artist.xcor()) + ", " + str(artist.ycor()))

window.mainloop()



# 15.1
# Get the name of the stranger/friend
name = input("What is your name? ")

# Switch case to display appropriate greeting.
if name == "Ethan":
    print("Hi " + name + ". How are you?")
elif name == "Ben":
    print("Hi there!")
    print("My name is Freddo")
    print("I like to swim and eat chicken wings!")
    print("Nice to meet you!")
elif name == "Gracie":
    print("Hi there!")
    print("My name is Freddo")
    print("I like to swim and eat chicken wings!")
    print("Nice to meet you!")
elif name == "Javior":
    print("Hi there!")
    print("My name is Freddo")
    print("I like to swim and eat chicken wings!")
    print("Nice to meet you!")
else:
    print("I don't think you belong here...")



# 15.2
import turtle

# Initialize the turtle
t = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()

num_box = 6

def draw_square():
    for _ in range(4):
        t.forward(20)
        t.left(90)

for i in range(3):
    for _ in range(num_box):
        t.pendown()
        draw_square()
        t.penup()
        t.forward(25)  # Move to the position for the next square

    for _ in range(num_box):
        t.backward(25)

    t.sety(t.ycor() - 25)
    t.setx(t.xcor() + 25)

    num_box -= 2

# Hide the turtle and finish
screen.mainloop()



# 15.3
# Global variable
counter = 0

def increment_counter():
    global counter  # Declare counter as global to modify it
    counter += 1

# Call the function multiple times and print the global variable
increment_counter()
increment_counter()
increment_counter()
print("Counter value:", counter)  # Should print "Counter value: 2"



# 15.4
import turtle

screen = turtle.Screen()
screen.setup(width=400, height=400)

square = turtle.Turtle()

def draw_square(size):
    square.penup()
    square.goto(0, 0)
    square.seth(180)
    for i in range(2):
        square.forward(size/2)
        square.right(90)
    square.pendown()
    for i in range(4):
        square.forward(size)
        square.right(90)

for i in range(50, 351, 50):
    draw_square(i)

screen.mainloop()



# 15.5
def doubleNumber(num):
    return int(num)*2

print(doubleNumber(5)) #Testing it out



# 15.6
def greet(name):
    greeting = "Hello there " + name + "!"
    return greeting

user_name = input("What is your name? ")
print(greet(user_name))



# 15.7
def isEven(number):
    return number % 2 == 0

# List of numbers to test
numbers = [3, 9, 2, 8, 5, 4]

# Loop through the list and print whether each number is even or odd
for num in numbers:
    if isEven(num):
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")



# 15.8
def ageGroup(age):
    if age < 13:
        return "Child"
    elif age < 21:
        return "Teen"
    elif age < 54:
        return "Adult"
    else:
        return "Senior"

# Test the function with different ages
print(age_group(10))  # Should return 'Child'
print(age_group(15))  # Should return 'Teen'
print(age_group(30))  # Should return 'Adult'
print(age_group(70))  # Should return 'Senior'



# 15.9a
def square(number):
    return number * number

# 15.9b
def sum_of_squares(x, y):
    return square(x) + square(y)  # Calls the square function for each argument

# Example of calling the outer function
print(sum_of_squares(3, 4))
