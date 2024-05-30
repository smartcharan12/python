def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}#dictoranry
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

print(fibonacci_memo(1.2))  # Output: 55