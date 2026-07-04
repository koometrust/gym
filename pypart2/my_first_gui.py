# tree = [
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0],
#     [0,1,1,1,1,1,0],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0]

# ]
# for rows in tree:
#     for pixel in rows:
#         if pixel == 0:
#          print(' ', end=" ")
#         else:
#          print('*', end=" ")
#     print(" ")
# tree = [0,0,0,1,0,0,0]
# for item in tree:
#     if item == 0:
#         print('10')
#     else:
#         print('*')





image = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]

]
zero = '$'
one = " "
def my_tree():
 for listz in image:
    for pixel in listz:
        if (pixel == 0):
            print(zero, end='')
        else:
            print(one ,end = '')

    # print("/n")
    print()

my_tree()
my_tree()
my_tree()
my_tree()