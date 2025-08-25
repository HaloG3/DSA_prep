# Function to generate Fibonacci sequence using memoization

#Memoization is a technique where results are stored to avoid doing the same computations many times. 
# 
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Number of terms in the Fibonacci series
terms = 10

if terms <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci Series:", end=" ")
    for i in range(terms):
        print(fibonacci_memo(i), end=" ")

