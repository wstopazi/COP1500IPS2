#  Scott Topazi
#  A brief demonstration on parameter passing functions from Sprint 2.
#  The beginnings of a searchable database of concert information.
#  A brief explanation of the different kinds of operators from Sprint 1.

from tinydb import TinyDB, Query  # Start by importing the 'books' we need from the tinydb library to interact and manipulate data within the database.

import math

db = TinyDB('musicdatabase.json')  # We've created a blank database or uploaded an existing database called TinyDB and have assigned it to store its data in a .json file.


def triangleArea(a, b, c):
    halfParameterS = 0.5 * (a + b + c)
    radicandArea = halfParameterS * (halfParameterS - a) * (halfParameterS - b) * (halfParameterS - c)
    squareRootArea = math.sqrt(radicandArea)
    return(squareRootArea)


sideA = int(input("Enter the length of side a: "))
sideB = int(input("Enter the length of side b: "))
sideC = int(input("Enter the length of side c: "))

print("The area of this triangle is", triangleArea(sideA, sideB, sideC))


def listOfItems(category):  # Defining a function to list all items from the various search queries throughout the program with a parameter of category.
    for item in category:
        print(item)


listOfItems(db)  # Recalling a function to list all items within the database.

print('\n')

#  def insert():
#      ID = input("Enter ID: ")
#      dateStr = input("Enter full date: ")
#      typeStr = input("Enter the type of concert: ")
#      insertStr = "{'ID': '" + ID + "', 'date': '" + dateStr + "', 'type': '" + typeStr +"'}"
#      print(insertStr)
#      db.insert(insertStr)
#
#  insert()

Concert = Query()  # Assigning our search Query 'book' to the variable Concert.

