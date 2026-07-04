cache_dic = {}
from functools import lru_cache
@lru_cache(maxsize=one)
def square(n):
    if n in cache_dic:
        print("Using Cached value {n}....")
        return cache_dic[n]
    else:
        print(cache_dic)
        print("Calculating new value....")
        result = n * n
        cache_dic[n] = result
        return result
    

print(square(45))
print(cache_dic)
print(square(45))
print (square(12))
print(cache_dic)
print(square(12))