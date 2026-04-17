class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr, nc = dr+r, dc+c
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)
        
        for r in range(rows):
            dfs(r, 0, pacific)
        
        for c in range(cols):
            dfs(0, c, pacific)
        
        for r in range(rows):
            dfs(r, cols-1, atlantic)
        
        for c in range(cols):
            dfs(rows-1, c, atlantic)

        return list(pacific & atlantic)