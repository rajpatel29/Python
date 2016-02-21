Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> array["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    array["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
NameError: name 'array' is not defined
>>> array = ["0" , "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]
>>> array[1: 5]
['1', '2', '3', '4']
>>> array[5:8]
['5', '6', '7']
>>> array[5:9]
['5', '6', '7', '8']
>>> array[5:10]
['5', '6', '7', '8', '9']
>>> array[5:]
['5', '6', '7', '8', '9']
>>> array[:]
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> array[ : 7]
['0', '1', '2', '3', '4', '5', '6']
>>> array[1 : 8 : 2]
['1', '3', '5', '7']
>>> array[8 : 1 : -2]
['8', '6', '4', '2']
>>> array[ :  : -2]
['9', '7', '5', '3', '1']
>>> 
