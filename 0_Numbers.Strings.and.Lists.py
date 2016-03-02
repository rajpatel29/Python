Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

 
>>> 2 + 2
4
>>> 6/4
1.5
>>> 4/3
1.3333333333333333
>>> 4//3
1
>>> 17%3
2
>>> 4 **2
16
>>> width = 20
>>> height = 10
>>> width + height
30
>>> 6.0/2
3.0
>>> 6/2
3.0
>>> 3 + 2
5
>>> width + _
25
>>> round(_ , 2)
25
>>> 500.566
500.566
>>> round(_,2)
500.57
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 'sam\'s egg'
"sam's egg"
>>> "I m \"cool\" I dont care "
'I m "cool" I dont care '
>>> s = "I am this and \n I am that"
>>> s
'I am this and \n I am that'
>>> print (s)
I am this and 
 I am that
>>> print ('c:\some\newfolder')
c:\some
ewfolder
>>> print (r'c:\some\newfolder')
c:\some\newfolder
>>> 4 * ' hi '
' hi  hi  hi  hi '
>>> 'py' 'thon'
'python'
>>> prefix = "py"
>>> prefix  "thon"
SyntaxError: invalid syntax
>>> prefix + "thon"
'python'
>>> text = ('Hi there '
		'how you doing?')
>>> text
'Hi there how you doing?'
>>> word = "python"
>>> word[2]
't'
>>> word[-1]
'n'
>>> word[-2]
'o'
>>> word[0:2]
'py'
>>> word[2:]
'thon'
>>> word[0: : 2]
'pto'
>>> word[0:]
'python'
>>> word[-2:]
'on'
>>> word[23:]
''
>>> word[2:56]
'thon'
>>> 'J' + word[:]
'Jpython'
>>> s ="Hey there how are you?"
>>> len(s)
22
>>> 
>>> 
>>> 
>>> 
>>> 
>>> squares = [1,2,3,4,5]
>>> squares
[1, 2, 3, 4, 5]
>>> squares[3]
4
>>> squares[2:]
[3, 4, 5]
>>> squres[: : 2] + [11,22,33,444]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    squres[: : 2] + [11,22,33,444]
NameError: name 'squres' is not defined
>>> squares + [22,333,4444]
[1, 2, 3, 4, 5, 22, 333, 4444]
>>> cubes = [1,2,3,4,5,6]
>>> cubes[3] = 90
>>> cubes
[1, 2, 3, 90, 5, 6]
>>> cubes.append(455)
>>> cubes
[1, 2, 3, 90, 5, 6, 455]
>>> 
>>> 
>>> 
>>> letters = ['q' , 'a' , 'c' , 'f' , 'h' , 'm']
>>> letters
['q', 'a', 'c', 'f', 'h', 'm']
>>> letters[2:5] = ['C' , 'F' ,'H']
>>> LETTERS
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    LETTERS
NameError: name 'LETTERS' is not defined
>>> letters
['q', 'a', 'C', 'F', 'H', 'm']
>>> letters[2:5] = []
>>> letters
['q', 'a', 'm']
>>> leters[:] = []
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    leters[:] = []
NameError: name 'leters' is not defined
>>> leters[:] = [ ]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    leters[:] = [ ]
NameError: name 'leters' is not defined
>>> letters[ : ] = []
>>> letters
[]
>>> let = [1,2,3,4,4]
>>> len(let)
5
>>> 
>>> 
>>> a = [1,2,3]
>>> n = [a,s,z]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    n = [a,s,z]
NameError: name 'z' is not defined
>>> n = ['a','s','z']
>>> nesting = [a , n]
>>> nesting
[[1, 2, 3], ['a', 's', 'z']]
>>> nesting[0][2]
3
>>> 
