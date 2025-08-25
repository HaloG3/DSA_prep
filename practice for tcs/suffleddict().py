'''
Step 1 – Construct the reference dictionary

We’ll assume you want all characters with their first appearance order (stable ordering).
Example:

reference = "hello"
order_dict = {ch: idx for idx, ch in enumerate(reference)}
print(order_dict)  
# {'h': 0, 'e': 1, 'l': 3, 'o': 4}

Step 2 – Sort another string by this mapping

We use Python’s sorted() with a custom key function that looks up each character’s order in the dictionary.

target = "olehl"

# sort according to order_dict
sorted_list = sorted(list(target), key=lambda ch: order_dict[ch])
print(sorted_list)  
# ['h', 'e', 'l', 'l', 'o']

Step 3 – Convert back into a string
result = "".join(sorted_list)
print(result)  
# "hello"

later in answer we handle the input logic according to the question 
'''


def new_str(p,s):
    res = {ch: idx for idx, ch in enumerate(list(p))}
    s_l = sorted(list(s), key = lambda ch: res[ch])
    result = ''.join(s_l)
    return result

T  = int(input())
results =[]
for _ in range(T):
    p= input()
    s= input()
        
    result =  new_str(p,s)
    results.append(result)
        
for ans in results:
    print(ans)
        

#####
# look sort but same shit bro 
n=int(input())
for _ in range(n):
    a=input()
    b=input()
    c=""
    l=[]
    for i in b:
        if i in a:
            ind=a.index(i)
            l.append(ind)
    l.sort()
    for i in l:
        c+=a[i]
    print(c)