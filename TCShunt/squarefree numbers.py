'''
question
Square Free Number
In the theory of numbers, square free numbers have a special place. A square free number is one that is not divisible by a perfect square (other than 1).
Thus 72 is divisible by 36 (a perfect square), and is not a square free number, but 70 has factors 1,2,5,7,10,14,35 and 70. As none of these are perfect squares (other than 1),70 is a square free number
For some algorithms, it is important to find out the square free numbers that divide a number. Note that 1 is not considered a square free number.

In this problem, you are asked to write a program to find the number of square free numbers that divide a given number.

Input Format:
The only line of the input is a single integer N which is divisible by no prime number larger than 19


Approach
The given program does this:

Loop through all numbers i from 2 to n/2.

Check if i is a divisor of n.

If yes, initially assume it is valid (count += 1).

Check if i itself is a perfect square → if yes, exclude it (count -= 1).

Keep a list temp of all perfect square divisors found so far.

For every divisor i, also check if it is divisible by any perfect square divisor stored in temp.
If yes → exclude it (count -= 1).

Finally, print the count.




Find Factors of Any Number
def get_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

# Example
print(get_factors(72))  # [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 36, 72]

'''


import math

def main():
    # Input the number 'n'
    n = int(input())
    
    # Initialize variables
    temp = []  # List to store perfect square divisors
    count = 0  # Variable to count valid divisors
    
    # Loop through all numbers from 2 to n/2
    for i in range(2, n // 2 + 1):
        # Check if 'i' is a divisor of 'n'
        if n % i == 0:
            count += 1  # Increment count since 'i' is a divisor
            sqnum = math.sqrt(i)  # Calculate square root of 'i'
            chksqr = int(sqnum)  # Convert the square root to an integer
            
            # Check if 'i' is a perfect square
            if chksqr == sqnum:
                count -= 1  # If 'i' is a perfect square, reduce count
                temp.append(i)  # Store the perfect square divisor
            else:
                # Check if 'i' is divisible by any previously found perfect square divisors
                for k in range(len(temp)):
                    if i > temp[k] and len(temp) != 0:
                        if i % temp[k] == 0:
                            count -= 1  # If 'i' is divisible by a perfect square, reduce count
                            break  # Exit the loop if condition met
                    else:
                        break  # Exit the loop if no need to check further
                
    # Output the count of divisors excluding perfect squares and their multiples
    print(count)

# Call the main function
if __name__ == "__main__":
    main()
