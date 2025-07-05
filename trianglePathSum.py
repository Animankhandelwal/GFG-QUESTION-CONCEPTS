class Solution:
    def minPathSum(self, triangle):
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[n - 1][i] = triangle[n - 1][i]
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j],
                                                dp[i + 1][j + 1])
        return dp[0][0]