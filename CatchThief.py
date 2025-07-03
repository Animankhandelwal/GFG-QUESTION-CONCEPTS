class Solution:
    def catchThieves(self, arr, k):
        #code  here
        n= len(arr)
        i,j=0,0
        count=0
        
        while i<n and j<n:
            # to find the police
            while i<n and arr[i]!='P':
                i+=1
            # to find the thief
            while j<n and arr[j]!='T':
                j+=1
            # if the police can catch the thief(within k)
            if i<n and j<n and abs(i-j)<=k:
                count+=1;
                i+=1
                j+=1
            # if the thief is far left then
            elif j<n and j<i:
                j+=1
            # if the police is far left
            elif i<n and i<j:
                i+=1
        return count