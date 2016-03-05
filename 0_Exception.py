#Exception


#Handling Exception

def exception1() :
    try:
        x = int(input("Enter a number : "))
        print("You entered " + str(x))
    except ValueError :
        print("ooooppppss you  got an exception")
        

'''
output

>>> exception1()
Enter a number : 34
You entered 34
>>> exception1()
Enter a number : ddn
ooooppppss you  got an exception

'''





#Multiple Exception
#default Exception handliing
#Finally block


dictionary = {"1" : 89 , "2" : 45 }

import sys

def exception2() :
    try:
        #ValueError
        x = int(input("Enter a number : "))
        print("You entered " + str(x))

        #ArithmeticError        
        y = 10 / x
        print("10 / " + str(x) + " = "  + str(y))

        #Default
        z = dictionary["1exception2()"]
        print(str(z))
        
    except ValueError :
        print("oops you  got a ValueError exception")
    except ArithmeticError :
        print("oops! you got an Arithmetic exception")
    except  :
        print("default exception "  )

    else:
        print("In else clause")
      
    finally :
        print("In finally block")
    







#Raising Exception

def exception3() :
    try :
        raise NameError("Hi there")
    except NameError:
        print("You got an exception")
        raise








#User Defined Exception

class MyException(Exception):
    def __init__(self, value1, value2):
        self.value = value2
    def __str__(self):
         return "This will be printed whenever you print exception object " + str(self.value)

def exception4() :
    try :
        raise MyException(2*2 , 45)
    except MyException as e:
        print("Value " + str(e.value))
        print("you got exception " + str(e) )
        
