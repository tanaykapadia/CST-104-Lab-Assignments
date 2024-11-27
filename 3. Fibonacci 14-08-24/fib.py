# Lines 4 and 6 in the code are to implement caching of function calls
# Using the memorisation technique, we can reduce the time complexity from exponential to linear

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Enter n:", end = ' ')
n = int(input())
print(f"The n'th term in the fibonacci sequence is: {fibonacci(n-1)}")