
mat1 = [
[5, 1, 2, 0, 7, 8, 2, 1],
[2, 3, 0, 2, 0, 4, 1, 3],
[4, 5, 7, 1, 5, 2, 31,1],
[2, 0, 1, 3, 2, 4, 1, 5],
[2, 4, 2, 1, 1, 2, 3, 4],
[2, 5, 7, 3, 5, 2, 1, 0],
[1, 0, 2, 3, 0, 2, 4, 1],
[4, 0, 5, 1, 3, 7, 4, 2],
]

mat2 = [
[5, 1, 2, 0, 7, 8, 2, 1],
[2, 3, 0, 2, 0, 4, 1, 3],
[4, 5, 7, 1, 5, 2, 31,1],
[2, 0, 1, 3, 2, 4, 1, 5],
[2, 4, 2, 1, 1, 2, 3, 4],
[2, 5, 7, 3, 5, 2, 1, 0],
[1, 0, 2, 3, 0, 2, 4, 1],
[4, 0, 5, 1, 3, 7, 4, 2],
 ]

mat3 = []

# for i = 1 to p do 



for x in range(0, len(mat1)):
    row = []
    for y in range(0, len(mat1[0])):
        total = 0
        for z in range(0, len(mat1)):
            total = total + (mat1[x][z] * mat2[z][y])
        row.append(total)
    mat3.append(row)

for x in range(0, len(mat3)):
    for y in range(0, len(mat3[0])):
        print (mat3[x][y], end=' ')
    print ()