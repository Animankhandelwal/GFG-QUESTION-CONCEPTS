class Solution:
    def countPS(self, s):
        # code here
        n=len(s)
        res=0
        dp=[[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = True
    
        # Two length string is palindrome if
        # both characters are same
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1
    
        # Handle palindromes of length 
        # greater than 2 (gap >= 2)
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
    
                # Check if the current string is a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    res += 1
    
        return res