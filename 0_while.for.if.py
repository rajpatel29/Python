#while
#Fibonacci series
a,b = 0 ,1
while b < 10 :
    print(b)
    a = b
    b = a + b

print()
print()

#see the difference
a,b = 0 ,1
while b < 10 :
    print(b)
    a , b = b ,  a + b    
    
print()
print()





#if , else if
x  = int(input("Please Enter a integer: "))
if(x < 0):
    print("You entered negative value")
elif(x <10):
    print("You entered between 0 to 10")
else:
    print("you entered greater than 10")

print()
print()   






#for
#The for statement in Python differs a bit from what you may be used to in C or Pascal. Rather than always iterating over an arithmetic progression of numbers (like in Pascal),
#or giving the user the ability to define both the iteration step and halting condition (as C), Python’s for statement iterates over the items of any sequence
#(a list or a string), in the order that they appear in the sequence. 

words = ['cat' , 'food' , 'apple']
for word in words :
    print(word + " "  + str(len(word)) )

print()
print()

seq = [1,2,3,4,5,6,7,8]
for i in seq[::3] :
    print(i)

print()
print()

#another way to do the same
seq = range(8)
for i in seq:
    print(i)
    
