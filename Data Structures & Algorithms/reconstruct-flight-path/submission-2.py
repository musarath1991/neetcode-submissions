class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for  src, dest in tickets:
            heapq.heappush(adj[src], dest)
        
        res = []
        def dfs(node):
            heap = adj[node]
            while heap:
                next_dest = heapq.heappop(heap)
                dfs(next_dest)
            res.append(node)
        dfs("JFK")
        return res[::-1]