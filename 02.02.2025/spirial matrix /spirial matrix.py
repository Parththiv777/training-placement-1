class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for i in range(n)]
        visited = set()
        r,c = 0,0
        rows, cols = n, n
        count = 0 
        counter = 1 
        total = n*n
        while count < total:
            #move to right
            while c < cols and (r,c) not in visited:
                matrix[r][c] = counter
                visited.add((r,c))
                count+=1
                counter+=1
                c+=1
            c-=1
            r+=1
            #move down 
            while r < rows and (r,c) not in visited:
                matrix[r][c] = counter
                visited.add((r,c))
                count+=1
                counter+=1
                r+=1
            r-=1
            c-=1
            #move left 
            while c >= 0 and (r,c) not in visited:
                matrix[r][c] = counter
                visited.add((r,c))
                count+=1
                counter+=1
                c-=1
            c+=1
            r-=1
            #move up 
            while r >= 0 and (r,c) not in visited:
                matrix[r][c] = counter
                visited.add((r,c))
                count+=1
                counter+=1
                r-=1
            r+=1
            c+=1
            
        return matrix


            
            
