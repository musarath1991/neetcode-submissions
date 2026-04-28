class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if r == n-1 and c == n-1:
                return time
            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr, nc = dr+r, dc+c
                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        new_time = max(time, grid[nr][nc])
                        heapq.heappush(heap, (new_time, nr, nc))
        return 0