class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r > rows-1 or c > cols-1 or grid[r][c] == "0":
                return 0
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands