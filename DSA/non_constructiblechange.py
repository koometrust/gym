# coins = [2,3,5,7,5,1,3,13,200]
# def noChange(coins):
#     coins.sort()
#     print(coins)
#     change = 0
#     for coin in coins:
#         if coin > change + 1:
#             return [f"They cant make{change+1}"]  
#         change += coin
#         print(change)
#     return change + 1    
        
# noChange(coins)           #if coin is > change + 1 return change + 1
 


coins = [5,7,1,1,2,22,3]

def noChange(coins):
    change = 0
    coins.sort()
    print(coins)
    for coin in coins:
        if coin > change + 1:
            print(f"this is the least maximum change we can give {change + 1}")
            return change + 1
        # print(change)
        change += coin
        print(change)

    return change + 1
noChange(coins)
