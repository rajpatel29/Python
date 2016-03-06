#Class

class MyClass:
    i = 90
    def f(self) :
        return "Hey there :)"
        
'''
output

>>> x = MyClass()

>>> x.f()
'Hey there :)'
>>> x.i
90

'''


#When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance.
class MyClass2 :
    def __init__(self , a , b) :
        self.x = a
        self.y = b

        
'''
output

>>> c = MyClass2(4,5)
>>> c.x
4
>>> c.y
5

>>> c.z =90
>>> c.z
90
'''


#data attributes correspond to “instance variables” in Smalltalk, and to “data members” in C++. Data attributes need not be declared; like local variables,
#they spring into existence when they are first assigned to.


#In above example see we did not declare x , y , z








#Class and Instance Variables

class Person :
    sharedName = "xyz"      # class variable shared by all instances
    
    def __init__(self, name) :
        self.name = name    # instance variable unique to each instance

'''
output

>>> person1 = Person("name1")
>>> person2 = Person("name2")
>>> person1.name
'name1'
>>> person2.name
'name2'

>>> person1.sharedName
'xyz'
>>> person2.sharedName
'xyz'

'''



#Any function object that is a class attribute defines a method for instances of that class. It is not necessary that the function definition is textually enclosed in the
#class definition: assigning a function object to a local variable in the class is also ok.

def f1 (self , x , y) :
    return min(x, y)


class C :
    f = f1
    def h1(self) :
        print("Hi there how you doing?")
    h = h1


'''
output

>>> obj = C()

>>> obj.h()
Hi there how you doing?

>>> obj.f(2,3)
2

'''



#Methods may call other methods by using method attributes of the self argument:
class Bag :
    def __init__(self) :
        self.bascket = []
    def add(self , x) :
        self.bascket.append(x)
    def addTwice(self , x) :
        self.add(x)
        self.add(x)

'''
output

>>> obj = Bag()

>>> obj.addTwice(2)
>>> obj.bascket
[2, 2]
>>> obj.add(4)
>>> obj.bascket
[2, 2, 4]

'''




class Parent :
    def __init__(self) :
        self.basket = []
        print("Prent Constructor")

    def callMe(self) :
        print("parent1 method ")

class Parent2 :
    def __init__(self) :
        print("Prent2 Constructor")

    def callParent2(self) :
        print("parent2 method ")


class Child (Parent , Parent2) :
    def __init__(self) :
        print("Child Constructor")

    def callMe2(self) :
        super(Child , self).callMe()
        

'''
output

>>> child = Child()
Child Constructor
>>> child.callMe2()
parent1 method

>>> child.callParent2()
parent2 method 

'''

        





































