import json
from difflib import SequenceMatcher 
from difflib import get_close_matches

# load the data from json file
data = json.load(open('files/data.json'))

# function to get the defenition of the word
def translate(word):
    # convert 
    word = word.lower()
    
    if word in data.keys():
         return data[word]
     
    elif len( get_close_matches(word,data.keys())) > 0:
         matchedWord = get_close_matches(word,data.keys(),cutoff= 0.8)[0]
         userInput = input( "Did you mean (%s) instead of (%s) ?  If yes press Y or not press N: " %(matchedWord,word))
         if userInput == "y":
             return data[matchedWord]
         elif userInput == "n":
             return 'Okay, search for in other place __!__'
         else:
             return '__!__ fuck ur self before somebody did...Or...Search for a doggy __!___'
        
            
    else:
         return  ">>>>> Fuck __!__ you man, what the hell you just entered <<<<<<<<<"

word = input("Search For a word: ")


print(translate(word))