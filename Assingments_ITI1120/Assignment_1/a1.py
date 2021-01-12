# JuanPablo Sanchez
# Student number: 300173810
# Assignment Number 1
# year 2020

import turtle
from math import *

###############
# Question 1
###############

def f_to_k(t):
    '''(number)->number
    Returns the converted temperature from Fahrenheit expressed in degrees Kelvin.
    Precondition: Temperature in Fahrenheit is given.
    Post : Temperature expressed in degrees Kevlin is returned.
    '''

    # Forumal to Convert Fahrenheit -> Celsius -> Kelvin.
    temp = ((t-32)* 5/9) + 273.15
    return temp

###############
# Question 2
###############

def poem_generator():
    '''()->none
    Prints a personalized poem that includes the name and city of birth of user.
    Precondition: none.
    Post : Prints the personalized poem.
    '''
    #User inputs data.
    name = input("Enter your name: ")
    city_of_birth = input("Enter your city of birth: ")

    #Prints the personalized poem.
    print("Everyday " + name + " woke up")
    print("Stayed up until the sun went down")
    print("Watched the days in " + city_of_birth + " go by")
    print("Everyday " + name + " woke up")

###############
# Question 3
###############

def impl2loz(w):
    '''(number) ->(number,number)
    Returns a pair of number such that w = l + o/16.
    Precondition: A non-negative number is given.
    Post : A solution which includes two pairs of unique integers.
    '''
    x = floor(w) #Removes the decimal point from w.
    diff = w-x #Is the difference between x and w.
    o = diff*16 # o < 16 has to be true which means that x < 16.
    l = x

    return(l,o)

###############
# Question 4
###############

