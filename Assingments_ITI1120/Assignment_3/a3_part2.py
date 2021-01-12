# Family Name: JuanPablo Sanchez
# Student Number:
# Course: ITI 1120
# Assignment Number 3
# Due October 19, 2020

##################################################################
# Question 2.1
###################################################################

def sum_odd_divisors(n):
    '''(number)->(number)
    Calculates the sum of all the positive odd divisors of n.
    Precondition: integer is given.
    Post: An integer is returned.
    '''

    if n == 0:
        return None

    #Counts the amount of times that n can be divisible by 'i'
    counter = 0

    #Sequence of i is 1,3,5... to the n number of times that it can be divisble
    for i in range(1,abs(n)+1,2):
        if n%i == 0:
            counter += i #Adds to the sum

    return counter

##################################################################
# Question 2.2
##################################################################

def series_sum():
    '''()->number
    Calculates the sum of a series of numbers from the formula 1/n^2.
    Precondition: none
    Post: An float is returned.
    '''

    n = int(input("Please enter a non-negative integer: "))
    total = 1000 #Start value
    x = 0
    
    if n<0:
        return None
    else:
        for i in range(1,n+1):
            x = 1/(i**2) #Formula given from question
            total += x #Adds to the sum
        return total

##################################################################
# Question 2.3
##################################################################

def pell(n):
    '''(int)->(number)
    Calculates the nth Pell number
    Precondition: interger is given
    Post: A integer is returned
    '''

    if n == 0:
        return 0
    if n == 1:
        return 1

    value_one = 0 #Condition 1
    value_two = 1 #Condition 2
    value_pell = 0 #Determine the pell number

    if n > 1:
        for i in range(2, n+1):
            #How to calculate a n number of a pell number
            value_pell = 2*value_two + value_one #Pell is twice the pervious number added to the pell number before that.
            value_one = value_two
            value_two = value_pell #To calculate the next pell number by saving the previous pell number
            
        return value_pell

##################################################################
# Question 2.4
##################################################################

def countMembers(s):
    '''(str) -> int
    Counts the number of times that a specific characer that is extraordinary is found in a word/phrase.
    Precondition: String is given and the characters that we need to find are e->j(incluise), F->X(inclusive), "!,\".
    Post: An integer is returned.
    '''

    counter = 0 #Count the number of times the character is found in the given preconditions.
    for found in s:
        if found in ("\efghijFGHIJKLMNOPQRSTUVWX2345,6!"): 
            counter +=1 #Adds to the counter

    return counter

##################################################################
# Question 2.5
##################################################################


def casual_number(s):
    '''(str)->(int)
    Converts an entered string to an integer.
    Precondition: String is given.
    Post: An integer is returned.
    '''

    if s.count("-") > 1: #If there are mulitple negative signs
        return None

    for i in s:
        s = s.replace(",","") #Replaces all of the negative and comma to check if all of the values in side of the phrase are numeric
        negative = s.replace("-","")

    if negative.isnumeric():
        return int(s)
    else:
        return None

##################################################################
# Question 2.6
###################################################################
    
def alienNumbers(phrase):
    '''(str)->(int)
    Calculates the numerical value to the alien transimition.
    Precondition: Characters inside the set {T,y,!,a,N,U} are given.
    Post: An integer is returned.
    '''

    #Counts the amount of times that the value appears in the phrase
    t = phrase.count('T')
    y = phrase.count('y')
    exlimation = phrase.count('!')
    a = phrase.count('a')
    n = phrase.count('N')
    u = phrase.count('U')

    total = (t*1024)+(y*598)+(exlimation*121)+(a*42)+(n*6)+(u*1) #Calculates the total value of the phrase
    
    return total

##################################################################
# Question 2.7
###################################################################

def alienNumbersAgain(phrase):
    '''(str)->(int)
    Calculates the numerical value to the alien transmition again.
    Precondition: Characters inside the set {T,y,!a, N, U} are given.
    Post: An integer is returned.
    '''

    def counting(symbol,value,phrase):

        counter = 0 #Counts the amount of times that the character is found in the 
        
        for i in phrase: 
            if symbol in i: #If we find the character in the phrase
                counter += 1 #Then we add to the counter
                
        return counter*value

    t = counting("T",1024,phrase) 
    y = counting("y",598,phrase)
    exlimation = counting("!",121,phrase)
    a = counting("a",42,phrase)
    n = counting("N",6,phrase)
    u = counting("U",1,phrase)

    total = t + y + exlimation + a + n + u #Adds to the total

    return total

##################################################################
# Question 2.8
###################################################################

        
def encrypt(text):
    '''(str)->(str)
    Encrypts a text by reversing the text and bringing the last and first character and going inward together.
    Precondition: String is given.
    Post: A String is returned.
    '''

    ns = ""
    text = text[::-1] #Reverses the string

    first_position = ""
    last_position = ""

    for i in range(0,len(text)):
        first_position = text[i] #Set to the first position
        last_position = text[len(text)-(i+1)] #Set to the last position of the string

        if first_position != last_position: #To check if the first position equal to the last position
            ns += first_position + last_position #If it isn't then add it the first position to the last position.
            
        elif first_position == last_position: #when the first position is equal to the last position then we add the last string to the total string
            return ns + last_position

        first_postion = ""
        last_position = ""

    return ns[0:len(text)] #To only go to the lenght of the string

##################################################################
# Question 2.9
###################################################################
         
def weaveop(s):
    '''(str)->(str)
    Inserts characters between every pair of consecutive characters in phrase.
    Precondition: String is given
    Post: A String is returned
    '''

    ns = ""
    first = ""
    second = ""

    if len(s)<=1: #Returns the orginial string when the length of the string is one
        return s

    for i in range(len(s)-1):

        if s[i].isalpha() and s[i+1].isalpha(): #To check if the character and the next character are characters usful when we check if the next character is a number
            if s[i].isupper(): #first position check if uppercase
                first = s[i] + 'O'
            else:
                first = s[i] + 'o'

            if s[i+1:i+2].isupper(): #second position check if uppercase
                second = 'P' + s[i+1:i+1]
            else:
                second = 'p' + s[i+1:i+1]
    
            ns += first + second
        else:
            ns += s[i] + "" #When the next character is a number

        if i == len(s)-2: # For odd len of numbers
                ns = ns + s[len(s)-1]

    return ns 

##################################################################
# Question 2.10
###################################################################

def squarefree(s):
    '''(str)->(boolean)
    Check if a word is squarefree which means that the word does not contain the same substring consecutively.
    Precondition: String is given.
    Post: A boolean expersion is returned.

    '''

    def isEqual(c,s):

        if c+c <= len(s):
            
            if s[0:c] == s[c:c+c]:
                return True #if we find the sequence of characters it returns true
            else:
                return isEqual(c, s[c:])#Using recursion to call back the function by taking rid of the first character/characters and then comparing again

        else:
            return False

    
    def checksquare(s):

        c = 1 #Starting the counter at 1 to start at the first character of the string
         
        while True:
            if c <= len(s):
                if isEqual(c,s):
                    return False #not square free
                    break
                else:
                    c+=1 #Adds to the counter to check the next character and the following set of characters

            else:
                return True #square free
                break
                                  
    value = False
    if checksquare(s):#When it is squarefree
        value = checksquare(s[::-1])#To check if the reversal is also squarefree which is only useful if the original word is squarefree

    return value


        
        
        
