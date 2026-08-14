class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        p = 0
        c = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    p += 4
                    if i > 0 and grid[i-1][j] == 1:
                        c += 1
                    if j > 0 and grid[i][j-1] == 1:
                        c += 1
        return p - 2*c 