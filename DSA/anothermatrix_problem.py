matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 8, 9]



]

# Print all elements in spiral order (clockwise from outside in):
# Expected output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
# Before writing any code, answer these in plain English:

# What are the four directions you move in?
# When do you change direction?
# What data structure holds your result?

#the directions I will move in are right from 1 to 3 it will be a normal nested for loop newRow[] will reset
#  after we collect all the values in the row and add them to the spiral array. 
# down from 3-9 for col in matrix[2]
#left from 9-7 for row in matrix[2, -1] 
#up from 7-4 for col in matrix[0, 1, -1] #trying to start stop and stepover(0 being the column,stop at 1 the center of the the column where element 4 is, and -1 is to reverse it so it can start from the bottom of the column & come up)
#then right straight into the centre, 4-5 for row in # Question?? if I say smatrix[0] it will start doing the columns, so how am I supposed to access 
def spiraly(matrix):
    spiral = []
    for row in range(len(matrix[row][col])): #trying to add a start stop so it can end at 
         giveToSpiral = []
         for col in range(len(matrix)):
              giveToSpiral.append(matrix[row][col])
            
    # for col in range(matrix[2]):
    #           giveToSpiral.append(matrix[row][col])

    for x in spiral:
         print(x)
    return spiral
spiraly(matrix)
            
            #I also had the idea of upacking the matrix like the tournament example
            # e.g  
            # 
            # first,second, third 
            # first,second, third 
            # first,second, third 
            # for row in range(len(matrix[row][col])):
            #   first,second, third = row 
            # giveToSpiral.append(first,second,third)

# Kindly guide my intuition