#Triplet mutliplication code 
#Wriiten By Jeffin Basil
#Contact : Jeffinbasil@gmail.com
#GitHub : https://github.com/FALLEN-01

import math


# Define the input matrix
#Modify the Matrix Here : 


M = [
    [(1, 1, 1), (4, 5, 6), (4, 5, 6), (4, 5, 6)],
    [(1/4, 1/5, 1/6), (1, 1, 1), (1, 1, 1), (2, 3, 4)],
    [(1/4, 1/5, 1/6), (1, 1, 1), (1, 1, 1), (2, 3, 4)],
    [(1/4, 1/5, 1/6), (1/2, 1/3, 1/4), (1/2, 1/3, 1/4), (1, 1, 1)]
]







rows = len(M)
cols = len(M[0])


R = [[0, 0, 0] for _ in range(cols)]


for col_idx in range(cols):
    PT = [1, 1, 1]
    for row_idx in range(rows):
        a, b, c = M[col_idx][row_idx]
        PT[0] *= a
        PT[1] *= b
        PT[2] *= c

    result_triplet = (
        math.pow(PT[0], (1 / cols)),
        math.pow(PT[1], (1 / cols)),
        math.pow(PT[2], (1 / cols))
    )
    
    R[col_idx][0] = round(result_triplet[0],3)
    R[col_idx][1] = round(result_triplet[1],3)
    R[col_idx][2] = round(result_triplet[2],3)

for row in R:
    print(row)