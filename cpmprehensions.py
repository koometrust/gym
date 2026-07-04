# new_list = [item for item in range(10) if item % 3 == 0]
# print(new_list)

a = [1,2,3,4,5,5,6,7]
# set_a  = set(a) 
# print(a)
# print(set_a)

unique_doubled = {item*2 for item in a}
print(unique_doubled)

wordso = ["cat", "tiger", "ox", "lion"]
word_lengths = { len(word): word for word in wordso}
print(word_lengths)
