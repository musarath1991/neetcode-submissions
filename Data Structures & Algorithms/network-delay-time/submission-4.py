class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, w in times:
            adj[u].append((v, w))
        dist = [float("inf")]*(n+1)
        dist[k] = 0
        heap = []
        heap.append((k, 0))
        while heap:
            node, t = heapq.heappop(heap)
            if t > dist[node]:
                continue
            for neigh, weight in adj[node]:
                if t + weight < dist[neigh]:
                    dist[neigh] = t + weight
                    heapq.heappush(heap, (neigh, dist[neigh]))
        ans = max(dist[1:])
        return ans if ans != float("inf") else -1
