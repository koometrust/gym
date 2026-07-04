# a = [6,5,4,2,7,1]
# def squarer(num):
#     return num * num

# b = list(map(squarer, a))
# print(a)
# print(b)
# b.sort()
# print(b)

# print(map(squarer, a))

# def even_num(numz):
#     for num in numz:
#         return  num % 2 == 0
            
def even_num(num):
    return num % 2 == 0
 
numz = list([144,5,4,2,7,1])
print(list(filter(even_num,numz)))

print(numz)
# print(b)