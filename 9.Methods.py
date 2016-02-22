Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

 
>>> face = [1,2,3,4,5]
>>> face
[1, 2, 3, 4, 5]
>>> face.append(45)
>>> face
[1, 2, 3, 4, 5, 45]
>>> face.count(1)
1
>>> face.count(0)
0
>>> one = [1,2,3]
>>> two = [4,5,6]
>>> one.extend(two)
>>> one
[1, 2, 3, 4, 5, 6]
>>> say = ['Hi' ,'There' , 'how' , 'r' , 'you']
>>> say.index('r')
3
>>> say.insert(2,"4")
>>> say
['Hi', 'There', '4', 'how', 'r', 'you']
>>> say.pop(1)
'There'
>>> say
['Hi', '4', 'how', 'r', 'you']
>>> say.remove('4')
>>> say
['Hi', 'how', 'r', 'you']
>>> say.reverse()
>>> say
['you', 'r', 'how', 'Hi']
>>> new = [23,45,32,1,76,44]
>>> new
[23, 45, 32, 1, 76, 44]
>>> new.sort()
>>> new
[1, 23, 32, 44, 45, 76]
>>> sorted("EassyFella")
['E', 'F', 'a', 'a', 'e', 'l', 'l', 's', 's', 'y']
>>> 1,2,3,4
(1, 2, 3, 4)
>>> rutvik = (1,2,3,4)
>>> rutvik
(1, 2, 3, 4)
>>> rutvik[2]
3
>>> 
