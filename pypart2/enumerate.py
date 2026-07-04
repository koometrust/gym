
for i,char in enumerate({'w','a','s'}): #Hii ndio inabamba
        print(i, char)

# for _ in range(5): #when use forloop wont get random retreival
#     for i,char in enumerate({'w','a','s'}): #Hii ndio inabamba
#         print(i, char,_)

# # for i,char in enumerate(list(range(1,101))): 
# #     print(i, char==50)

for i,char in enumerate(list(range(1,101))): 
    if char == 50:
        print(i)

for i,char in enumerate(list(range(1,101))): 
    print(i,char) 
    if char == 50:
        print(f'waassup we here {i}')

print('1' == 1)