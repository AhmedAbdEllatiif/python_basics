

def foo(a,b = 3):
    return a - b 
print(foo(a =10)) 


########List comprehension############
# if we want to divide each num of this list by 10 we can do it by for loop on it and divide each member
# by 10 then add it in a new list.
# or simply use one line comperhension

#temps = [225,230,112,152,-999,512]

""" this is the old way
result  = []
for temp in temps:
    result.append(temp / 10)
print(result)
"""    
''' simple way in one line    
result = [temp / 10 for temp in temps] 
print(result)
'''

''' simple way in one line with condition    
result = [temp /10 for temp in temps if temp != -999]
print(result)
'''
''' simple way in one line with condition but return another value with else instead of just ignoring it
result = [temp /10 if temp != -999 else 0 for temp in temps]
print(result)
'''


############ For Loops ############

""" dict (Like map)
students_grades = {"Ahmed" : 10 ,"Khokha" : 15, "Loooza" : 20}
for student in students_grades.items():
    # Every student is Tuple ("Ahmed",10) like this
    #message = f"Name: {student[0]} , Grade: {student[1]}"
    #message = "Name: %s , Grade: %s" % (student[0] ,student[1]) 
    message = "Name: {} , Grade: {}".format(student[0],student[1]) 
    
    print(message)
"""

"""Another (better) way to do dict::

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
"""


""" lists
temps = [22.3, 25.2, 33.1, 18.1]
for t in temps :
    print(t)
    print('rounded: ',round(t))

print("Awesome Done")

for index, t in enumerate(temps):
    print(index, t)
""" 

############ Type and isinstance ############
""" 
for color in colors: 
    if isinstance(color,int):
    if type(color) is int:
        print(color)
"""


############ string concatination ############
""" string concatination
user_input = input("Enter First Name: ")
fName = user_input 
#message = 'Hello %s!' %user_input 
#print(message)

user_input = input("Enter Your Last: ")
message = f'Hello {fName} {user_input}!' # For python 3.6 and
message = 'Hello %s %s!' % (fName, user_input) # For python lower than 3.6 and
print(message)

name = "Sim"
experience_years = 1.5
awesome = 'Awesome'
print("Hi {} {}, you have {} years of experience".format(awesome,name, experience_years,))

"""