print("1) Date", "2) Type", "3) Name", sep='\n')  # Listing the first set of options separated by a line feed carriage return.
doAgain = True  # Setting up a condition to test throughout the coming while loop.
answer1 = input("By which of the following categories would you like to search our concerts? ")
print('\n')
while doAgain:  # Initiating a while loop with the condition assigned earlier. Loop will continue as long as the condition is met.
    if answer1 == "1":
        concertDate = input("Please enter the date in the following format: mmddyy ")
        resultsDate = db.search(Concert.ID == concertDate)  # Performing a search within the database using the input from the concertDate variable. This particular date format is actually found in the ID category.
        print('\n')
        listOfItems(resultsDate)  # Recalling a function to list items found in resultsDate.
        doAgain = False  # This will break the condition of the loop, thus stopping and jumping to the end of the loop.
    elif answer1 == "2":
        print("a) Large Ensemble", "b) Nisita Concert Series", "c) Recital Class", "d) Junior Recital", "e) Senior Recital", sep='\n')  # Option 2, presents another list of options, all listed separated by a line feed carriage return.
        answerType = input("By which of the following types would you like to search our concerts? ")
        doTypeAgain = True  # Setting up a condition for a new while loop inside of the main while loop.
        while doTypeAgain:  # Initiating a while loop with the condition assigned in the previous line. This loop will continue as long as this condition is met.
            if answerType == "a":
                resultsType = db.search(Concert.type == "Large Ensemble")  # Performing a search within the database using the input from the answerType variable which in this case is 'a' being linked to Large Ensemble.
                print('\n')
                listOfItems(resultsType)  # Recalling a function to list items found in resultsType. In this case, Large Ensemble.
                doTypeAgain = False  # This will break the condition of this inside loop, thus stopping and jumping to the end of this loop.
            elif answerType == "b":
                resultsType = db.search(Concert.type == "Nisita Concert Series")  # Performing a search within the database using the input from the answerType variable which in this case is 'b' being linked to Nisita Concert Series.
                print('\n')
                listOfItems(resultsType)  # Recalling a function to list items found in resultsType. In this case, Nisita Concert Series.
                doTypeAgain = False  # This will break the condition of this inside loop, thus stopping and jumping to the end of this loop.
            elif answerType == "c":
                resultsType = db.search(Concert.type == "Recital Class")  # Performing a search within the database using the input from the answerType variable which in this case is 'c' being linked to Recital Class.
                print('\n')
                listOfItems(resultsType)  # Recalling a function to list items found in resultsType. In this case, Recital Class.
                doTypeAgain = False  # This will break the condition of this inside loop, thus stopping and jumping to the end of this loop.
            elif answerType == "d":
                resultsType = db.search(Concert.type == "Junior Recital")  # Performing a search within the database using the input from the answerType variable which in this case is 'd' being linked to Junior Recital.
                print('\n')
                listOfItems(resultsType)  # Recalling a function to list items found in resultsType. In this case, Junior Recital.
                doTypeAgain = False  # This will break the condition of this inside loop, thus stopping and jumping to the end of this loop.
            elif answerType == "e":
                resultsType = db.search(Concert.type == "Senior Recital")  # Performing a search within the database using the input from the answerType variable which in this case is 'e' being linked to Senior Recital.
                print('\n')
                listOfItems(resultsType)  # Recalling a function to list items found in resultsType. In this case, Senior Recital.
                doTypeAgain = False  # This will break the condition of this inside loop, thus stopping and jumping to the end of this loop.
            else:
                answerType = input("Invalid entry...please enter a valid entry: ")
                doTypeAgain = True  # Loop condition is met which means the loop will continue until a valid entry is entered. This marks the end of this inside loop.
        doAgain = False  # This will break the condition of the main while loop, thus stopping and jumping to the end of the loop.
    elif answer1 == "3":
        answerName = input("Enter the name of the concert you would wish to find. ")
        resultsName = db.search(Concert.name == answerName)  # Performing a search within the database using the input from the answer1 variable which in this case is '3' being linked to the name category.
        print('\n')
        listOfItems(resultsName)  # Recalling a function to list items found in resultsName.
        doAgain = False  # This will break the condition of the main while loop, thus stopping and jumping to the end of the loop.
    else:
        if answer1 != range(1, 4):  # If the user input does not equal the range from 1 to 4 (1, 2, 3), the user will be prompted to enter a valid entry.
            answer1 = input("Please enter a valid entry: ")
            doAgain = True  # The loop condition is met, so the loop will continue until a valid entry has been entered.
print('\n')
doPerformerAgain = True  # Setting up a condition to be met for the while loop up ahead.
answer2 = input("Would you like to search a specific performer? y for yes, any other key for no: ")
print('\n')
while doPerformerAgain:  # Initiating a while loop with the condition assigned a few lines earlier. This loop will continue as long as this condition is met.# Initiating the loop
    if answer2 == "y":
        answerPerformers = input("Enter the last name of the performer you would like to look up. ")
        print('\n')
        resultsPerformers = db.search(Concert.performers.any(answerPerformers))  # Performing a search within the database using the input from the answerPerformers variable. This is set up so that if the input matches ANY indices within the performers category over all items, those items will be sorted out.
        listOfItems(resultsPerformers)  # Recalling a function to list items found in resultsPerformers.
        doPerformerAgain = False  # This will break the condition of the loop, thus stopping and jumping to the end of the loop.
    else:
        if not(answer2 == "y"):
            doPerformerAgain = False  # This still breaks the condition of the loop, but the user is shown an additional message instead of just the last one.
            print("I hope this program was helpful!")
print('\n')
print("Thank you for using this program!")
print('\n')
# An explanation of the exponent operator **

print("Next, we'll look at some commonly used numeric operators.\n")
print("First up is the exponent operator: ** .")
print("This operator will raise the first integer to the power of the second integer.")
print("4 ** 2 =", 4 ** 2)
print("Let's try some numbers of your own.")
powerFirstNum = input("Enter your base number: ")
powerSecNum = input("Enter the exponent in which to raise the base number: ")
print(powerFirstNum + " ** " + powerSecNum + " =", int(powerFirstNum) ** int(powerSecNum))
print("\n")

