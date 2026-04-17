class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                d = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((d, j))
                adj[j].append((d, i))
        
        res = 0
        visited = set()
        heap = [(0, 0)]
        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neighcost, neigh in adj[i]:
                if neigh not in visited:
                    heapq.heappush(heap, (neighcost, neigh))
        return res