class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
        
        def bfs(source, target):
            if source not in adj or target not in adj:
                return -1
            queue = deque()
            visited = set()
            queue.append((source, 1))
            visited.add(source)
            while queue:
                node, w = queue.popleft()
                if node == target:
                    return w
                for neigh, weight in adj[node]:
                    if neigh not in visited:
                        queue.append((neigh, w*weight))
                        visited.add(neigh)
            return -1

        res = []
        for a, b in queries:
            res.append(bfs(a, b))
        return res