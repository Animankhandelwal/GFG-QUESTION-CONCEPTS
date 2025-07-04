import heapq
class Solution:
   def minCost(self, arr):
    # code here
    heapq.heapify(arr)
    result=0
    while len(arr)>1:
        first=heapq.heappop(arr)
        second=heapq.heappop(arr)
        
        result+=first+second
        
        heapq.heappush(arr,first+second)
    return result