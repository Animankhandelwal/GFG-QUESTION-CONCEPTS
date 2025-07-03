class Solution:
    def solve(self, n, p ,a, b, d): 
        #code here
        outgoing = [-1] * (n + 1)
        incoming = [-1] * (n + 1)
        diameter = [float('inf')] * (n + 1)
        # Building graph representation
        for i in range(p):
            outgoing[a[i]] = b[i]
            incoming[b[i]] = a[i]
            diameter[a[i]] = d[i]
    
        result = []
        # DFS to find tank-tap connections
        for i in range(1, n + 1):
            
            # Tank found
            if outgoing[i] != -1 and incoming[i] == -1: 
                curr, minDia = i, float('inf')
                
                while outgoing[curr] != -1:  
                    
                    minDia = min(minDia, diameter[curr])
                    
                    # Move to next house
                    curr = outgoing[curr] 
                
                # Store (tank, tap, min diameter)
                result.append([i, curr, minDia]) 
        return result