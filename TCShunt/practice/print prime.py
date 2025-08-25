def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # only check up to sqrt(num)
        if num % i == 0:
            return False
    return True


def print_primes_upto(n: int):
    """Print all prime numbers from 1 to n."""
    primes = [num for num in range(1, n+1) if is_prime(num)]
    print("Prime numbers from 1 to", n, ":", primes)


# Example usage
print_primes_upto(30)
