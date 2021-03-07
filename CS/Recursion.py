def fact(n):
    assert n >= 0 and int(n) == n , "Only Accept Positive Integers"
    if n in [0,1]:
        return 1
    else:
        return n * fact(n-1)

#print('Factorial >>> ',fact(4))

## 1 Find Recusion case - the flow
"""
 n! = n*(n-1)*(n-2)*.......*2*1
 when (n-1)! = (n-1) * (n-1-1) * (n-1-2) ..... *2*1
 >>>>>>> (n-1) * (n-1-1) * (n-1-2) ..... *2*1 == (n-1) * (n-2) * (n-3) ..... *2*1 
 then n! = n * (n-1)!
 """
 
def fact_first_step(n):
      return n * fact_first_step(n-1)
  
  
## 2 Base case - The stop criterion
""" 
1! = 1
0! = 1
We stop when reach 1 or 0
"""
def fact_second_step(n):
     if n in  [0,1]:
         return 1
     else:  
        return n * fact_second_step(n-1)
    
    
## 3 Unintentional case - The constraint
""" 
The above functions did not check for negative numbers or non int numbers
assert check the attached file F:\python_course\CS\Assert+keyword.pdf
"""
def fact_third_step(n):
    assert n >= 0 and int(n) == n , "Only Accept Positive Integers"
    if n in [0,1]:
        return 1
    else:
        return n * fact_third_step(n-1)
    


# Find the sum of digits of positive number
def find_sum(x):
    assert x >= 0 and int(x) == x, "Only Accept Positive Integers "
    if x == 0 :
        return 0
    else :
        return find_sum(int(x/10)) + int((x % 10))
#print(find_sum(4))


#Find power of number
def find_power(n,pwr):
    assert  int(pwr) == pwr, "Only Accept Positive Integers "
    if pwr == 0 :
        return 1
    if pwr == 1 :
        return n
    elif pwr < 0 :
         return 1/n * find_power(n,(pwr+1))
    else :
        return n * find_power(n,(pwr-1))
#print(find_power(5,-2))

#Find Greatest Common Divisor of two numbers (gcd)
def find_gcd(x,y):
    print(y)
    assert  int(x)==x and int(y)==y, "Only Accept Integer Numbers "
    if x < 0:
        x= x*-1
    if y < 0:
        y= y*-1
    if y == 0:
        return x
    else:
        return find_gcd(y, (x%y))
#print(find_gcd(-48,-18))

# Convert Decimal to Binary 
def convert_dcml_bnry(x):
    assert  int(x)==x, "Only Accept  Integer Numbers "
    if x == 0:
        return 0
    if x == 1:
        return 1
    return x % 2 + (10*convert_dcml_bnry(int(x/2)))
#print(convert_dcml_bnry(-10.5))

# Find Product of Array Element
arr = [1,2,3,6]
def product(arr):
    if len(arr) == 0:
        return 1
    print(arr)
    return arr[0] * product(arr[1:])
#print(product(arr))

# Find Recursive Range
def rec_range(x):
    assert int(x) == x , "Only Accept Integer numbers"
    if x == 0 : 
        return 0 
    if x == 1 :
        return 1
    if x < 0:
        return x + rec_range(x + 1)
    else:
        return x + rec_range(x - 1)
#print(rec_range(-6))

# reverse string
# Return the reverse of String
def reverse(strng):
    if len(strng) <= 1:
      return strng
    print(strng)
    return strng[-1] + reverse(strng[0:len(strng)-1])
#print(reverse('Ahmed'))   


# Forward as Backward
def isPalindrome(str):
    if len(str) == 0:
        return True
    if str[0] != str[-1]:
        return False
    else:
        return isPalindrome(str[1:-1])
#print(isPalindrome('tacocat'))   



######## someRecursicve
# someRecursicve takes accepts array and callback 
# function returns true if a single elemnet is odd 
def isOdd(num):
    return num % 2 != 0
array = [2,2,2,6,2,8,8,4,4,6,2,4,8,9]
def someRecursicve(arr,isodd):
    if len(arr) == 0:
        return False
    if isodd(arr[0]):
        return True 
    else:
        return someRecursicve(arr[1:] , isodd)
#print(someRecursicve(array,isOdd))
        
        
########### Flatten       
# Flatten takes array of arrays and returns a new array with all values flattened
#[2,2,2,6,2,[8,8,4],4,6,2,[4,8,9]] >> [2,2,2,6,2,8,8,4,4,6,2,4,8,9]
nested_arr = [2,2,2,6,2,[8,8,4],4,6,2,[4,8,9]]
def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr 
#print(flatten(nested_arr))


# capitalizeFirst
# capitalizeFirst accepts array of string return array with capitalizeFirst letter
def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    else:
        result.append(arr[0].capitalize())
        return result + capitalizeFirst(arr[1:]) 
#print(capitalizeFirst(['ahmed','mohamed','ahmed']))



## NESTED EVEN SUM 
di = {'ahmed':2,'asd':3}
obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}
def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) == dict:
             sum += nestedEvenSum(obj[key])
        if type(obj[key]) == int and obj[key] % 2 == 0:
             sum += obj[key]
    return sum
#print(nestedEvenSum(obj1))


def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj
#print(stringifyNumbers(obj1))


##COLLECT STRINGS SOLUTION
def collectStrings(obj):
    resultArr = []
    for key in obj:
        if type(obj[key]) is str:
            resultArr.append(obj[key])
        if type(obj[key]) is dict:
            resultArr = resultArr + collectStrings(obj[key])
    return resultArr


