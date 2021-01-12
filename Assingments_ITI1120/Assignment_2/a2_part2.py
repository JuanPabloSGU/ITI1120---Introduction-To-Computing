# Family Name: JuanPablo Sanchez
# Student Number: 
# Course: ITI 1120
# Assignment Number 2
# Due October 2, 2020

###############
# Question 1 #
###############

def min_enclosing_rectangle(radius,x,y):
    '''(number,number,number)->(number,number)
    A rectangle that contains a circle and determine the position of the bottom-left corner coordinates
    Precondition: All values given are real numbers.
    Post: Coordinates are returned.
    '''

    if(radius>0): #Radius is greater than 0
        xfinal = x-radius
        yfinal = y-radius

        return(xfinal,yfinal)
    else: #Radius is less than 0
        return None

###############
# Question 2 #
###############

def vote_percentage(results):
    '''(str)->(number)
    Finds the percentage of votes are "yes".
    Precondition: Results has mulitple string values.
    Post : A integer is returned.
    '''

    #To make every input a lower case string.
    results = results.lower()
    
    #Counts the number of times "yes" is in given string.
    agree = results.count('yes')
    non_agree = results.count('no')

    #Finds the percenage of "yes" are in the given data.
    percentage = (agree/(agree+non_agree)) 

    return percentage
    
###############
# Question 3 #
###############

def vote():
    '''()->none
    Asks the user for all of the votes and presents the outcome of the proposal.
    Preconditon: none.
    Post : Print statments are returned.
    '''

    #Asks the user for a string input
    vote = input("Enter the yes, no, abstained voes one by one and then press enter: ")

    #Calls the function vote_percentage to calculate the percentage of "yes"
    percentage = vote_percentage(vote)

    #All votes are yes
    if(percentage == 1):
        print("Proposal passes unanimously")

    #2/3 votes are yes
    elif(percentage >= (2/3)):
        print("Proposal passes with super majority")

    #1/2 votes are yes
    elif(percentage >= (1/2)):
        print("Proposal passes with simple majority")

    #Not enough votes to be greater than 50 percent
    else:
        print("Proposal fails")

    
    

    

    
