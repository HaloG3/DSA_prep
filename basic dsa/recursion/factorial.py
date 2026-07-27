def factorial(n):
    if n == 0:  # Base case
        return 1
    if n<0:
        return "not valid "
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))


# using lru cache so that we can find slight big numbers esiluy 
from functools import lru_cache # it can stroe all the values that is not ideal 
@lru_cache # for really big numbers 
def fact(num):
    if num==0 or num ==1:
        return 1 
    return num*fact(num-1)


#for really big numbers 
#we use memoisation it will only store last result 
fact_cache = {}
def fact_memo (n):
    if n in fact_cache:
        return fact_cache[n]
    if n ==0 or n==1:
        return 1 
    fact_cache[n] = n* fact_memo(n-1)
    return fact_cache[n]


print(fact_memo(000))
