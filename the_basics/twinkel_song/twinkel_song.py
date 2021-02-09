base_str = 'Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are.\n\n '

base_words = base_str.split()



def get_spaces(count):
    spaces = '\t' * count
    return '\n' + spaces 
    


def song(index,repeats):
    
    f_sentences = []
    commna_repeat = 0
    dot_repeat = 0

    add_spaces = True
   
    
    for word in base_words: 
        
        if  word[-1] == '.':
            f_sentences.append(word + " ")
            f_sentences.append('\n')
            commna_repeat = 0
            dot_repeat = dot_repeat + 1
            
            if dot_repeat == 2:
                if index + 1 == repeats:
                     f_sentences.append("\n              >>>>>>>>>>..... End of Song .....<<<<<<<<<< \n\n")
                else:
                     f_sentences.append(get_spaces(5)+" 'Repeat' " + '\n\n')
                
                dot_repeat = 0
                add_spaces = True
            
        elif word[-1] == ',':
            commna_repeat = commna_repeat + 1
            f_sentences.append(word + " ")
            
            
        elif commna_repeat == 4:
            add_spaces = True
            commna_repeat = 0
            f_sentences.append(get_spaces(2))
            f_sentences.append(word + " ")
        
        
            
        elif(commna_repeat == 3):
         
            if add_spaces:
                f_sentences.append(get_spaces(1))
                f_sentences.append(word + " ")
                add_spaces = False
            elif word[-1] == '!':
                f_sentences.append(word + " ")
                f_sentences.append(get_spaces(2))
            else:
                f_sentences.append(word + " ")
            
        
        else:
            f_sentences.append(word + " ")
        

    formatted_song = ''

  
    print(formatted_song.join(f_sentences))


def let_sing_twinkle_twinkel(repeats):
    print("\n              >>>>>>>>>>.....Lets Sing Twinkle,Twinkle Song.....<<<<<<<<<< \n\n")
    for i in range(repeats):
        song(index = i,repeats= repeats)

let_sing_twinkle_twinkel(repeats = 3)
    
        



