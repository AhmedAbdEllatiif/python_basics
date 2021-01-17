import json
from difflib import SequenceMatcher 
from difflib import get_close_matches

# load the data from json file
data = json.load(open('files/data.json'))

# function to get the defenition of the word
def translate(word):
    # convert the word to lowre case 
    word = word.lower()
    global matchedWord 
    matchedWord = ''
    
    # check if the word already in the data
    if word in data.keys():
         return data[word]
     
    # Check if the word.title matches and data key like(egypt)
    elif word.title() in data.keys():
        return data[word.title()]
     
    # check if the word match any word in the data
    elif len( get_close_matches(word,data.keys())) > 0:
         matchedWord = get_close_matches(word,data.keys(),cutoff= 0.8)[0]
         userInput = input( "Did you mean (%s) instead of (%s) ?  If yes press Y or not press N: " %(matchedWord,word))
         if userInput == "y":
             return data[matchedWord]
         elif userInput == "n":
             return 'Okay, search for in other place __!__'
         else:
             return '__!__ fuck ur self before somebody did...Or...Search for a doggy __!___'
        
    # fuck the user        
    else:
         return  ">>>>> Fuck __!__ you man, what the hell you just entered <<<<<<<<<"


# input by user
word = input("Search For a word: ")


# Data returned from the function
wordData = translate(word)


# To print the corrent word 
if matchedWord != '':
    print('>>>> {} <<<<: '.format(matchedWord.capitalize()))
else:
    print('>>>> {} <<<<: '.format(word.capitalize()))
   
   
# print the data     
if isinstance(wordData,str): 
    print(wordData)
else:
    for index,line in enumerate(wordData):
        print(line)
        if(index == len(wordData) - 1):
            print('\n')

