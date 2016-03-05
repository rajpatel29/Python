
#Tuples and Sequences

t = '123' , 34 , "Hi there"

u = t , (12 , 34 , 56)

v = ([1 , 2 , 4] , [5 , 6 , 7])


'''
output

>>> t
('123', 34, 'Hi there')
>>> t[0]
'123'
>>> t[0] = 6785
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t[0] = 6785
TypeError: 'tuple' object does not support item assignment
>>> u
(('123', 34, 'Hi there'), (12, 34, 56))
>>> v
([1, 2, 4], [5, 6, 7])

'''


#A special problem is the construction of tuples containing 0 or 1 items: the syntax has some extra quirks to accommodate these. Empty tuples are constructed by
#an empty pair of parentheses; a tuple with one item is constructed by following a value with a comma


empty = ()

singleton = "Hi there" ,


'''
output

>>> empty
()
>>> len(empty)
0
>>> singleton
('Hi there',)
>>> len(singleton)
1

'''





#Sets

basket = ["apple" , "banana" , "Taco" , "123" , "123"]

food = set(basket)

a = set('abcdef')
b = set('defghfj')



'''
output

>>> food
{'banana', '123', 'apple', 'Taco'}

>>> "123" in food
True
>>> "34" in food
False


>>> a
{'f', 'a', 'b', 'e', 'c', 'd'}
>>> b
{'f', 'j', 'e', 'h', 'g', 'd'}
>>> a - b
{'c', 'b', 'a'}
>>> a | b
{'f', 'a', 'j', 'b', 'e', 'h', 'g', 'c', 'd'}
>>> a & b
{'f', 'e', 'd'}
>>> a ^ b
{'h', 'c', 'g', 'a', 'j', 'b'}

'''



#Dictionaries

tel = {"first" : 123 , "second" : 802 }

#another way to create dictionaries

tel2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


tel3 = {x : x**2 for x in (1,2,3,4)}

'''
output

>>> tel
{'second': 802, 'first': 123}
>>> tel["third"] = "hi there"
>>> tel
{'second': 802, 'third': 'hi there', 'first': 123}
>>> tel['second']
802
>>> del tel["third"]
>>> tel
{'second': 802, 'first': 123}
>>> tel.keys()
dict_keys(['second', 'first'])
>>> "second" in tel
True

>>> tel2
{'sape': 4139, 'guido': 4127, 'jack': 4098}

>>> tel3
{1: 1, 2: 4, 3: 9, 4: 16}
'''


















