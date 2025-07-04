class Solution:
	def MinSquares(self, n):
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = i
            for x in range(1, int(i**0.5) + 1):
                # recursive case
                dp[i] = min(dp[i], 1 + dp[i - x * x])
        
        return dp[n]