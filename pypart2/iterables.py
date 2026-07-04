#iterate through a Dict
users= {
    'admin':'Collins',
    'npc':'jeff',
    'npc2':'lozzy'

}

for k, v in users.items():
    print(k, v)

#counter   
for num in range(10,0):
    print(num)    

for num in [1,2,3,4,5,6,7,8,9,10]:

    print()

num = [1,2,3,4,5,6,7,8,9,10]
print(sum(num))

counter = 0
for num in range(1,11):   
    counter = counter + num
print(counter)   


for num in range(1,11):   
    counter = sum(range(1,11)) #sum only works with an iterable
print(counter) 