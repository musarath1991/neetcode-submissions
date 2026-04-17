class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, w in times:
            adj[u].append((v,w))
        dist = [float("inf")]*(n+1)
        dist[k] = 0
        heap = []
        heap.append((0, k))
        while heap:
            curr_time, node = heapq.heappop(heap)
            if curr_time > dist[node]:
                continue
            for neigh, weight in adj[node]:
                if curr_time + weight < dist[neigh]:
                    heapq.heappush(heap, (curr_time + weight, neigh))
                    dist[neigh] = curr_time + weight
        ans = max(dist[1:])
        return ans if ans != float("inf") else -1
        