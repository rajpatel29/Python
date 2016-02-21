Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

 
>>> num = 23
>>> num
23
>>> print "value of num is: " + num
SyntaxError: Missing parentheses in call to 'print'
>>> print ("value of num is: " + num)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print ("value of num is: " + num)
TypeError: Can't convert 'int' object to str implicitly
>>>  print ("value of num is: " + str(num))
 
SyntaxError: unexpected indent
>>> num = str(num)
>>> num
'23'
>>> print ("value of num is: " + num)
value of num is: 23
