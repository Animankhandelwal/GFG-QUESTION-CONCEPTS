class Solution:
    def longestPalinSubseq(self, s):
        # code here
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    if i + 1 == j:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
        # The final answer is stored in dp[0][n-1]
        return dp[0][n - 1]