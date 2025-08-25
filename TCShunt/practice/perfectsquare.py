def perfectsq(n):
    if n<1:
        return False
    if n ==1 :
        return True
    if (n**0.5) in  range (1,int(n/2)+1):
        return True
    else: 
        return False
print(perfectsq(1))