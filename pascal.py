class Solution:
	def nthRowOfPascalTriangle(self, n):
	    # code here
	    mat=[]
	    for row in range(n):
	        arr=[]
	        for i in range (row+1):
	            if row==i or i==0:
	                arr.append(1)
                else:
                    arr.append(mat[row-1][i-1]+mat[row-1][i])
            mat.append(arr)
        return mat[-1]