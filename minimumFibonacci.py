class Solution:
    def minimumFibonacci(self, k):
        fib=[1,1]
        while fib[-1]<k:
            fib.append(fib[-1]+fib[-2])
            
        count=0
        
        for i in range (len(fib)-1,-1,-1):
            while k>=fib[i]:
                k-=fib[i]
                count+=1
        
        return count