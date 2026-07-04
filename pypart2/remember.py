# print("Hello jude")

# print(range(10))
# print(range(10))

# # for x in range(10):
# #     print(x)
# # list = range(1,10)
# # for x in list:
# #     print(x)



# # for x in range(1,11):
# #  print(x)


# conter =sum(range(1,11))
# print(conter)

# # add_to_set ={1,2,3,4} 
# # number = int(input("Give me a number?"))
# # add_to_set.add(number)
# # print(add_to_set)

# list = [1,2,3,4,5]
# number = int(input("Give me a number?"))
# # no sets only add unique numbers
# # only add dups
# if list.count(number) > 0:
#     list.append(number)

# print(list)


# jude = [1,2,3,4,5]
# k = ['a','b','c','d','e','f']
# m = [3,4,5,6,7,8]
# picture = [

#    [1,1,1,0,1,1,1],
#    [1,1,0,0,0,1,1],
#    [0,0,0,0,0,0,0],
#    [1,1,1,0,1,1,1],
#    [1,1,1,0,1,1,1],
#    [1,1,1,0,1,1,1]
          
#    ]

# for line in picture:
#     for pixel in line:
        
        
#      if pixel == 1:
#         print(" ", end = " ")
#      else:
#         print("+", end = " ")


#     print(end = "\n")


#     # for y in image:
#     #  if x == 1:
#     #   print("meow")

# for i,char in enumerate(list(range(1,55))):
#     if char == 50:
#      print(i, char)

# dict = {
#     "jude": 5, 
#     "koome": 6
#     }

# for k,v in dict.items():
#   print(k)

# person = {"name": "jude", "age": 21}
# print(person["name"])
# print(person["name"])

# person.update({"name": 5 ,"year": 2022})
# print(person)

# newname = person.pop("age")
# newname = newname * 2
# person.update({"newkey":newname})
# print(person)

my_dict = {"name": "Alice", "age": 25}
my_dict["years"] = my_dict.pop("age")  # Key "age" becomes "years"
print(my_dict)