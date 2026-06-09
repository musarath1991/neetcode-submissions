class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        res = []
        def dfs(node):
            heap = adj[node]
            while heap:
                new_node = heapq.heappop(heap)
                dfs(new_node)
            res.append(node)
        dfs("JFK")
        return res[::-1]