class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
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
        while len(visited) < len(points):
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue
            res += cost
            visited.add(node)
            for dist, neigh in adj[node]:
                if neigh not in visited:
                    heapq.heappush(heap, (dist, neigh))
        return res