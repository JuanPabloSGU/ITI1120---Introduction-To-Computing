# Family Name: JuanPablo Sanchez
# Student Number: 
# Course: ITI 1120
# Assignment Number 4
# Due November 2, 2020

def two_length_run(numbers):
    '''(list)->bool
    Finds if there are sequence of consective repeated values in a list.
    Precondition: A list of integers is given.
    Post: A boolean is returned.
    '''

    # To make function efficient to not go into the loop
    if len(numbers) <= 1: 
       return False
    
    consequtive = False
    i = 0

    while i < len(numbers):

        #Test the value next to the origin to see if it consective repeated values.
        if numbers[i-1] == numbers[i]:
            #If we enter the loop we exit as soon as possible because we have found what we are looking for.
            consequtive = True
            return consequtive

        i += 1

    return consequtive

#main
list_numbers = input("Please input a list of numbers separated by spaces: ").strip().split()

for i in range(len(list_numbers)):
    #The user can enter any type of number and is not specific to integers.
    list_numbers[i] = float(list_numbers[i])
    #This is to allow the user to compare the actual number and not a rounded number which could lead to a false positive.

print(two_length_run(list_numbers))
