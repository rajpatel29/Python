#List


numbers = [2 , 4 , 3 ,1 , 66 ,34 , 90]


print("Initial list")
for i in numbers :
    print(str(i) , end = " ")


print()
print()


#Add an item to the end of the list; equivalent to a[len(a):] = [x].
print("append()")
numbers.append(0)

for i in numbers:
    print(str(i) , end = " " )


print()
print()


#Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.
print("extend()")
L = [6,7,8]
numbers.extend(L)

for i in numbers :
    print(str(i) , end = " ")


print()
print()


#Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list,
#and a.insert(len(a), x) is equivalent to a.append(x).
print("insert(i,n)")
numbers.insert(0,99)
numbers.insert(4,44)

for i in numbers :
    print(str(i) , end = " ")


print()
print()


#Remove the first item from the list whose value is x. It is an error if there is no such item.
print("remove(x)")
numbers.remove(44)

for i in numbers :
    print(str(i), end = " ")


print()
print()


#Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
print("pop(x)")
numbers.pop(0)

for i in numbers :
    print(str(i), end = " ")


print()
print()


#Return the index in the list of the first item whose value is x. It is an error if there is no such item.
print("index(x)")
print("element at index 1"+  " is "  + str(numbers.index(1)))


print()
print()


#Return the number of times x appears in the list.
print("count(x)")
print("Number of times 1 appears in list " + str(numbers.count(1)))


print()
print()


#Sort the items
print("sort()")
numbers.sort()

for i in numbers :
    print(str(i) , end = " ")



print()
print()


#Reverse the elements of the list, in place.
print("reverse")
numbers.reverse()

for i in numbers :
    print(str(i) , end = " ")



print()
print()

print("del")
seq = [1,2,3,4,5,6,7]

del seq[3]

for i in seq :
    print(str(i) , end = " ")

print()
print()

del seq[2:4]

for i in seq :
    print(str(i) , end = " ")

print()
print()

del seq[:]

for i in seq :
    print(str(i) , end = " ")


