# An explanation of the multiplication operator *

print("Next, we will take a look at the multiplication operator: * .")
print("This operator will multiply two integers together.")
print("4 * 2 =", 4 * 2)
print("Let's try some numbers of your own again.")
multiFirstNum = input("Enter your first number: ")
multiSecNum = input("Enter your second number: ")
print(multiFirstNum + " * " + multiSecNum + " =", int(multiFirstNum) * int(multiSecNum))
print("\n")

# An explanation how the multiplication operator works with strings

print("Interestingly, the multiplication operator can work with string types as well.")
print("For example, 'Hello World!' * 5 with print Hello World! 5 times, like so:")
print("Hello World!" * 5)
animal = input("What is your favorite animal? ")
qty = input("How many times would you like it to repeat? ")
print(animal * int(qty))
print("\n")

# An explanation of the division operator /

print("Now, we will move on to the division operator: / .")
print("This operator will divide one number by another number.")
print("10 / 5 =", 10 / 5)
print("Enter in some numbers of your own again.")
divFirstNum = input("Enter your first number: ")
divSecNum = input("Enter the number you'd like to divide by: ")
print(divFirstNum + " / " + divSecNum + " =", int(divFirstNum) / int(divSecNum))
print("\n")

# An explanation of the addition (+) and subtraction (-) operators

print("Up next, we'll use two operators: addition (+) and subtraction (-).")
print("Obviously, + will add two numbers and - will subtract one number from another.")
print("3 + 4 =", 3 + 4)
print("4 - 3 =", 4 - 3)
print("Now, enter in a few numbers to add together.")
addFirstNum = input("Enter first number: ")
addSecNum = input("Enter second number: ")
addThirdNum = input("Enter third number: ")
addFinalNum = input("And one more: ")
print(addFirstNum + " + " + addSecNum + " + " + addThirdNum + " + " + addFinalNum + " =", int(addFirstNum) + int(addSecNum) + int(addThirdNum) + int(addFinalNum))
print("\n")

# An explanation how the addition operator works with strings

print("Similar to the multiplication (*) operator, addition (+) can be used on string types as well.")
print("For example, look what happens when we add the two words camp and ground together by running the code 'camp' + 'ground'.")
print("camp" + "ground", "\n")
print("Next, enter two numbers you would like to subtract.")
subFirstNum = input("Enter your first number: ")
subSecNum = input("Enter your second number for which you will subtract: ")
print(subFirstNum + " - " + subSecNum + " =", int(subFirstNum) - int(subSecNum))
print("\n")

# An explanation on the modulus (%) and floor division (//) operators

print("Finally, we'll look at a couple of special operators that are quite useful in accounting and other financial situations.")
print("Those are the modulus (%) and the floor division (//) operators.")
print("There are essentially three parts to a division problem: dividend, divisor, and quotient.")
print("The quotient is the solution to a division problem, but the dividend doesn't always get divided evenly by the divisor, so a remainder is left over. That's where these operators come in handy.")
print("The modulus (%) operator will only give us the remainder portion of the quotient.")
print("For example, try entering in two numbers that will not divide evenly.")
modFirstNum = input("Enter your first number: ")
modSecNum = input("Enter your second number: ")
print(modFirstNum + " % " + modSecNum + " =", int(modFirstNum) % int(modSecNum))
print("\n")
print("On the other hand, the floor division (//) operator will only give us the whole number portion of the quotient.")
print("Try two different numbers that do not divide evenly  and try to guess what you think the answer will be.")
floorFirstNum = input("Enter your first number: ")
floorSecNum = input("Enter your second number: ")
print(floorFirstNum + " // " + floorSecNum + " =", int(floorFirstNum) // int(floorSecNum))
