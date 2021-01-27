class Account:
     
    def __init__(self,filePath):
        self.filePath = filePath
        with open(filePath,'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self,amount):
       self.balance = self.balance - amount

    def deposit(self,amount):         
       self.balance = self.balance + amount
       
    def commit(self):
        with open(self.filePath,'w') as file:
            file.write(str(self.balance))
        
       

# Inheritance
class Checking(Account):
    
    # This how to create doc for a class
    """ This class generates checking account objects"""
    
    def __init__(self,filePath,fee):
        self.fee = fee
        Account.__init__(self,filePath)
        
    def transfer(self,amount):
        self.balance = self.balance - amount - self.fee
        

checking = Checking('balance.txt',50)
print(checking.__doc__)
#checking.transfer(100,20)
#print(int(checking.balance))
