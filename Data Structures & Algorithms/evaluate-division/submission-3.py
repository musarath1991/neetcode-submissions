class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
        
        def bfs(src, dst):
            if src not in adj or dst not in adj:
                return -1
            queue = deque([(src, 1)])
            visited = set()
            visited.add(src)
            while queue:
                node, wt = queue.popleft()
                if node == dst:
                    return wt
                for neigh, weight in adj[node]:
                    if neigh not in visited:
                        queue.append((neigh, wt*weight))
                        visited.add(neigh)
            return -1
        
        res = []
        for u, v in queries:
            res.append(bfs(u, v))
        return res
