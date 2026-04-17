class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)}
        for i in range(n):
            a1, b1 = points[i]
            for j in range(i+1, n):
                a2, b2 = points[j]
                dist = abs(a1-a2) + abs(b1-b2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        res = 0 
        visited = set()
        heap = [[0, 0]]
        while len(visited) < n:
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            res += cost
            visited.add(i)
            for neighcost, neigh in adj[i]:
                if neigh not in visited:
                    heapq.heappush(heap, [neighcost, neigh])
        return res