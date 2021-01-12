# Family Name: JuanPablo Sanchez
# Student Number: 
# Course: ITI 1120
# Assignment Number 2
# Due October 2, 2020

import math
import random


def elementary_school_quiz(flag, n):
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2
    '''(number, number) -> (number)
    Creates a randomly generated quiz can either be a quiz on subtraciton or exponentiation.
    Precondition: flag is 0 or 1, n is 1 or 2
    Post: A integer representing the number of questions correct are returned.
    '''

    number_correct = 0
    #Variable that holds the number of correct responses by the user.

    if flag == 0: #When 0 it is the substraction quiz.

        #Loop that creates the number of problems based on the number of n given.
        for i in range(n):
            #Two randomly generated integers are created.
            value_one = int(random.uniform(1,10)) #Theses values range from 1 - 9
            value_two = int(random.uniform(1,10))

            print ("Question", i+1)
            #\u002D is the unicode number for the subraction symbol.
            answer = int(input("What is the result of " + str(value_one) + "\u002D" + str(value_two) + "? "))

            correct = value_one - value_two
            #Calculates the correct value that is needed to compared against the number given from user.

            #When the number given from the user is the same.
            if correct == answer:
                number_correct +=1
                #No number is added if the user got the question wrong.

    if flag == 1: #When 1 it is the exponentiation quiz.

        #Loo that creates the number of problems based on the number of n given.
        for i in range(n):
            #Two randomly generated integers are created.
            value_one = int(random.uniform(1,10)) #Theses values range from 1 - 9
            value_two = int(random.uniform(1,10))
                      
            print ("Question", i+1)
            answer = int(input("What is the result of " + str(value_one) + "\u005E" + str(value_two) +"? "))

            correct = value_one**value_two
            #Calculates the correct value that is needed to compare against the number given from user.

            #When the number given from the user is the same.
            if correct == answer:
                number_correct +=1
                #No number is added if the user got the qustion wrong.

    #Returns the a value that represents the number of answer that the user got correct.
    return number_correct


def high_school_quiz(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    '''(number,number,number)->None
    Is a quadratic equation solver that prints all roots of the given values.
    Precondition: All values are given.
    Post: Solutions for the roots are printed.
    '''

    #This is to calculate the discriminant.
    discriminant = (b**2)-4*a*c

    #If the function given is a non-quadratic or constant.
    if a == 0 and discriminant != 0:

        #Calculates the possble roots of the linear function.
        root = (c*-1)/b
        print("The linear equation %s\u00B7x + %s = 0" % (b,c))
        #The %s is string format.
        #\u00B7 is the unicode character number of the multiplication symbol.
        print("has the following real roots: " + str(root))

    #When the discrimiant produces real roots.
    elif discriminant > 0:

        #Calculates the positive version of the quadratic equation.
        positive = ((b*-1)+(math.sqrt(discriminant)))/(2*a)

        #Calculates the negative version of the quadratic equation.
        negative = ((b*-1)-(math.sqrt(discriminant)))/(2*a)

        print("The quadratic equation %s\u00B7x^2 + %s\u00B7x + %s = 0" %(a,b,c))
        print("has the following real roots: ")
        print(positive, "and", negative)

    #When the discrimiant produces complex roots.
    elif discriminant < 0:

        #Taking the squared root of a number is not allowed, the discriminant needs to be changed to a positive value.
        squared_discrim = ((math.sqrt(discriminant*-1))/(2*a))

        #To the value b in the equadratic formula since it is producing a complex root it is not possible to subtract from that value.
        infront = (b*-1)/(2*a)

        #%s is more formating strings.
        print("The quadratic equation %s\u00B7x^2 + %s\u00B7x + %s = 0" %(a,b,c))
        print("has the following two complex roots: ")
        print("%s + i %s\n and\n%s - i %s" %(infront,squared_discrim,infront,squared_discrim))

    #When the function given has a "a" and "b" values are 0
    elif discriminant == 0 and a ==0:
        if c == 0: #When all of the values of "a" and "b" and "c" are equal to 0
            print("The quadratic equation %s\u00B7x + %s = 0" %(b,c))
            print("is satisfied for all numbers x")
        else: ##When all of the values of "a" and "b" are equal to 0 but not c is equal to 0
            print("The quadratic equation %s\u00B7x + %s = 0" %(b,c))
            print("is satisfied for no numbers x")


# main

# your code for the welcome tmessage goes here

print("*"*41)
print("*" + (' '*39) + "*")
print("*" + " __Welcome to my math quiz-generator__ " + "*")
print("*" + (' '*39) + "*")
print("*"*41)

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")


if status=='1': 
    # your code goes here

    #Handles the elementary school response.
    title = "__" + name + ", welcome to my quiz-generator for elementary school students.__ "

    #Welcome message
    print("*" * (len(title)+2))
    print("*" + (" " *(len(title)) + "*"))
    print("*" + title + "*")
    print("*" + (" " *(len(title)) + "*"))
    print("*" * (len(title)+2))
    
    subject =  int(input(name + " what would you like to practice? Enter \n0 for subtraction\n1 for exponentitation "))
    #If the user does not enter an integer the program will crash.

    #When subject value is in range of the accepted values of the question.
    if subject == 0 or subject == 1: 
        questions = int(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))
        #If the user does not enter an integer the program will crash.

        #When the number of questions are in the accepted values of the question.
        if questions == 1 or questions ==2:

            #Call to a function elementary school quiz
            grade = elementary_school_quiz(subject, questions)

            if grade == questions: #When the user gets all of the questions correct
                print("Congradulations " + name + "! You'll probably get an A tomorrow.")
            elif (grade - questions) == 1: #When the user gets half of the quesions correct
                print("You did ok" + name + ", but I know you can do better.")
            else: #When the user does not get any question correct
                print("I think you need some more pratice " + name + ".")

        elif questions == 0: #When the user inputs "0" when asked the number of question is asked.
            print("Zero questions. OK. Good bye")
            pass
        else: #When the user inputs a value that is not in the range of the expected values.
            print("Only 0, 1 or 2 are valid choices for the number of questions.")
            pass

    else: #When the user inputs a value that is not in the range of the expected values.
        print("Invalid choice. Only 0 or 1 is accpeted.") 
        pass
    

elif status=='2':

    # your code for welcome message

    #Handles the Highschool response.
    quadratic_title = "__quadratic equation, a\u00B7x^2 + b\u00B7x + c = 0, solver for " + name + "__"

    #Welcome message
    print("*" * (len(quadratic_title)+2))
    print("*" + (" " *(len(quadratic_title)) + "*"))
    print("*" + quadratic_title + "*")
    print("*" + (" " *(len(quadratic_title)) + "*"))
    print("*" * (len(quadratic_title)+2))
    
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here

        #Converts the string into lower to handle the various forms of "yes"
        question = question.lower()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered

            #Asks the user for the numbers that represents the coefficients.
            a = float(input("Enter a number the coefficient a: "))
            b = float(input("Enter a number the coefficient b: "))
            c = float(input("Enter a number the coefficient c: "))
            #When nonfloat values are given the program will crash.

            #Calls the Highschool quiz and sends all of the values by the user to the function.
            high_school_quiz(a, b, c)

        
else:
    # your code goes here
    #When the the user does not input a number or character(s) in the range of the question of what level of schooling that they are in.
    print(name + " you are not a target audience for this software")
    pass

print("Good bye "+name+"!")
