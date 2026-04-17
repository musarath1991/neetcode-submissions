class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        p = 0
        shared = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    p += 4
                    if r < rows-1 and grid[r+1][c] == 1:
                        shared += 1
                    if c < cols-1 and grid[r][c+1] == 1:
                        shared += 1

        return  p - 2*shared