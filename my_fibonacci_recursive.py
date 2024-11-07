# def fibonacci(n):
#     if n < 2:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

# Optomized for linear time
def fibonacci(n, memo=None):
    # Initialize dict
    if memo is None: 
        memo = {}
    if n in memo:
        return memo[n]
    # Base case
    if n < 2:
        return n 
    # Recursive case with memoization for time complexity of O(n)
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print(fibonacci(0))  # Output: 0
print(fibonacci(2))  # Output: 1
print(fibonacci(10)) # Output: 55