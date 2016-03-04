
'''
#Using List as stack
stack = [1,2,3]
stack.append(4)

for i  in stack :
    print(str(i), end = " ")

print()
print()

stack.pop()
'''

'''
output
>>> stack.pop()
3
>>> stack.pop()
2
>>> stack.pop()
1
'''


print()
print()


'''
#Using List as Queue
from collections import deque
queue =deque( [1,2,3,4] )
queue.append(5)

for i in queue:
    print(str(i), end = " ")
'''

'''
output
>>> queue.popleft()
1
>>> queue.popleft()
2
>>> queue.popleft()
3

'''


print()
print()



#nested list
matrix = [
            [ 1 , 2 , 3] ,
            [ 2 , 3 , 4] ,
            [ 3 , 4 , 5] ,
        ]


'''
output
>>> matrix
[[1, 2, 3], [2, 3, 4], [3, 4, 5]]
'''




































