Python 3.5.1 (v3.5.1:37a07cee5969, Dec  5 2015, 21:12:44) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

 
>>> rutvik = "Hi ther %s, hows your %s"
>>> verbs = ('what \'s up' , 'leg')
>>> print rutvik % verbs
SyntaxError: Missing parentheses in call to 'print'
>>> print (rutvik % verbs)
Hi ther what 's up, hows your leg
>>> another = ('what is up ' , 'foot')
>>> print (rutvik % another)
Hi ther what is up , hows your foot
>>> example = "Hi there my name is rutvik"
>>> example.find('there')
3
>>> 
>>> 
>>> sequence = ['Hi' , 'there' , 'how\'s' , 'dappo']
>>> equence
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    equence
NameError: name 'equence' is not defined
>>> sequence
['Hi', 'there', "how's", 'dappo']
>>> glue = 'glue'
>>> glue.join(sequence)
"Higluetheregluehow'sgluedappo"
>>> example = "I wish I Had A cAr"
>>> example
'I wish I Had A cAr'
>>> example.lower()
'i wish i had a car'
>>> example.upper()
'I WISH I HAD A CAR'
>>> example.replace('HAD' , 'HAVE')
'I wish I Had A cAr'
>>> example.replace('Had' , 'Have')
'I wish I Have A cAr'
>>> 
