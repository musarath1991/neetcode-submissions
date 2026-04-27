class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in tickets:
            heapq.heappush(adj[u], v)
        res = []
        def dfs(source):
            heap = adj[source]
            while heap:
                new_dest = heapq.heappop(heap)
                dfs(new_dest)
            res.append(source)
        dfs("JFK")
        return res[::-1]