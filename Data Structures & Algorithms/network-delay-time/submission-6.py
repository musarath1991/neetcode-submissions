class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
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
            for neigh, time in adj[node]:
                if time + t < dist[neigh]:
                    dist[neigh] = t + time
                    heapq.heappush(heap, (neigh, dist[neigh]))
        
        res = max(dist[1:])
        return res if res != float("inf") else -1


