class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(adj[u], v)
        res = []
        def dfs(src):
            heap = adj[src]
            while heap:
                dest = heapq.heappop(heap)
                dfs(dest)
            res.append(src)
        dfs("JFK")
        return res[::-1]