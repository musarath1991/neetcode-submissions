class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        p, connections = 0, 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    p += 4
                    if r < rows-1 and grid[r+1][c] == 1:
                        connections += 1
                    if c < cols-1 and grid[r][c+1] == 1:
                        connections += 1
        return p - 2*connections