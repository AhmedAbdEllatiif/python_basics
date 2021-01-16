

def sentence_maker(phrase):
  capitalized = phrase.capitalize()
  if phrase.startswith(("how","what","why","when","is","do","are","does")) :
    return "{}?".format(capitalized) 
    #return f"{capitalized}?"
  else : 
    return "{}.".format(capitalized)
    #return f"{capitalized}."



results = []
while True:
  userInput = input('Say Something:')
  if userInput == "\end":
    break 
  else: 
    results.append(sentence_maker(userInput))
    
print(" ".join(results))

"""
oldMessage = ''
while True: 
  message = input('Say Something: ')
  
  if message == 'q':
     break
  
  elif message == 'cmd':
    print(oldMessage)
    break
    
  else:
    message = sentence_maker(message)
    oldMessage = f'{oldMessage} {message}'
    continue
    """
  
  

