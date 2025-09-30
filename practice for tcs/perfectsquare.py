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
# for printing list of these
b = 100
lst = [i for i in range(b) if perfectsquare(i)==True]
print('Perfectsquare number are : ',lst)