"""
    Task: Buy sell stock algorithm
    Context: Asked in Goldman Sacs
    Category: Algorithm

    Problem Statement: Suppose you have given the stock prices for respective days like 
    (100, 180, 260, 310, 40, 535, 695). The stock price for the 1st day is 100, 
    the 2nd day it is 180 and so on. Write a Python program to determine 
    what days the user should buy and sell the stocks to get the maximum profit.

    In the above case, in the following scenarios user will get maximum profit.
    Buy stock on 1st day (100)
    Sell stock on 4th day (310)
    Buy stock on 5th day  (100)
    Sell stock on 7th day (695)
"""
stocklist = [100, 180, 260, 310, 40, 535, 695]

def local_min(ys):
        # python list compression to generate list of local minima's 
        # include y if all conditions are true
        # enumerate li -> (index, elem), .... (index(n), elem(n))
        # set i = index, y = elem
        # if i == 0 then elem = first element of list 
        # [ logical OR ]
        # if previous elem if greater than or eq to current elem
        # [ Logical AND ]
        # if i == len(ys) - 1, means last elem of the list, no next elem to compare
        # [ logical OR ]
        # current elem is smaller than next elem of the list
        # return y, if all true
    return [ (i, y) for i, y in enumerate(ys) 
                if ((i == 0) or (ys[i - 1] >= y)) 
                and ((i == len(ys) - 1) or (y < ys[i + 1])) 
            ]

def local_max(ys):
    return [ (i, y) for i, y in enumerate(ys) 
                if ((i == 0) or (ys[i - 1] <= y)) 
                and ((i == len(ys) - 1) or (y > ys[i + 1])) 
            ]

def buySellStock():
    buy = local_min(stocklist)
    sell = local_max(stocklist)
    for i, y in enumerate(buy):
        index, price = buy[i]
        print('buy stock on day:', index+1, ", with price:", price)
        index, price = sell[i]
        print('sell stock on day:', index+1, ", with price:", price)

if __name__ == "__main__":
    buySellStock()

"""
Output>>>
    buy stock on day: 1 , with price: 100
    sell stock on day: 4 , with price: 310
    buy stock on day: 5 , with price: 40
    sell stock on day: 7 , with price: 695
"""