
# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
# it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.
from functools import cache
# using top-buttom approach memoisation and recursion
def solution(nums):
    @cache
    def dp(i):
        # Base cases
        if i == 0:
            return nums[0]
        if i == 1: 
            return max(nums[0], nums[1])
        

        
        # Reoccurrence relation
        return max(dp(i - 1), dp(i - 2) + nums[i])
    
    return dp(len(nums) - 1)

def solution2(nums):
    # To avoid out of bound error from setting base case
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    dp = [0] * n
    
    # Base Cases
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    
    for i in range(2, n):
        # Recurrence relation
        dp[i] = max(dp[i -1], dp[i - 2] + nums[i])
        
    return dp[n-1]

def test_soln():
    inps = [([1,2,3,1], 4), ([2,7,9,3,1], 12)]
    index = 0
    for input, expected in inps:
        result = solution(input)
        assert result == expected, f"Test{index}, expected: {expected}, got: {result}"
        print(f"Test{index}, expected: {expected}, got: {result}")
        index += 1
        
if __name__ == "__main__":
    test_soln()
    
    