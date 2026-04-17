class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        degree = [0]*(n)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        queue = deque()
        for i in range(n):
            if degree[i] == 1:
                queue.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            size = len(queue)
            remaining_nodes -= size

            for _ in range(size):
                node = queue.popleft()
                for neigh in adj[node]:
                    degree[neigh] -= 1
                    if degree[neigh] == 1:
                        queue.append(neigh)
        return list(queue)