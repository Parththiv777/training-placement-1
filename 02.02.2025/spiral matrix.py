class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        num = 1
        i, j = 0,  0
        matrix = []
        for _ in range(n):
            matrix.append([0]*n)
        while(i>=0 and i<n and j>=0 and j<n and num <= n*n and matrix[i][j]==0):
            # right i, j+=1
            while(j < n and num<=n*n and matrix[i][j]==0):
                matrix[i][j] = num
                num += 1
                j+=1
            j-=1
            i+=1
            # down i+=1, j
            while(i < n and num<=n*n and matrix[i][j]==0):
                matrix[i][j] = num
                num += 1
                i+=1
            i-=1
            j-=1
            # left i, j-=1
            while(j >=0 and num<=n*n and matrix[i][j]==0):
                matrix[i][j] = num
                num += 1
                j-=1
            j+=1
            i-=1
            # up i-=1, j
            while(i >=0 and num<=n*n and matrix[i][j]==0):
                matrix[i][j] = num
                num += 1
                i-=1
            i+=1
            j+=1
        return matrix
