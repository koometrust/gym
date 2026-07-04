# def sum(num1, num2):
#     def another_func(num1,num2):
#         return num1+num2

# print(sum(anoth))

# my_dict = {"name": "Alice", "age": 25}
# my_dict["years"] = my_dict.pop("age")  # Key "age" becomes "years"

# nums = [1,2,3,4,5,6,7]
# target = 

# # x + y = target
# # 8 - y = x 


# x = 0
# for y in nums:

#     x = target - y 
# print(x, y)


# num = [2, 7, 11, 15]
# nums = [2, 7, 11, 15]

# target = 26
# # target - y = x
# y = 0
# def two_sum():
#  for i, x in enumerate(num):
#     for j, y in enumerate(nums):
#         if x + y == target:
#             print(f"this is x {i} & This is j {j}")
#             return
    
# two_sum()

# num = [2, 7, 11, 15]
# target = 26
# for k, v in enumerate(num):
#     x = 0
#     x = target - v
#     if v + x == target:
#         print(k)
          

 
# # print (type(dict_num))
# print(type(num))

# FUNCTION twoSum(nums, target):
#     CREATE an empty hash map named seen_numbers

#     FOR each INDEX, VALUE in nums:
#         COMPUTE complement = target - VALUE
        
#         IF complement EXISTS in seen_numbers:
#             RETURN [ seen_numbers[complement], INDEX ]
            
#         STORE VALUE in seen_numbers with INDEX as its value
        
#     RETURN empty list (if no solution is found)

nums = [2, 7, 11, 15]
target = 28
def two_sum(nums, target):
  seen_numz = {}
  for k,v in enumerate(nums):
    complement = target - v 
    if complement in seen_numz:
      print(seen_numz(complement, k)) 
      seen_numz.update(k)
    # return  seen_numz = {}

two_sum(nums, target)
