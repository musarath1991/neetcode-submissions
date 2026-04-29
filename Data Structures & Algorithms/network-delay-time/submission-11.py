class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        heap = [(0, k)]
        dist = [float("inf")]*(n+1)
        dist[k] = 0
        while heap:
            time, node = heapq.heappop(heap)
            for neigh, cost in adj[node]:
                if time + cost < dist[neigh]:
                    dist[neigh] = time + cost
                    heapq.heappush(heap, (dist[neigh], neigh))
        
        res = max(dist[1:])
        return res if res != float("inf") else -1