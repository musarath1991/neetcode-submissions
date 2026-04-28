class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(adj[u], v)
        
        res = []
        def dfs(source):
            heap = adj[source]
            while heap:
                dst = heapq.heappop(heap)
                dfs(dst)
            res.append(source)
        dfs("JFK")
        return res[::-1]