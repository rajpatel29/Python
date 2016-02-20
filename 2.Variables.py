Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

 
>>> x = 3
>>> x ** 2
9
>>> g = inp
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    g = inp
NameError: name 'inp' is not defined
>>> g = input("Enter number here: ")
Enter number here: 23
>>> int(g) + 2
25
>>> g + 2
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    g + 2
TypeError: Can't convert 'int' object to str implicitly
>>> f  = input()
g
>>> f + 2
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    f + 2
TypeError: Can't convert 'int' object to str implicitly
>>> int(f) + 2
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int(f) + 2
ValueError: invalid literal for int() with base 10: 'g'
>>> f
'g'
>>> int(f)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    int(f)
ValueError: invalid literal for int() with base 10: 'g'
>>> f
'g'
>>> 
