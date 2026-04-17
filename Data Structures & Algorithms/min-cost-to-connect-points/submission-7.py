class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)}
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        visited = set()
        heap = [(0, 0)]
        res = 0
        while len(visited) < n:
            dist, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            res += dist
            for neighdist, neigh in adj[i]:
                if neigh not in visited:
                    heapq.heappush(heap, (neighdist, neigh))
        return res