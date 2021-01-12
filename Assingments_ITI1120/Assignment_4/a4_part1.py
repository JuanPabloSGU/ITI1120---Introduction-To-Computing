# Family Name: JuanPablo Sanchez
# Student Number: 
# Course: ITI 1120
# Assignment Number 4
# Due November 2, 2020

def is_valid_file_name():
    '''()->str or None'''
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
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name

def clean_word(word):
    '''(str)->str
    Returns a new string which is lowercase version of the given word
    with special characters and digits removed

    The returned word should not have any of the following characters:
    ! . ? : , ' " - _ \ ( ) [ ] { } % 0 1 2 3 4 5 6 7 8 9 tab character and new-line character

    >>> clean_word("co-operate.")
    'cooperate'
    >>> clean_word("Anti-viral drug remdesivir has little to no effect on Covid patients' chances of survival, a study from the World Health Organization (WHO) has found.")
    'antiviral drug remdesivir has little to no effect on covid patients chances of survival a study from the world health organization who has found'
    >>> clean_word("1982")
    ''
    >>> clean_word("born_y1982_m08\n")
    'bornym'

    '''
    #YOUR CODE GOES HERE

    word = word.lower()

    special_char = '''!.?:,'"-_\()[]{}%\t\n''' #All special characters that are to be removed
    numbers = "0123456789" #All digits that are to be removed

    #Replaces all of the elements that are in special characters with an empty string
    for element in special_char:
        word = word.replace(element,"")

    for elements in numbers:
        word = word.replace(elements,"")
        
    return word #Returns string


def test_letters(w1, w2):
    '''(str,str)->bool
    Given two strings w1 and w2 representing two words,
    the function returns True if w1 and w2 have exactlly the same letters,
    and False otherwise

    >>> test_letters("listen", "enlist")
    True
    >>> test_letters("eekn", "knee")
    True
    >>> test_letters("teen", "need")
    False
    '''

    if len(w1) != len(w2): #Testing the length of the string is the same to not compare strings that don't have the same length
        return False

    w1 = list(w1) #Converting a string into a list to individually compare letters
    w2 = list(w2)

    w1.sort()
    w2.sort()

    if w1 == w2: #If the lists have exactly the same letters
        return True
    else:
        return False
    
def create_clean_sorted_nodupicates_list(s):
    '''(str)->list of str
    Given a string s representing a text, the function returns the list of words with the following properties:
    - each word in the list is cleaned-up (no special characters nor numbers)
    - there are no duplicated words in the list, and
    - the list is sorted lexicographicaly (you can use python's .sort() list method or sorted() function.)

    This function must call clean_word function.

    You may find it helpful to first call s.split() to get a list version of s split on white space.
    
    >>> create_clean_sorted_nodupicates_list('able "acre bale beyond" binary boat brainy care cat cater crate lawn\nlist race react cat sheet silt slit trace boat cat crate.\n')
    ['able', 'acre', 'bale', 'beyond', 'binary', 'boat', 'brainy', 'care', 'cat', 'cater', 'crate', 'lawn', 'list', 'race', 'react', 'sheet', 'silt', 'slit', 'trace']

    >>> create_clean_sorted_nodupicates_list('Across Europe, infection rates are rising, with Russia reporting a record 14,321 daily cases on Wednesday and a further 239 deaths.')
    ['', 'a', 'across', 'and', 'are', 'cases', 'daily', 'deaths', 'europe', 'further', 'infection', 'on', 'rates', 'record', 'reporting', 'rising', 'russia', 'wednesday', 'with']
    '''

    ps = s.split() #Converts to individual characters to send to the clean word function

    x = "" #Empty string to hold all of the converted characters and the unchanged characters to create a new string
    
    for i in ps:
        x += clean_word(i)+ " "
 
    y = ''.join(x[:len(x)-1]) #Joins all of the characters together 
    
    z = list(y.split(" ")) #Creats a list, most important it spaces the positions where the characters were replaces with an empty string, needed for when a number gets replaced.
    
    z.sort() #Sort the list lexicographicaly 
    reverse = z[::-1] #Reverses the list as to just remove the first position of the string.

    for i in range(len(z)-1):
        if z[i] == z[i+1]:
            reverse.remove(z[i]) #Removes the word that is repeated in the list.

    return reverse[::-1] #Since we reversed the list from before we need to reverse the list again to return to lexicographical list.

