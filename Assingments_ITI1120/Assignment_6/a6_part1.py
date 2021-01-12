import string

# Family Name: JuanPablo Sanchez
# Student Number: 
# Course: ITI 1120
# Assignment Number 6
# Due 7 Dec, 2020

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE

    valid_input = False
    file_name = None

    while valid_input == False:
        try:
            file_name = input("Enter the name of the file : ").strip()
            file = open(file_name)
            file.close()
            valid_input = True
        
        except FileNotFoundError:
            print("There is no file with that name. Try Again")

    return file_name

def clean(text):
    '''(str) -> 2d list
    Extra function that removes all of the punctuation in a given text.
    Precondition: A string is given.
    Post: A 2d list is returned.
    '''

    #Removing all punctuation
    remove_punctuation = ''.join(i for i in text if not i in string.punctuation)

    #Since we need to keep the order of the sentences
    #We split each sentences at each new line
    seperated_lines = remove_punctuation.splitlines()

    for sentence in range(len(seperated_lines)):
        #Inside the 2d list we need to seperate the words
        #We need to keep the order of the words in each sentence
        seperated_lines[sentence] = seperated_lines[sentence].split()

    #Returns a 2d list
    return seperated_lines


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE

    #Open the file and read content
    file_line = open(fp).read().lower()
    cleaned_sentences = clean(file_line) #2d list

    dictionary_of_words = {}

    for sentence in range(len(cleaned_sentences)):
        for key in cleaned_sentences[sentence]:

            #Removing all words words with less than 2 characters
            #Removing all numbers 
            if len(key) > 1 and key.isdigit() == False:

                #If the word does not exist, insert the key with location
                dictionary_of_words.setdefault(key, set()).add(sentence + 1)

    return dictionary_of_words
    
def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE

    #Creates a list that is the individual strings given from the user
    words = []
    words.extend(query.split())
    
    #Creating a set of the values of the first word in the query
    original = set()
    original.update(D.get(words[0]))

    #Looping through the rest of the list but starting past the orginial key
    for word in range(1, len(words)):
        original.intersection_update(D.get(words[word]))

    #Converting the set into a sorted list
    coexistance_values = []
    for value in original:
        coexistance_values.append(value)

    coexistance_values.sort()

    return coexistance_values


def clean_word(key):
    '''(str) -> str
    Removes punctuation from a given string.
    Precondition: string is given.
    Post: A string is returned.
    '''

    clean_key = ''.join(i for i in key if i not in string.punctuation)

    return clean_key

def is_key_special_char(key):
    '''(str) -> str
    Tests if the key is a special character.
    Precondition: string is given:
    Post: string is returned.
    '''

    if key in string.punctuation:
        key = " "

    return key

def check_valid_key(d, query):
    '''(dict, str) -> list or str
    Checks to see if the value is a dictionary.
    Precondition: dictionary, string is given.
    Post: A string or list is returned
    '''

    #Creating a list of individual possible words
    possible_keys = query.split()

    cleaned_keys = []

    for key in possible_keys:

        #Since we have removed all of the punctuation
        #The result is always going to return as an error
        #We need to clean the word to have the possbility
        #For a result
        clean_key = clean_word(key)

        #Check if it is a special character
        #A special character has a different output line
        if is_key_special_char(key) == " ":
            return ""

        #Check to see if it is a number
        if key.isalpha() == False:
            return key

        if clean_key not in d:
            return key

        else:
            cleaned_keys.append(clean_key)

    #List of all keys that can be accessed by the dictionary.
    return cleaned_keys

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE

#Loop that asks the user for a new input until key value is inputed.
while query != 'q':

    if len(query) == 0:
        print("Word '' not in the file")

    else:
        #Check to see if all user inputed values are able to searched in the dictionary.
        valid_key = check_valid_key(d, query)

        #Since there could be two return variable
        #The list is the when all the values can be found in the dictionary.
        if type(valid_key) is list:

            #The find_coexistance function paramaters uses a string.
            #We convert list into a string.
            string_of_all_keys = ' '.join([str(key) for key in valid_key])
        
            coexistance_values = find_coexistance(d, string_of_all_keys)

            if len(coexistance_values) > 0:
                
                #Printing all the values
                for i in coexistance_values:
                    print(i, end = " ")

                print()

            else:
                print('The one or more words you entered does not coexist in a same line of the file.')
        
        else:
            #When the input of the user cannot be found in the dictonary.
            #A string is returned showing which word cannot be found.
            print("Word '" + str(valid_key) + "' not in the file")
        
    #Reasks the question.
    query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    
