class Solution:
    def maxHeight(self,height, width, length):
        #Code here
        n=len(height)
        boxes=[]
        for i in range(n):
            a, b, c=height[i], width[i], length[i]
            boxes.append([a,b,c])
            boxes.append([a,c,b])
            boxes.append([b,a,c])
            boxes.append([b,c,a])
            boxes.append([c,a,b])
            boxes.append([c,b,a])
            
        boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)
        dp=[0]*len(boxes)
        ans=0
        for i in range(len(boxes)-1,-1,-1):
            dp[i]=boxes[i][2]
            for j in range(i+1, len(boxes)):
                if boxes[i][0]>boxes[j][0] and boxes[i][1]>boxes[j][1]:
                    dp[i]=max(dp[i], boxes[i][2]+dp[j])
            ans=max(ans, dp[i])
        return ans