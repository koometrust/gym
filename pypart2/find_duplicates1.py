import my_first_gui

some_list = ['a','b','c','d','e','d','f','g','g','d','h','i','g']# d,g,
#find the duplicate return them as a list.
#Set it will remove the duplicates.
#sets has methods that can return the differences.
#List methods that retun duplicates(return)
#moment u change to set. You lose duplicates

# some_list.remove('d')
# print(some_list) #has no return

set_list = set(some_list)
# print(set_list)
new_list = list(set_list)

# woi = set_list.difference(some_list)
#diff cause it returns the diff btwn 2 sets
#how d we make a set with zero duplicates.--it already has zero dups
#use the method to retun set of dups then turn it to a list

# tup_list = 
# tuple(some_list) 
# print(tup_list)
# set
#################################################################################
#old list is an list

# dup_list = []
# for char in new_list:
#     counter = 1
#     for var in some_list:
#         if char == var and counter > 1:
#             print(f'we\'re duplicate {var}')

#         elif char == var:
#             # print('WE\'RE SAME',var)
#             counter+=1


#         # elif char == var and counter > 1:
#         #     print(f'we\'re duplicate {var}')

#         # else:
#         #     print(f'NOT the same, {var}')
     
# print(some_list)
# print(new_list)
# print(dup_list)

#Lists
#################################################################################
dup_list = []
for char in new_list:
    counter = 1
    for var in some_list:
        if char == var and counter > 1:
            print(var)
            if var not in dup_list:
             dup_list.append(var)
            #  print(dup_list)


        elif char == var:
            # print('WE\'RE SAME',var)
            counter+=1
    # dup_list.remove(var)

# print(some_list)
# print(new_list)
print(dup_list)
#################################################################################
some_list = ['a','b','c','d','e','d','f','g','g','d','h','i','g']# d,g

#dup []
# go through list looking for dups for
#add them to dup (if more than twice add to dup)
#worked
#only on entrance into dup
#every time I want something I create a condition
#either remove
#or only add if
#prevention is better than cure

duplicates = []

for itemz in some_list:
    if some_list.count(itemz) > 1:
        if itemz not in duplicates:
          duplicates.append(itemz)
print(duplicates) 

my_first_gui.my_tree()

