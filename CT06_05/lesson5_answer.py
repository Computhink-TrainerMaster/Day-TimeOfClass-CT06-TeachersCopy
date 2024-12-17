# 5.Recap1
name = input("What is your friend's name? ")
age = int(input("How old will they be turning this year? "))
message = input("What message would you like to write to them? ")

print("Happy " + str(age) + "th birthday " + name + "! " + message)



# 5.1
user_name = input("What is your name? ")
for i in user_name:
    print("Give me a " + i + "!")
print("What do we have?")
print(user_name + " is the best!")



# 5.2
for i in range(100):
    print("I like chicken rice.")



# 5.3
for i in range(100):
    print("I like cake.")
    print("Give me more")



# 5.4
for i in range(60):
    print(i)



# 5.5a
for i in range(1, 6):
    print(i)

# 5.5b
for i in range(51, 101):
    print(i)

# 5.5c
for i in range(18, 30):
    print(i)



# 5.6a
for i in range(2, 25, 2):
    print(i)
    
# 5.6b
for i in range(8, 97, 8):
    print(i)
    
# 5.6c
for i in range(5, 0, -1):
    print(i)



# 5.7a
print("Ready!")
for i in range(3, 0, -1):
    print(i)
    
# 5.7b
for i in range(10, 0, -1):
    print(i)
print("Boo!")



# 5.8
start = int(input("What number would you like to start counting from? "))
stop = int(input("What number would you like to count until? "))

if start < stop:
    for i in range(start, stop + 1):
        print(i)
else:
    for i in range(start, stop - 1, -1):
        print(i)



# 5.9
num = 0

for i in range(10):
    num = num + i
    print(num)