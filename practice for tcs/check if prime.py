
import math 
def prime(n):
    if n <2:
        return False
    for i in range (2, int(math.sqrt(n))+1):
        if n %i ==0:

            return False
    else: 
        return True
print(prime(7))