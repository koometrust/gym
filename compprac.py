
# squared_num = [num*2 for num in range(10) if num % 3 == 0]  
# print(squared_num)

# words = ["hello","jude","mcoastie"]

# wordsy = { word:len(word) for word in words}
# print(wordsy)

# fives = { key for key, value in wordsy.items() if value == 5} 
# print(fives)

# super_hero = {
#     'age': 57,
#     'powers': ['flight', 'ice_breath', 'super_hearing'],
#     'name': 'jude_koome'

# }

# a = [1,2,3,4,5]
# renamer = [8 if i == 5 else i for i in a]
# print(f"{renamer}")
# print(a)


# key value maker from list
letters = ['f','e','d','c','b','a','a','b']

duplicates = set([letter for letter in letters if letters.count(letter) > 1])
print(duplicates)


a = ['f','e','d','c','b','a','a','b']
# def duplicates():
dups = []
for letter in a:
        if a.count(letter) > 1 and letter not in dups:
            dups.append(letter)
    
    
print(dups)

x = "hello"[0]
print(x)