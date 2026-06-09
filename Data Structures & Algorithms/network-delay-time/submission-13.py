class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        dist = [float("inf")]*(n+1)
        heap = [(0, k)]
        dist[k] = 0
        while heap:
            curr_time, node = heapq.heappop(heap)
            if curr_time > dist[node]:
                continue
            for neigh, neigh_cost in adj[node]:
                if curr_time + neigh_cost < dist[neigh]:
                    dist[neigh] = curr_time + neigh_cost
                    heapq.heappush(heap, (dist[neigh], neigh))
        res = max(dist[1:])
        return res if res != float("inf") else -1