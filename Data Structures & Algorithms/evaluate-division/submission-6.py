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
            visited = set()
            queue = deque()
            visited.add(src)
            queue.append((src, 1))
            while queue:
                node, prod = queue.popleft()
                if node == dst:
                    return prod
                for neigh, cost in adj[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh, prod*cost))
            return -1
        res = []
        for a, b in queries:
            res.append(bfs(a,b))
        return res