list = [32, 2,45,67,86,34,2,78,104,56,78]
#find max even in list
#find even then Find max among the even

# evens = []
# def even_maker(list):
#     for num in list:
#         if num % 2 == 0:
#             evens.append(num)

# even_maker(list)

# print('all evens',evens)
# evens.sort(reverse=True)
# print(evens[0])


#### as 1 function
def even_maker(list):
    evens = []
    for num in list:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)

print(even_maker(list))

# print('all evens',evens)
# evens.sort(reverse=True)
# print(evens[0])