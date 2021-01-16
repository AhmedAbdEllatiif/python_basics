#myFruitFile = open('fruits.txt')
#print(myFruitFile.read())

'''open for reading (default)
with open('../files/fruits.txt') as myFile:
    content = myFile.read()

print(content)
'''
'''open for writing, truncating the file first
with open('../files/vegtables.txt','w') as vegFile:
    content = vegFile.write('Tomato\nCucumber\nOnion\n')
'''

''' appending to the end of the file if it exist
with open('../files/vegtables.txt','a') as vegFile:
        vegFile.write('\nPeper')
'''
'''
with open('../files/vegtables.txt','a+') as vegFile:
    vegFile.write('\nAwesome')
    vegFile.seek(0) #To make the cursor at the first of the file
    content = vegFile.read()
print(content)
'''

with open('../files/vegtables.txt','a+') as vegFile:
    vegFile.seek(0)
    content = vegFile.read()
    vegFile.seek(0)
    vegFile.write("\n{}".format(content))
    vegFile.write("\n{}".format(content))


'''
# In this section, you learned that:

# You can read an existing file with Python:
with open("file.txt") as file:
    content = file.read()

# You can create a new file with Python and write some text on it:
with open("file.txt", "w") as file:
    content = file.write("Sample text")

# You can append text to an existing file without overwriting it:
with open("file.txt", "a") as file:
    content = file.write("More sample text")
    
# You can both append and read a file with:
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()
'''