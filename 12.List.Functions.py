Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

 
>>> numbers = [1,2,3,4,5,6,7]
>>> len numbers
SyntaxError: invalid syntax
>>> len (numbers)
7
>>> max (numbers)
7
>>> min (numbers)
1
>>> list ("rutvik")
['r', 'u', 't', 'v', 'i', 'k']
>>> numbers[3] = 10
>>> numbers
[1, 2, 3, 10, 5, 6, 7]
>>> del numbers[3]
>>> numbers
[1, 2, 3, 5, 6, 7]
>>> numbers[7] = 99
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    numbers[7] = 99
IndexError: list assignment index out of range
>>> 
