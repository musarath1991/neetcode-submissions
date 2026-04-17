class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        queue = deque([0])
        visited = set()

        while queue:
            node = queue.popleft()
            visited.add(node)
            for neigh in adj[node]:
                if neigh not in visited:
                    queue.append(neigh)
        return len(visited) == n
