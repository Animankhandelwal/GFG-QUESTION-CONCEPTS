class Solution:
    def waterOverflow(self, K, R, C):
        # code here 
        memo=[[0.0 for _ in range(R)] for _ in range(R)]
        memo[0][0]=K
        for row in range(R-1):
            for col in range(row+1):
                excess=max(0.0, memo[row][col]-1.0)
                if excess >0:
                    memo[row][col]=1.0
                    memo[row+1][col]+=excess/2
                    memo[row+1][col+1]+=excess/2
        return min(1.0,memo[R-1][C-1])