def pale(n):
    '''(number)->(boolean)
    Determines if a number is a pale number. Meaning at least two consecutive digits each equal to 3.
    Or if the last digit is divisible.
    Precondition: A positive integer that has four digits.
    Post: A boolean is returned.
    '''
    position_one = (floor(n//1000)%10)
    position_two = (floor(n//100)%10)
    position_three = (floor(n//10)%10)
    position_four = (n%10)

    consecutive = not((position_one==3 and position_two==3)or(position_two==3 and position_three==3)or(position_three==3 and position_four==3))
    #Compares each position that is equal to 3 and compare if any pair is true
    #Consecutive is true when all pairs don't equal 3
    last_digit = not(position_four%4==0)
    #last_digit is true when is not divisible by 4

    return consecutive and last_digit

###############
# Question 5
###############
    
def bibformat(author, title, city, publisher, year = 0):
    '''(str,str,str,str,number)->(str)
    Determines the MLA format of a book.
    Precondition: Four strings and one int is given.
    Post : A string is returned.
    '''
    form = (author + " ("+ str(year) + "). " + title + ". " + city + ": " + publisher + ".")
    return form
    
###############
# Question 6
###############

def bibformat_display():
    '''() ->(function)
    Asks user for information of a book used to create a citation in MLA form.
    Precondition: none.
    Post : Function bibformat is called.
    '''
    book_Title = input("Enter the title of a book: ")
    book_Author = input("Enter the name of the autor? ")
    book_Year = int(input("What year was the book pusblished? "))
    book_Publisher = input("Enter the name of the pusblisher: ")
    book_City = input("In what city are the headquaters of the publisher? ")

    return bibformat(book_Author, book_Title, book_City, book_Publisher, book_Year)

###############
# Question 7
###############

def compound(x,y,z):
    '''(number,number,number)->(boolean)
    Returns a boolean expression if the following statments are both true.
    Precondition: x,y,z are given.
    Post: A boolean expression is returned.
    '''
    even = bool(x%2==0 and y%2!=0 and z%2!=0)
    # Only true if there is no remander.
    maximum = bool(x + y >= 100 or x + z >= 100 or y + z >= 100)
    # Only true if atleast one pair of the three integers adds up to a number greater than 100.
    determine = (even and maximum)

    return determine

################
# Question 8
################

def funct(p):
    '''(number)->(number)
    Solves for r given a formula 5^r^2 - number + 10.
    Precondition: number given is greater than or equal to 11
    Post: A print statement is given.
    '''
    r = sqrt((log(p-10))/(log(5)))#Isolated for r given equation 5^r^2 - p + 10 = 0

    print ("The solution is r: " , r)

################
# Question 9
################

def gol(n):
    '''(number)->(number)
    Returns a minimum number of times that p can be divided by n.
    Precondition: Number is given.
    Post: A integer is returned.
    '''
    p = ceil((log(n))/(log(2)))#Comes from the concept where e^n = log(n) = e

    return p

################
# Question 10
################

def draw_rocket():
    '''()->None
    Draws a rocket.
    Precondition: none
    Post: A poorly drawn rocket is shown.
    '''
    s = turtle.Screen()
    t = turtle.Turtle()

    #Setting the background colour to black to reflect space
    s.bgcolor("black")
    t.pencolor("white")
    t.pensize(7)

    #This for the starts that appear when the rocket is completed
    import random

    t.penup()

    for i in range(100): #For each i interval each x and y position are pseudo randomly generated
        x = random.uniform(-450,450)
        y = random.uniform(-450,450)

        t.goto(x,y)
        #A white dot represents a star in space
        t.dot(3,"white")   

    t.penup()
    #Using the fill function to fill the main of the Rocket
    t.fillcolor("gray")
    t.begin_fill()
    t.goto(-100,-200)
    t.pendown()
    t.goto(100,-200)
    t.left(90)
    t.goto(100,50)
    t.setheading(45)
    t.goto(0,200)
    t.dot(10,"white")
    t.setheading(225)
    t.goto(-100,50)
    t.setheading(270)
    t.goto(-100,-200)
    t.end_fill()

    #This is for the fire part at the bottom of the rocket
    t.pencolor("red")
    t.fillcolor("dark red")
    t.begin_fill()
    t.setheading(300)
    t.forward(50)
    t.setheading(60)
    t.forward(25)
    t.setheading(325)
    t.forward(75)
    t.setheading(35)
    t.forward(75)
    t.setheading(300)
    t.forward(25)
    t.setheading(60)
    t.forward(50)
    t.end_fill()

    #This is the window of the rocket
    t.penup()
    t.pencolor("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.goto(20,50)
    t.pendown()
    t.circle(25)
    t.end_fill()

    #This is the wing on the right
    t.penup()
    t.pencolor("white")
    t.fillcolor("gray")
    t.begin_fill()
    t.goto(100,-200)
    t.pendown()
    t.setheading(300)
    t.forward(100)
    t.setheading(30)
    t.forward(50)
    t.setheading(90)
    t.forward(150)
    t.setheading(130)
    t.forward(145)
    t.end_fill()

    #This is the wing on the left
    t.penup()
    t.pencolor("white")
    t.fillcolor("gray")
    t.begin_fill()
    t.goto(-100,-200)
    t.pendown()
    t.setheading(240)
    t.forward(100)
    t.setheading(140)
    t.forward(50)
    t.setheading(90)
    t.forward(150)
    t.setheading(50)
    t.forward(135)
    t.end_fill()

################
# Question 11
################

def cad_cashier(price,payment):
    '''(number,number)->(number)
    Calculates the the change of a customer should get in Canadian dollars.
    Precondition: Payment is greater than price given.
    Post: A float value is returned representing the change.
    '''

    change = abs(price-payment) 
    digit = round(round(change/0.05)*(0.05), 2)
    #Inside second "round", change/0.05 is to isolate decimals and round to correct sigfigs.
    #First "round" is that the ending of the decmial to the 0.05 value and to only have the solution in the realistic change.

    return digit

################
# Question 12
################

def min_CAD_coins(price,payment):
    '''(number,number)->(number,number,number,number,number)
    Function that shows the amount of change given back to the customer in specific dollar values
    Precondition: Payment is greater than price given.
    Post: Mulitple integers are returned.
    '''

    #Calls a function that calculates the change
    change = cad_cashier(price,payment)
    newChange = ceil(change*100) #Moves the decimal point

    #Finds remander, subtract from original value, then finds the exact amount of the number of times is the remander
    toonies = ((newChange - (newChange%200))/200) 
    newChange = newChange%200 #Reseting the amount to subtract from the initial value

    loonies = ((newChange - (newChange%100))/100)
    newChange = newChange%100
    
    quarters = ((newChange - (newChange%25))/25)
    newChange = newChange%25

    dimes = ((newChange - (newChange%10))/10)
    newChange = newChange%10

    nickels = ((newChange - (newChange%5))/5)

    return int(toonies),int(loonies),int(quarters),int(dimes),int(nickels)
