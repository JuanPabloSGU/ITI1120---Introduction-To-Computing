# Family Name: JuanPablo Sanchez
# Student Number: 
# Course: ITI 1120
# Assignment Number 4
# Due November 2, 2020

def number_divisble(integers,n):
    '''(list)->None
    Takes a list from the user and prints the number of times that list contains a number that is divisble by a integer given from the user.
    Precondition: List of integers is given, positive integer is given
    Post: A statement is printed.
    '''
    
    counter = 0
    for i in integers:
        if i % n == 0: #The values in the list are divisble by the integer given
            counter += 1
    print("The number of elements divislble by",n,"is",counter)

#main
list_numbers = input("Please input a list of numbers separated by spaces: ").strip().split()
#We assume that the user is going to follow instructions properly


for i in range(len(list_numbers)):
    list_numbers[i] = int(list_numbers[i]) #Input are only supposed to be non-negative integers

#We assume that the user is going to follow instructions properly
divisor = int(input("Please input an integer: "))


number_divisble(list_numbers, divisor) #Calls the function
