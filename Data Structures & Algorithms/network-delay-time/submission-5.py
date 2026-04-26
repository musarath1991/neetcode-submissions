class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, t in times:
            adj[u].append((v, t))
        dist = [float("inf")]*(n+1)
        dist[k] = 0
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for neigh, weight in adj[node]:
                if time + weight < dist[neigh]:
                    dist[neigh] = time + weight
                    heapq.heappush(heap, (dist[neigh], neigh))
        ans = max(dist[1:])
        return ans if ans != float("inf") else -1
