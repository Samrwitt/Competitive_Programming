from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        largestLocal = [[0] * (n - 2) for _ in range(n - 2)]
        
    
        for i in range(1, n - 1):
            for j in range(1, n - 1):
               
                max_value = max(
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[i][j-1], grid[i][j], grid[i][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]
                )
                largestLocal[i-1][j-1] = max_value
        
        return largestLocal
 