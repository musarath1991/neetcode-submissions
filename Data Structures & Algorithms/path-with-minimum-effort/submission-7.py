class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float("inf")]*cols for _ in range(rows)]
        heap = []
        heap.append((0, 0, 0))
        while heap:
            diff, r, c = heapq.heappop(heap)
            if r == rows-1 and c == cols-1:
                return diff
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = dr+r, dc+c
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_diff = abs(heights[nr][nc] - heights[r][c])
                    max_diff = max(diff, new_diff)
                    if max_diff < dist[nr][nc]:
                        dist[nr][nc] = max_diff
                        heapq.heappush(heap, (dist[nr][nc], nr, nc))
                    
