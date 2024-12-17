# Lesson 13 - Lists

# Recap 1: ATM Simulator
Using 'while' loop and 'if' conditions, create a program to
simulate an ATM. Users of your ATM must be able to withdraw,
deposit, and check balance.

1. The user starts with an account balance of $1000
2. Using a 'while' loop, the program should repeatedly ask the user
   to choose between "Withdraw", "Deposit", "Check Balance", and
   "Exit" options.
3. If the user chooses "Withdraw":
    a.  Ask the user for the amount to withdraw.
    b.  Check if the balance is sufficient. If it is, deduct the
        amount from the balance and display a success message along
        with the remaining balance.
    c.  If the balance is not sufficient, display an error message.
4. If the user chooses "Deposit":
    a.  Ask for the amount to deposit.
    b.  Add the amount to the balance and display the updated balance.
5. If the user chooses "Check Balance":
    a.  Display the current balance.
6. The program should continue running (asking these options) until
   the user chooses the "Exit" option.

-------------------------------------------------------------------

# Task 1: List of groceries
**Task 1a**:
Create a list of 8 groceries you need to buy:
1. Apples
2. Bread
3. Carrots
4. Dates
5. Eggs
6. Flour
7. Grapes
8. Honey

**Task 1b**:
You have decided to get "Herbs" instead of "Honey".
Rename "Honey" to "Herbs"

**Task 1c**:
1. You have just ran out of Ice. Add "Ice" into the list.
2. Insert "Bananas" between "Apples" and "Bread".

**Task 1d**:
You no longer want any bread. Delete "Bread" from the list.

-------------------------------------------------------------------

# Task 2: List of groceries (part 2)
1. Use a 'for' loop and print out all the groceries on your list
2. If grocery == "Apples", print "<grocery name>: I need 5 of these"
3. If grocery == "Carrots", print "<grocery name>: I need 3 of
   these"
4. If name == "Grapes", print "<grocery name>: Get the FarmFresh
   brand"

-------------------------------------------------------------------

# Task 3: Grocery shopping
Write a program to keep track of the groceries you have placed
into the basket.

1. Use a 'while' loop to ask "What item have you added to your
   basket?"
2. Add the grocery into a list.
3. If the user types "end", exit the loop
4. Print all the groceries in the list in this format:
    a. "I have bought Apples"
    b. "I have bought Bananas"
    c. "I have bought Carrots"
    d. etc...

-------------------------------------------------------------------

# Task 4: Online Catalogue
**Task 4a**:
Write a program to create an online catalogue for a grocery store.

1. Using a 'while' loop, ask the user (grocery store manager) to
   input the items their online catalogue should have.
3. Add each item into the catalogue list
4. End the loop when the user types "end"

**Task 4b**:
Based on the list created by the grocery store manager, do the
following:

1. Imagine a customer browsing the website of the grocery store.
   Ask the customer: "What are you looking for?"
2. If the item is in the list, say "Yes we sell that."
3. Else, say "Sorry, we don't have that."

-------------------------------------------------------------------

# Task 5: Lucky draw number generator
Create a lucky draw number generator that generates 10 numbers
between 1 to 9999.

1. Import the 'random' library
2. Using the 'random.randint()' function and a 'for' loop, add 10
   random numbers into a list
3. Using another loop, announce the winners in the following format:
    a. Winner #1: 5426
    b. Winner #2: 3241
    c. Etc...

-------------------------------------------------------------------

# Task 6: Pizza Topping
Create a program that asks the user what pizza topping they want

1. Create a list of pizza toppings
2. Print out the list of pizza toppings with an index number next
   to each of them in this format:
    "1. Mushrooms"
    "2. Pepperoni"
    "3. Pineapple"
    ...
3. In a 'while' loop, ask the user which pizza topping they want
   (By index)
4. Exit the 'while' loop only when the user enters "end"
5. Print the toppings that the user has selected