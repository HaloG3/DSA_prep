import math 
s = input('Enter the string: ')
def allsubs(s):
    n = len(s)
    substring = set()
    # generate all substing 
    for i in range(n):
        for j in range(i+1, n+1):
            substring.add(s[i:j])
    return list(substring)

print(allsubs(s))