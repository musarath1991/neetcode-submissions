class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(len(points)):
            a1, b1 = points[i]
            for j in range(i+1, len(points)):
                a2, b2 = points[j]
                dist = abs(a1-a2) + abs(b1-b2)
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        visited = set()
        heap = [(0, 0)]
        res = 0
        while len(visited) < n:
            dist, pt = heapq.heappop(heap)
            if pt in visited:
                continue
            res += dist
            visited.add(pt)
            for neigh, cost in adj[pt]:
                if neigh not in visited:
                    heapq.heappush(heap, (cost, neigh))
        return res
