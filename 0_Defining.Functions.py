'''
def fib(n):
    a,b = 0 , 1
    while a < n:
        print (a , end = " ") ,
        a,b = b , a + b
    


fib(100)

print()
print()

#If you want to return list then
def fib2(n):
    result =[ ]
    a,b = 0 , 1
    while a < n:
        result.append(a)
        a,b = b , a + b
    return result

   
print()
print()

#Default Argument Values
def addThree(x = 1 , y = 2 , z = 3):
    sum = x + y + z
    print( sum )

addThree()
addThree(0)
addThree(0,0)
addThree(0,0,0)


print()
print()

#The default values are evaluated at the point of function definition in the defining scope
i = 8
def f(arg = i):
    print(str(arg))
f()    


print()
print()
'''


def fun(a, L =[ ]):
    L.append(a)
    return L

'''
output will be
>>> fun(1)
[1]
>>> fun(2)
[1, 2]
>>> fun(3)
[1, 2, 3]
'''


#If you don’t want the default to be shared between subsequent calls, you can write the function like this instead
def fu(a, L = None):
    if L is None :
        L =[]
    L.append(a)
    return L

'''
output will be something like this
>>> fu(1)
[1]
>>> fu(2)
[2]
>>> fu(3)
[3]
'''



#Keyword Arguments
#Functions can also be called using keyword arguments of the form kwarg=value.

def keyarg(city  , state = "default state" , contry = "defaunt contry"):
    print("CITY : " + city + " STATE : " + state  + " CONTRY : " + contry)

'''
output will look somrthing like this
>>> keyarg('cc')
CITY : cc STATE : default state CONTRY : defaunt contry
>>> keyarg(state = 'ss', city =  'cc')
CITY : cc STATE : ss CONTRY : defaunt contry
>>> keyarg(state = 'ss', city =  'cc')
'''




#Arbitary Arguments
def arbargs(first , *arguments):
    print("First argument is " + first)
    print("Rest are")
    for arg in  arguments :
        print(arg)

'''
output
>>> arbargs('cc' , '1' , '2'  , '3')
First argument is cc
Rest are
1
2
3
>>> arbargs('cc' )
First argument is cc
Rest are
>>> arbargs( )
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    arbargs( )
TypeError: arbargs() missing 1 required positional argument: 'first'

'''




#When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those
#corresponding to a formal parameter. This may be combined with a formal parameter of the form *name (described in the next subsection) which receives a tuple containing
#the positional arguments beyond the formal parameter list. (*name must occur before **name.) 

def method1(first , *arguments , **keywords):
    print("first argument is " + first)
    print("Iterating through tuple")
    for arg in arguments:
        print (arg)
    print("Iterating through dictionary")
    for key in keywords:
        print( key + " has value of " + keywords[key])

'''
output

>>> method1('1' , '2' , '3','4','5' , key1 = '6' , key2 = '7' , key3 = '8')
first argument is 1
Iterating through tuple
2
3
4
5
Iterating through dictionary
key1 has value of 6
key3 has value of 8
key2 has value of 7

'''



#lambda function
def method2(n):
    return lambda x : x + n
            
'''
output

>>> f = method2(40)
>>> f(0)
40
>>> f(10)
50
>>> f(20)
60

'''























    
