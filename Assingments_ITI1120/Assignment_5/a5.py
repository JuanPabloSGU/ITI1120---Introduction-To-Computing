# Family Name: JuanPablo Sanchez
# Student Number: 
# Course: ITI 1120
# Assignment Number 4
# Due November 23, 2020

import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]

    # YOUR CODE GOES HERE

    def get_friends(user, list_of_friends):

        '''(int, list) -> list
        Finds the id of the user in a list and takes the value of the column of the id and adds it to a list.
        Precondition: User is an integer, list is given.
        Post: A list is returned.
        '''

        is_assgined = False
        list_of_user_direct_friends = []

        for index in range(len(list_of_friends)):
            if user == int(list_of_friends[index][0]):
                list_of_user_direct_friends.append(int(list_of_friends[index][1]))
                is_assgined = True

            else:
                #When we find a user that is different then we return the list
                if is_assgined: 
                    break

        return list_of_user_direct_friends
        
    def get_indirect_friends(user, list_of_friends):
        '''(int, list)->list
        Finds the indirect users by comparing the column selection of the list to the given user id.
        Precondition: User is an integer, list is given.
        Post: A list is returned.
        '''

        #This is the same function as get_friends but instead of looking for the first column we search the second column
        
        is_assgined = False
        list_of_user_direct_friends = []

        for index in range(len(list_of_friends)):
            if user == int(list_of_friends[index][1]):
                list_of_user_direct_friends.append(int(list_of_friends[index][0]))
                is_assgined = True

            else:
                if is_assgined:
                    break

        return list_of_user_direct_friends

    def unique_identifiers(list_of_friends):
        '''(list)->(list)
        Checks in a list if there are integers are unique meaning that if in a list the values are unique.
        Precondition: List is given.
        Post: A list is returned.
        '''
        
        list_of_unique_id = []

        for elements in range(1,len(list_of_friends)):

            #To see if the element is in the new created list
            if list_of_friends[elements][0] not in list_of_unique_id:
                list_of_unique_id.append(list_of_friends[elements][0])

            if list_of_friends[elements][1] not in list_of_unique_id:
                list_of_unique_id.append(list_of_friends[elements][1])

        return list_of_unique_id
                
    list_of_friends = []
    for index in friends:
        list_of_friends.append(index.split())
        #Created a new list that contains the elements in the friends.

    #The value at the top of the textfile refers to the unique number of id's
    total_number_of_users = int(friends[0])

    #Since we don't want to input the top value we slice the list
    list_of_friends = list_of_friends[1::]


    #Converting the string of list to a int of list
    for i in range(len(list_of_friends)):
        for j in range(len(list_of_friends[i])):
            list_of_friends[i][j] = int(list_of_friends[i][j])

    #Sorting the column side to find the user easier
    list_of_friends_sorted = list_of_friends[:]
    list_of_friends_sorted.sort(key=lambda x : x[1])
    
    #This is the list of the unique id of the users
    unique_list_of_users = unique_identifiers(list_of_friends)
    unique_list_of_users.sort()

    #The start position referses to the start position that is used to slice the list_of_friends
    start_position_for_list_of_friends = 0
    start_position_for_list_of_friends_sorted = 0

    all_users = []
    for i in range(len(unique_list_of_users)):

        user_value = int(unique_list_of_users[i])

        #Adding both functions together that include both the list of friends and the indirect list of friends.
        #We are only focus on the unique values that we go through the list of unqiue values.
        
        combine_list_of_friends = get_friends(user_value,list_of_friends) + get_indirect_friends(user_value,list_of_friends_sorted) 
        combine_list_of_friends.sort()

        #Formating the output of the created list.
        all_users.append([user_value, combine_list_of_friends])
        all_users.sort()

        #Since the len means that how many friends that we have then we don't need to search those same positions since they are sorted
        start_position_for_list_of_friends = len(get_friends(user_value,list_of_friends))
        start_position_for_list_of_friends_sorted = len(get_indirect_friends(user_value, list_of_friends_sorted))

        list_of_friends = list_of_friends[start_position_for_list_of_friends::]
        list_of_friends_sorted = list_of_friends_sorted[start_position_for_list_of_friends_sorted::]

    #Turning all of the values into to tuples.
    for i in range(len(all_users)):
        all_users[i] = tuple(all_users[i])

    #Set network list given to us to the created list from the functions.
    network = all_users

    return network #huge.txt 15s to return a value

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    
    # YOUR CODE GOES HERE

    def find_user(id_user, network):
        '''(int,list)->list
        Finds the user id in the network and returns a list that is comprised of the friends of the id.
        Precondition: id_user is already in the network, network is given.
        Post: A list is returned.
        '''
        
        friends = [] #List that holds the friends of the user
        
        for i in range(len(network)):
            if id_user == network[i][0]: # [0] is the first column that refers the the id of any user
                friends.append(network[i][1])

        return friends

    def compare_list_of_friends(user1_list_of_friends,user2_list_of_friends):
        '''(list,list)->list
        Finds the shared friends in both list and return a list of shared friends.
        Precondition: List of friends of user1 and list of friends of user 2 is given.
        Post. A list is returned. 
        '''

        common_friends_user1 = [] #Since user1_list_of_friends is a 2d list we need to compare that values inside of each position
        for i in user1_list_of_friends:
            for j in i:
                common_friends_user1.append(j)

        common_friends_user2 = []
        for i in user2_list_of_friends:
            for j in i:
                common_friends_user2.append(j)

        common_friends = []
        for i in range(len(common_friends_user1)):
            if common_friends_user1[i] in common_friends_user2: #If the id of the friend is found in the list of the other list then add to the list
                common_friends.append(common_friends_user1[i])

        return common_friends
                

    user1_find_friends = find_user(user1, network) #Find the friends of both users
    user2_find_friends = find_user(user2, network)

    common = compare_list_of_friends(user1_find_friends,user2_find_friends) #This is the list that has both shared friends

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    # YOUR CODE GOES HERE

    def get_Friends(user,network):
        '''(int, list)->list
        Finds all the friends of the user.
        Precondition: user and network is given.
        Post: A list is returned.
        '''

        user_friends = []

        for i in range(len(network)):
            if user == network[i][0]: #This referse to the column position and check if the id are the same
                user_friends.append(network[i][1])

        return user_friends

    def get_Friends_of_Friends(user,friend,list_of_Friends,network):
        '''(int,int,list,list)->list
        Finds the friends of friends from the user.
        Precondition: user, friend, list_of_Friends, network are given.
        Post: A list is returned.
        '''

        compare = []

        for i in list_of_Friends: #2D array so we have to use the values inside of list_of_Friends
            for j in i:
                compare.append(j)
        
        Friends_of_friend = get_Friends(friend,network) #Calls the find the list of friends of friends

        new_list_of_Friends = []

        for i in Friends_of_friend:
            for j in i:
                if user != j and j not in compare: #We can't include the user and the friends of the user in the results
                    new_list_of_Friends.append(j)

        return new_list_of_Friends

    def find_unique_non_friends(list_of_non_friends):
        '''(list)->(list)
        Finds the unique id in the given list. A unique is the a id that does not appear in the list more than once.
        Precondition: list_of_non_friends is given.
        Post: A list is returned.
        '''

        list_of_unique_friends = []

        for i in list_of_non_friends:
            for j in i:
                if j not in list_of_unique_friends: #To see if the current index is already in the list
                    list_of_unique_friends.append(j) #If it isn't then we add that index to the list

        return list_of_unique_friends

    def find_common_of_unique_friends(user,user2,network):
        '''(int,int,list)->int
        Finds the commonfriends of both users by calling a function.
        Precondition: user1 and user2 and network are given.
        Post: A integer is returned
        '''

        #Call the getCommonFriends function and returns the length of the list that is returned in the getCommonFriends function
        return len(getCommonFriends(user,user2,network))

    #Get the friends of the user
    friends_of_Friends = get_Friends(user,network) #This list are the list of friends that the user has.

    #Find the friends of the users friends that does not include the user or the friends of the friends of the user
    list_of_friends_of_friends = []

    for i in friends_of_Friends:
        for j in i:
            #This list are the list of friends that the user is not friends with
            list_of_friends_of_friends.append(get_Friends_of_Friends(user,j,friends_of_Friends,network))
    
    #Find the unique friends of friends
    list_of_unique_friends = find_unique_non_friends(list_of_friends_of_friends)
    
    #Find the common friends between the user and the unique friends of the friends and count the amount of common friends between the user and the unique friends.
    number_of_unique_friends = []
    
    for i in list_of_unique_friends:
        number_of_unique_friends.append([i,find_common_of_unique_friends(user,i,network)])

    #We need to choose the unique friend that has the higest amount of friends and with the lowest id
    if len(number_of_unique_friends) <= 0:
        return None

    #Finds the max value in the column that is the column referes to the length of the common friend the user and the unique non friend has
    max_value = 0
    for i in range(len(number_of_unique_friends)):
        if max_value < number_of_unique_friends[i][1]:
            max_value = number_of_unique_friends[i][1]


    #We need to find the lowest id of the user with the highest amount of known friends
    list_of_unique_friends = []
    for i in range(len(number_of_unique_friends)):
        if max_value == number_of_unique_friends[i][1]:
            list_of_unique_friends.append(number_of_unique_friends[i][0])

    #If two users have the same amount of max common friends then we have to choose the id with the lower value
    return min(list_of_unique_friends)

