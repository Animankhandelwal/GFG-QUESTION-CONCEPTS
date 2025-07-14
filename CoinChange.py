class Solution:
    def count(self, coins, sum):
        # code here 
        n = len(coins)
        dp = [0] * (sum + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(coins[i], sum + 1):
                dp[j] += dp[j - coins[i]]
                
        return dp[sum]