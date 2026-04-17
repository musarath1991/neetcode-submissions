class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float("inf")]*cols for _ in range(rows)]
        dist[0][0] = 0
        heap = []
        heap.append((0,0,0))
        while heap:
            wt, r, c = heapq.heappop(heap)
            if r == rows-1 and c == cols-1:
                return wt
            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr, nc = dr+r, dc+c
                if 0 <= nr < rows and 0 <= nc < cols:
                    curr_wt = abs(heights[nr][nc] - heights[r][c])
                    max_wt = max(curr_wt, wt)
                    if max_wt < dist[nr][nc]:
                        dist[nr][nc] = max_wt
                        heapq.heappush(heap, (max_wt, nr, nc))
        return 0
            