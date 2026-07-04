def twoSum():
        nums = [2,3,4,5,1,7]
        target = 6
        seen = {}
        for idx, num in enumerate(nums):
            # key = num
            # value = idx
            # print(idx, num)
            y = target - num
            if y in seen: #in retrievs keys in seen dict k:v -> num:idx
                print(f"{y} has been found for {num} to give us {target}") 
                return[seen[y], idx]

            seen[num] = idx #storing
            print(seen)

twoSum()

# # what I'm tracking 
# # what I'll be asked for 
# nums = [2,3,4,5,1,7]
# target = 6
# seen = {}
# def twoSum():
#      nums = [2, 3, 4, 5, 1, 7]
#      target = 7
#      seen = {}

#      for idx, num in enumerate(nums):

#       key = num
#       value = idx

#       complement = target - num # what I'm tracking 

#       if complement in seen:
#           print(complement)
#           return[seen[idx], idx]
      
#       seen[key] = value #store
#       print(seen)
# twoSum()         

# def twoSum():
#     nums = [2, 3, 4, 5, 1, 7]
#     target = 9
#     record = {}

#     for idx, num in enumerate(nums):   # unpack (index, value) from enumerate
#         key   = num                    # what I'm tracking → the number
#         value = idx                    # what I need later → where it was
#         complement = target - num      # what I'm looking for

#         if complement in record: 
#             print(f"{complement} has been found for {num} to give us {target}" )      # ask first
#             return [record[complement], idx]

#         record[key] = value  # then store 
#         print(record)      

# twoSum()