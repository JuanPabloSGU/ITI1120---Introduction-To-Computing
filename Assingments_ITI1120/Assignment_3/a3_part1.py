# Family Name: JuanPablo Sanchez
# Student Number: 
# Course: ITI 1120
# Assignment Number 3
# Due October 19, 2020

def is_up_monotone(X, d):
    # Your code for is_up_monotone function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function

    y = int(d) #d value
    length = len(X) 
    remander = len(X)%y
    monotone = True #To see if it is monotone
    
    a = 0 #start position of the string
    z = y #d value therefore our end position
    
    for i in range(len(X)):

        if (len(X)-remander)>z:
            if(is_statement(a,z,X)):
                a += z #add to the counter by the z value
                z = z+z #add to the counter by the z value 
                monotone = True #When the first position is less than the second position
            
            else:
                monotone = False #When the first position is greater than the second position
                break

    final_result(X,d)
    
    if monotone:
        return True
    else:
        return False
    
    
# you can add more function definitions here if you like       

def is_statement(a,z,X):

    a = int(a)
    z = int(z)
    
    string_one = X[a:z] #0->z(inclusive)
    string_two = X[a+z:z+z] #z->z+z(inclusive)
    
    if string_one < string_two: #check if the first is less than the second
        return True #Redo the loop from is_up_monotone
    else:
        return False #No need to check other positons because the first position is greater than second position

def final_result(X,d):
    d = int(d)

    ns = ""
    comma = ""
    
    for i in range(0,len(X)-d+1,d):
        temp = X[i:i+d] #Slice the sign for formating purposes
        ns += temp + ", "

    print(ns[0:len(ns)-2]) #Remove the last 2 positions of the new string to remove the comma and the extra spacing
    
    print()
    

# main
# Your code for the welcome message goes here, instead of name="Vida"

print("*"*41)
print("*" + (' '*39) + "*")
print("*" + " __Welcome to my up-monotone inquiry__ " + "*")
print("*" + (' '*39) + "*")
print("*"*41)

print()

name = input("What is your name? ")
name = name.strip()

title = " __" + name + ", welcome to up-monotone inquiry.__ "

print()
print("*" * (len(title)+2))
print("*" + (" " *(len(title)) + "*"))
print("*" + title + "*")
print("*" + (" " *(len(title)) + "*"))
print("*" * (len(title)+2))

flag=True
full=True

while flag:
    question=input(name+", would you like to test if a number admits an up-monotone split of given size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
    #YOUR CODE GOES HERE. The next line should be elif or else.
    elif question=='yes':
        print("Good choice!")

        integers = input("Enter a positive integer: ") #Asks the user for an input
        integers = integers.strip() #Strip all of the extra spaces
        num_neg = integers.count("-") #Count the number of negative signs in the input
        integers = integers.replace("-","") #Remove all of the negative signs in the input

        if integers.isnumeric(): #Check if the input is a integer, isnumeric() covers character but also float values
            if num_neg < 1 and int(integers) > 0: # Checks if there was a negative number before removal and to see if the number given is greater than 0

                split = input("Input the split. The split has to divide the length of " + integers + " i.e. " + str(len(integers)) + "\n")

                #Follows the same process as for the input for the first number
                split = split.strip()

                num_neg_split = split.count("-")
                split = split.replace("-","")

                if split.isnumeric():

                    if num_neg_split < 1 and int(split) > 0:
                        
                        if len(integers)%int(split) == 0: #To see if it is divisble by each integer
                            if is_up_monotone(integers,split): #Calls the up_monotone function
                                print("The sequnce is up-monotone") #The function returns true then prints
                            else:
                                print("The sequence is not up-monotone") #The function returns false then prints
                        else:
                            print(str(split) + " does not divide " + str(len(integers)) + ". Try again.") #If it does not divide evenlly 
                    else:
                        print("The input has to be a positive integer. Try Again")
                else:
                    print("the input can only contain digits. Try Again")
            else:
                print("The input has to be a positive integer. Try Again")
        else:
            print("The input can only contain digits. Try Again")

    else:
        print("Please enter yes or no. Try Again.") #If the user inputs not a yes or a no
#finally your code goes here too.

#This is for the final statment when the user inputs a "no" it is the same format of the welcome message
secondTitle = " __" + "Good bye "+ name + "!__ "

print("*" * (len(secondTitle)+2))
print("*" + (" " *(len(secondTitle)) + "*"))
print("*" + secondTitle + "*")
print("*" + (" " *(len(secondTitle)) + "*"))
print("*" * (len(secondTitle)+2))
