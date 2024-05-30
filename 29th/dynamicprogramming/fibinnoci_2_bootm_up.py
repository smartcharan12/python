#bottom up solution
#complexity O(n) befor recuursion 2 power n
def fibonacci_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)#array of size n+1 with all values as 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fibonacci_tab(20575))  # Output: 