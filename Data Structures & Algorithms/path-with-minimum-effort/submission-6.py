class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float("inf")]*cols for _ in range(rows)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            diff, r, c = heapq.heappop(heap)
            if r == rows-1 and c == cols-1:
                return diff
            for dr, dc in [(-1, 0),(1, 0), (0, 1),(0, -1)]:
                nr, nc = dr+r, dc+c
                if 0 <= nr < rows and 0 <= nc < cols:
                    difference = abs(heights[nr][nc] - heights[r][c])
                    new_diff = max(diff, difference)
                    if new_diff < dist[nr][nc]:
                        dist[nr][nc] = new_diff
                        heapq.heappush(heap, (new_diff, nr, nc))
        return 0


