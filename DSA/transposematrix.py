
# def transposeMat(matrix):
#     TransposedMatrix = []
#     for col in range(len(matrix[0])):
#         newRow = []
#         newRow.append(col)
#         print(newRow)
#     for row in range(len(matrix)):
#         newCol = []
#         newCol.append(row)
#         print(newCol)
#         # newCol = TransposedMatrix.append(row)

#     return TransposedMatrix[newRow,newCol]

# transposeMat(matrix)

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ] 

# def transposeMat(matrix):
#     TransposedMatrix = []
#     for col in range(len(matrix[0])):
#         newRow = []
#         for row in range(len(matrix)):
#          newRow.append(matrix[col][row])
#         TransposedMatrix.append(newRow)
    
#     print(TransposedMatrix) 

#     return TransposedMatrix

# transposeMat(matrix)



# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# def transposeMat(matrix):
#     transposedMatrix = []

#     for col in range(len(matrix[0])):     # iterate over columns of original
#         # newRow = []
#         for row in range(len(matrix)):    # iterate over rows of original
#             # newRow.append()   # ✅ row first, col second
#          transposedMatrix.append(matrix[row][col])

#     for row in transposedMatrix:
#         print(*row)

#     return transposedMatrix

# transposeMat(matrix)




matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]



#     for col in range(len(matrix[0])):
#        print(transposedMatrix)
#        newRow = []

#        for row in range(len(matrix)):
#           newRow.append(matrix [row][col])
#           print(newRow)
#        transposedMatrix.append(newRow)

#     for row in transposedMatrix:
#             print(*row)

#     return transposedMatrix

# transposeMat(matrix)

def transposeMat(matrix):
    transposedMatrix = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposedMatrix.append(newRow)

    for row in transposedMatrix:
        print(*row)
    return transposedMatrix
transposeMat(matrix)