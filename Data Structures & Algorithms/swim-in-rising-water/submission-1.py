class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        visited = set()
        heap.append((grid[0][0], 0, 0))
        visited.add(grid[0][0])
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == n-1 and c == n-1:
                return t
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr, nc = dr+r, dc+c
                if 0 <= nr < n and 0 <= nc < n:
                    heapq.heappush(heap, (max(grid[nr][nc], t), nr, nc))
