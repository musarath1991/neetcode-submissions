class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        res = []
        def dfs(src):
            heap = adj[src]
            while heap:
                new_src = heapq.heappop(heap)
                dfs(new_src)
            res.append(src)
        dfs("JFK")
        return res[::-1]

