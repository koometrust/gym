
from functools import reduce
# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item

# a = [1,2,3]
# b = reduce(accumulator, a, 0)
# print(b)

''' 
what is happening inside reduce

 def my_reduce(function, iterable, initializer):
    acc = initializer          # acc starts as your 0
    for item in iterable:
        acc = function(acc, item)   # acc gets REPLACED with the return value
    return acc
'''

def killer(kill, item):
    print(kill, item)
    return kill - item
a = [1,2,3]

print(reduce(killer, a, 5))
