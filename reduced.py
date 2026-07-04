from functools import reduce

def killer(kill, num): 
    print(kill, num)
    return kill - num
a = [1,2,3,4,5,5,6,7]

print(reduce(killer, a, 10))