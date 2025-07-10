class Solution:
    def equalPartition(self, arr):
        arrSum = sum(arr)
        n = len(arr)
        if arrSum % 2 != 0:
            return False
    
        arrSum = arrSum // 2
        dp = [[False] * (arrSum + 1) for _ in range(n + 1)]
        # If sum is 0, then answer is true (empty subset)
        for i in range(n + 1):
            dp[i][0] = True
        # Fill the dp table in bottom-up manner
        for i in range(1, n + 1):
            for j in range(1, arrSum + 1):
                if j < arr[i - 1]:
                  
                    # Exclude the current element
                    dp[i][j] = dp[i - 1][j]
                else:  
                    # Include or exclude
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
        return dp[n][arrSum]