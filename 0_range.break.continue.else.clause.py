

#range
for i in range(5):
    print(i)

print()    
print()

for i in range(3 , 10):
    print(i)

print()
print()


for i in range(0 , 10 , 2):
    print(i)

print()
print()
    
for i in range(0 , -10 , -2):
    print(i)

print()
print()


#else clause

for  i in range (4): 
    for j in range(4) :
        print ("i " + str(i) + " j: " + str(j))

    else:
        print("In else clause")
        

print()
print()



#break
#Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or when the condition becomes false (with while),
#but not when the loop is terminated by a break statement.

for  i in range (4): 
    for j in range(2, 5) :
        if(i==j):
            print ("i " + str(i) + " j: " + str(j))
            break
    else:
        print("In else clause")
            

print()
print()

#continue
for i in range(10):
    if (i%2 != 0) :
        continue
    print( str(i) + " is even number")
        

        