def word_anagrams(word, wordbook):
    '''(str, list of str) -> list of str
    - a string (representing a word)
    - wordbook is a list of words (with no words duplicated)

    This function should call test_letters function.

    The function returs a (lexicographicaly sorted) list of anagrams of the given word in wordbook
    >>> word_anagrams("listen", wordbook)
    ['enlist', 'silent', 'tinsel']
    >>> word_anagrams("race", wordbook)
    ['acre', 'care']
    >>> word_anagrams("care", wordbook)
    ['acre', 'race']
    >>> word_anagrams("year", wordbook)
    []
    >>> word_anagrams("ear", wordbook)
    ['are', 'era']
    '''
       
    #YOUR CODE GOES HERE

    found_anagrams = "" #Creates empty string to hold to found anagrams

    for i in range(len(wordbook)):
        if test_letters(word,wordbook[i]): #If test_letters returns true and the word is the same found in the word book then add the new list.
            if word != wordbook[i]:
                found_anagrams += wordbook[i] + " "

    convert_anagrams = ''.join(found_anagrams[:len(found_anagrams)-1]) #Converting the string into a list, subtracing the last position to account for the spacing the in string.

    anagrams = list(convert_anagrams.split())
    anagrams.sort() #Sorting the list lexicographicaly

    return anagrams #Returns the list

def count_anagrams(l, wordbook):
    '''(list of str, list of str) -> list of int

    - l is a list of words (with no words duplicated)
    - wordbook is another list of words (with no words duplicated)

    The function returns a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.
    
    Whenever a word in l is the same as a word in wordbook, that is not counted.

    >>> count_anagrams(["listen","care", "item", "year", "race", "ear"], wordbook)
    [3, 2, 3, 0, 2, 2]

    The above means that "listen" has 3 anagrams in wordbook, that "care" has 2 anagrams in wordbook ...
    Note that wordbook has "care", "race" and "acre" which are all anagrams of each other.
    When we count anagrams of "care" we count "race" and "acre" but not "care" itself.
    '''
    
    #YOUR CODE GOES HERE
    
    num_anagrams = [] #Create a open list to store the number of times word_anagrams is called.

    for i in range(len(l)):
        x = word_anagrams(l[i],wordbook) #Stores the returned value of word_anagrams

        num_anagrams.append(len(x)) #Adds to the list the number of elements in the previous statment to count the number of times word_anagrams is called.

    return num_anagrams #Returns the list of integers
        
def k_anagram(l, anagcount, k):
    '''(list of str, list of int, int) -> list of str

    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a  (lexicographicaly sorted) list of all the words
    in l that have exactlly k anagrams (in wordbook as recorded in anagcount)

    k_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2], 2)
    ['care', 'ear', 'race']
    '''

    #YOUR CODE GOES HERE
    
    k_anagram = [] #Empty List for the elements with k index
    j = 0 #Counter for the first list to see the index of the position
    
    for i in anagcount: #Sets i to the value of how many times there is an anagram
        
        if i == k:
            k_anagram.append(l[j]) #Add to the list the element that has the required position to the new list.
            
        j += 1

    k_anagram.sort() #Sorts the list lexicographicaly

    return k_anagram

