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
        c=binomialCoeff(2*n,n)
        
        return c//(n+1)
    
    