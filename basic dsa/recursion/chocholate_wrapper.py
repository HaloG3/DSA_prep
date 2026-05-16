'''
Given three values money, price, and wrap, the task is to find the total number of chocolates you can eat.
 Here money defines the total amount of money you have, price is the cost of buying a single chocolate and wrap
   defines the number of wrappers that can be returned to get one extra chocolate.
'''

def count(money ,price, wrap):
    if money <price:
        return 0
    choco = money//price 

    choco = choco + (choco-1) //(wrap-1)
    return choco
print( count(30 , 2,3))

