outcnt = 0 # initialize a counter for counting the pair of prime numbers 
h = 24
r = 12

lst = [i+1 for i  in range(24)]
def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # only check up to sqrt(num)
        if num % i == 0:
            return False
    return True

lstt = [lst[i:i + r] for i in range(0, h, r)]
for i in (lstt[-1]):
    if lstt[-1][i]== is_prime:
        print(lst[-1][i][i])

   
    
print(lstt)

   