def max_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with maximum number of anagrams (in wordbook as recorded in anagcount)
    
    >>> max_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['item', 'listen']
    '''
    
    #YOUR CODE GOES HERE
    x = max(anagcount) # Finding the max value of the anagcount

    #Similar to the process in k_anagram
    max_anagram = []
    j = 0

    for i in anagcount:
        if i == x:
            max_anagram.append(l[j])

        j+=1

    max_anagram.sort()

    return max_anagram


def zero_anagram(l, anagcount):
    '''(list of str, list of int) -> list of str
    - l is a list of words (with no words duplicated)
    - anagcount is a list of integers where i-th integer in the list
    represents the number of anagrams in wordbook of the i-th word in l.

    The function returns a (lexicographicaly sorted) list of all the words
    in l with no anagrams
    (in wordbook as recorded in anagcount)
    
    >>> zero_anagram(["listen","care", "item", "year", "race", "ear"], [3, 2, 3, 0, 2, 2])
    ['year']
    '''

    #YOUR CODE GOES HERE

    #Similar to the process in k_anagram and max_anagram
    zero_anagram = []
    j = 0

    for i in anagcount:
        if i == 0: #Find the element with zero number of anagrams.
            zero_anagram.append(l[j])

        j += 1

    zero_anagram.sort()

    return zero_anagram


#Theses are my created functions for the scrabble portion
def find_anagrams(word, wordbook):
    '''(str, list of str) -> (list of str)
    This function is to find a anagram of a given word.
    Precondition: word and wordbook is given.
    Post: A list of string is returned.
    '''

    found_anagrams = ""

    for i in range(len(wordbook)):
        if test_letters(word,wordbook[i]): #To test the entire word is in the wordbook
            found_anagrams += wordbook[i] + ' ' #Add to a string the word that are the same in the wordbook

    convert_anagrams = ''.join(found_anagrams[:len(found_anagrams)-1])

    anagrams = list(convert_anagrams.split()) # Converts the string into a list
    return anagrams

def ommit_letter(word):
    '''(str)->None
    This function slices a word and test if the slice word has a anagram.
    Precondition: String is given.
    Post: Print statements are printed.
    '''

    # Tried to have most of the print statments in the function to make the main function easier to read.
    print("The letters you gave us are: " + word)

    list_word = list(word)
    part_one = []
    part_two = []
    new_word = []
    ns = ""

    print("Let's see what we can get if we ommit one of these letters.")

    for i in range(len(list_word)):
        part_one = list_word[:i] #Splits the word into 2 places to remove the index that we are using 
        part_two = list_word[i+1:]
        new_word = part_one + part_two

        ns = ''.join(new_word) #Creating a new string to hold the spliced word to be compared

        print("Without the letter in position", i+1, "we have letters " + ns)

        if find_anagrams(ns,wordbook)!=[]: #If find_anagras returns "[]" it means that it did not find any word that are in the wordbook because it did not add to the list of words.
            print("Here are the words that are comprised of letters " + ns)
            print(find_anagrams(ns,wordbook))
        else:
            print("There is no word comprised of letters: " + ns)
        
##############################
# main
##############################
wordbook=open("english_wordbook.txt").read().lower().split()
list(set(wordbook)).sort()

print("Would you like to:")
print("1. Analize anagrams in a text -- given in a file")
print("2. Get small help for Scrabble game")
print("Enter any character other than 1 or 2 to exit: ")
choice=input()

if choice=='1':
    file_name=get_file_name()
    rawtx = open(file_name).read()
    l=create_clean_sorted_nodupicates_list(rawtx)
    anagcount = count_anagrams(l,wordbook)

    print("\nOf all the words in your file, the following words have the most anagrams:")

    # YOUR CODE GOES HERE
    # when asking for k from the user you may assume that they will enter non-negative integer

    x = max_anagram(l,anagcount)
    print(x)

    print()

    print("Here are their anagrams: ")
    for i in range(len(x)):
        element = ''.join(x[i]) #word_angrams requires a string to be input'd meaning that we need to convert the word into a list and back into a string.
        
        print("Anagrams of " + element + " are : ", word_anagrams(element,wordbook))

    print()

    print("Here are the words from your file that have no anagrams: ")
    print(zero_anagram(l, anagcount))

    print()

    print("Say you are interested if there is a word in your life that has exactly k anagrams")
    k = int(input("Enter an integer for k: "))
    print("Here is a word (words) in your file with exactly", k, "anagrams: ")
    print(k_anagram(l, anagcount, k))

    
elif choice=='2':

    #YOUR CODE GOES HERE

    badinput = False

    while badinput == False: #Handles if the user inputs a space

        word = input("Enter the letters that you have, one after another with on space: ")

        if word.find(" ") != -1: #.find returns -1 if it is found in the string 
            print("Error: You entered space(s).")
        else:
            badinput = True #To get out of the while loop


    miss_input = False

    while miss_input == False:
             
        print("Would you like help forming a word with: ")
        print("1. All these letters")
        print("2. All but one of these letters? ")
        user = input()
        user = user.strip() #Not nessary but asked in the video to do

        if user == '1':
            if find_anagrams(word,wordbook) != []: #If find_angrams returned "[]" means that it did not find the word in the woodbook.
                print("Here are the words that are comprised of exactly these letters: ")
                print(find_anagrams(word, wordbook))
            
            else:
                print("There is no word comprised of exactly these letters.")

            miss_input = True #To get out of the while loop
    
        elif user == '2':
            ommit_letter(word) #Calls the function that holds most of the print statments to create a clear main function
            miss_input = True                   
else:
    print("Good bye")