def number_of_friends(user,network): #This was not included in the starter code
        '''(int, list)->int
        Finds the friends of the given user and finds the length of each list of users friends.
        Precondition: User and network are given.
        Post: A integer is returned.
        '''
        user_friends = []

        for i in range(len(network)):
            if user == network[i][0]: #This referse to the column position and check if the id are the same
                user_friends.append(network[i][1])

        for i in user_friends:
            return len(i) #Referres the length of each list of user_friends.

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''
    # YOUR CODE GOES HERE

    counter = 0

    for user in range(len(network)):
        if number_of_friends(network[user][0],network) >= k: #If there are any list lengths that are greater than k we add to the counter
            counter += 1
        
    return counter

def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''

    max_value = 0

    for user in range(len(network)):
        #Finds the max value by comparing the returned the length of the number of friends
        if max_value < number_of_friends(network[user][0],network):
            max_value = number_of_friends(network[user][0],network)

    return max_value
    

def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''
    max_friends=[]
    # YOUR CODE GOES HERE

    #To see if there is a user with the maximum number of friends and checks the network to see if a user has the exact value
    maximum_friends = maximum_num_friends(network)

    for i in range(len(network)):
        if maximum_friends == len(network[i][1]):
            max_friends.append(network[i][0])
    
    return    max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    # YOUR CODE GOES HERE

    list_of_everyone = []

    for i in range(len(network)):
        list_of_everyone.append(number_of_friends(network[i][0],network))

    #Calculates the average
    net = sum(list_of_everyone)/len(network)

    return net
        

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    # YOUR CODE GOES HERE

    people_who_know_the_most = people_with_most_friends(network)

    #Since we are most likley to find the person with the most friends is the person that has the highest posiblity to know everyone
    for i in people_who_know_the_most:
        if number_of_friends(i,network) == len(network)-1:
            return True

    return False

####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''(2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''
    
    # YOUR CODE GOES HERE

    valid_input = False
    ans = 0

    while valid_input == False:
        try:
            ans = int(input("Enter an integer for a user ID: "))
            valid_input = True

        except ValueError: #User enters a float, string it catches the badinput
            print("That was not an integer. Please try again.")

        if valid_input: #If it is an integer we check if the user is in the network

            valid_input = False

            for i in range(len(network)):
                if ans == network[i][0]:
                    valid_input = True

            if valid_input == False:
                print("That user ID does not exist")

    return ans
            
##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")
