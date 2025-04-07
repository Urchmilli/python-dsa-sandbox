# fibonacci solution without optimization(without dp) time complexity(2^n)
def fibonacci(n):
    
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

# fibonacci solution with optimization(top-button approach) using recursion and memoization
def fibonacci1(n):
    memo = {}
    if n == 0:
        return 0
    if n == 1: 
        return 1
    if n in memo: 
        return memo[n]

    memo[n] = fibonacci1(n-1) + fibonacci1(n-2)
    
    return memo[n]

# fibonacci solution with optimization(button-top approach) using iteration and array cache
def fibonacci2(n):
    
    dp = [0] * (n+1)
    
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

 
if __name__ == "__main__":
    print(fibonacci(7))
    print(fibonacci1(7))
    print(fibonacci2(7))