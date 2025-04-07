# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.


# solution with optimization(top-button approach)
def min_cost(arr):
    def dp(i):
        
        memo = {}
        if i <= 1:
            return 0
        
        if i in memo:
            return memo[i]
        
        memo[i] = min(dp(i-1)+arr[i-1], dp(i-2)+arr[i-2])
        return memo[i]
    
    return dp(len(arr))

# using  buttom-up approach
def min_cost2(arr):
    n = len(arr)
    dp = [0] * (n+1)
    
    for i in range(2, n+1):
        dp[i] = min(dp[i-1] + arr[i-1], dp[i-2] + arr[i-2])
        
    return dp[n]
    

def solution():
    inps = [([10,15,20], 15), ([1,100,1,1,1,100,1,1,100,1], 6)]
    idx = 0
    for inp, expected in inps:
        result = min_cost2(inp)
        assert result == expected, f"Test{idx} expected: {expected}, returned: {result}"
        print(f"Test{idx} expected: {expected}, returned: {result}") 
        idx +=1


if __name__ == "__main__":
    solution()
    
    