lst = [22 ,44,6+49,77,33]
def hcf(numbers):
    numbers = [abs(num) for num in numbers if num!=0]

    if not numbers:
        return 0
    
    smallest = min(numbers)
    factors = set()
    for f in range(1, int(smallest**0.5)+1):
        if smallest %f == 0:

            factors.add(f)
            factors.add(smallest//f)

        hcf_f = 1
        for f in sorted (factors, reverse = True):
            if all(num %f == 0 for num in numbers):
                hcf_f = f
                break

    
    return hcf

    
lst= [22,44,55,66]

print(hcf((lst)))

    
from functools import reduce 
def gcd(a,b):
    a,b = abs(a), abs(b)
    while b:
        a,b = b, a%b
        return a 
def hcf_best(numbers):
    numbers = [abs(num) for num in numbers if num != 0 ]
    if not numbers:
        return 0
    return reduce (gcd,numbers)
print('hcf os ', hcf_best(lst))

        
    
        
