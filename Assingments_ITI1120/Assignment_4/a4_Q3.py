# Family Name: JuanPablo Sanchez
# Student Number:
# Course: ITI 1120
# Assignment Number 4
# Due November 2, 2020

def longest_run(l):
    '''(list)->int
    Takes a list of number and returns the number of consecutive repeated values in the list.
    Precondition: A list is given
    Post: A integer is returned
    '''

    if len(l) < 1: #To test if the length is 0 meaning that there is no possiblity for repeative values.
        return 0

    if len(l) == 1: 
        return 1 #Since the values only appears once means that it repeates only once.

    targetnum = l[0] #represent the value that we are compairing to. 
    count = 1 #Count the number of times the value is consequtive and repeating
    total = [0] #List to store the number of times it is consequtive and repeating.

    for i in range(len(l)-1):
        if l[i] == l[i+1]:

            #To compare if the consequtive num is the same as the next num
            if targetnum == l[i]:
                targetnum = l[i] 
                count += 1 #Add to the counter
                
            else:
                total.append(count)
                #Add to the list to keep the previous target's number count to use to compare the max length.

                targetnum = l[i]
                count = 2 #Since we find a consequtive num we add 2 as we start at 1 and add 1 since we found one.

    #If we come to the end of the list and we haven't found a new target num we check the counter to see if the it is the largets run of consequtive number.
    if count > max(total):
        return count
    else:
        return max(total)
            
#main
list_numbers = input("Please input a list of numbers separated by spaces: ").strip().split()

for i in range(len(list_numbers)):
    #Since the user can input numbers which means we have to account for float values to be consecutive repeated values.
    list_numbers[i] = float(list_numbers[i])
    #Converting the entire list to a float allows us to not have a false counter total.

print(longest_run(list_numbers))
