def binomialCoeff(n,k):
    res=1
    if k>n-k:
        k=n-k
        
    for i in range(k):
        res*=(n-i)
        res//=(i+1)
        
    return res

class Solution:
    def catalan(n):
        
        # Calculate value of 2nCn
        c=binomialCoeff(2*n,n)
        
        #return 2nCn/(n+1)
        return c//(n+1)
    
    