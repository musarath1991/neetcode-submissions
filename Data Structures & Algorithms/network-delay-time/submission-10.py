class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        dist = [float("inf")]*(n+1)
        dist[k] = 0
        heap = [(0, k)]
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for neigh, cost in adj[node]:
                if cost + time < dist[neigh]:
                    dist[neigh] = cost + time
                    heapq.heappush(heap, (dist[neigh], neigh))
        res = max(dist[1:])
        return res if res != float("inf") else -1