
'''

squares_1 = []
for i in range(5) :
    squares_1.append(i * i)


#another way to do the same

squares_2 = [ x ** 2 for x in range(5) ]

#>>> squares_1
#[0, 1, 4, 9, 16]

#>>> squares_2
#[0, 1, 4, 9, 16]

'''


'''

comb_1 = []
for  x in [1,2,3]:
    for y in [1,2,3]:
        if x != y:
            comb_1.append((x,y))


comb_2 =  [(x , y) for x in [1,2,3] for y in [1,2,3] if x!=y]            
        

#>>> comb_1
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

#>>> comb_2
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

'''



vec1 = [-4 , -2 , 0 , 2 , 4]

vec2 = [x * 2  for x in vec1]

vec3 = [x for x  in vec1 if x > 0]

vec4 = [abs(x) for x in vec1 ]

vec5 = [(x , x ** 2 ) for x in range(6)] 

vec = [[1,2,3] , [3,4,5]]

vec6 = [num for ele in vec for num in ele]


#>>vec2
#[-8, -4, 0, 4, 8]

#>>> vec3
#[2, 4]

#>>> vec4
#[4, 2, 0, 2, 4]

#>>> vec5
#[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

#>>> vec6
#[1, 2, 3, 3, 4, 5]



matrix = [
            [1 , 2 , 3] ,
            [4 , 5 , 6] ,
            [7 , 8 , 9] ,

        ]


nest1 = []
for i in range(3):
        transposed_row = []
        for row in matrix:
             transposed_row.append(row[i])
        nest1.append(transposed_row)


#another way to do the same

nest2 = [[row[i] for row in matrix ] for i in range(3)]


#>>> nest2
#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]




