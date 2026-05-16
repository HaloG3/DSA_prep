def factorial(n):
    if n == 0:  # Base case
        return 1
    if n<0:
        return "not valid "
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))