def Cashiers_algorithm(D, n):
    count = 0
    result = [] # empty list to hold the denominations used
    
    # sort the coin denominations in decreasing order
    
    for coin in D:
        while n >= coin:
            n -= coin
            count += 1
            result.append(coin)
    
    print(result) # print the list of denominations used
    print(sum(result)) # print the list of denominations used
    return count # return the total number of coins used

D = [100,25,10,5,1]

n = 5127

print(Cashiers_algorithm(D,n), "coins needed")
"""
    currentPurse <- 0
    result <- []
    for coin in D:
        while n >= coin:
            n = n - coin
            count = count + 1
            result[count] <- coin
"""
