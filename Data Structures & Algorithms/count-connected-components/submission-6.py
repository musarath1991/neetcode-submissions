class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs_helper(node, visited):
                visited[node] = True
                for neigh in adj[node]:
                    if not visited[neigh]:
                        dfs_helper(neigh, visited)
        def dfs(start):
            visited = [False]*n
            dfs_helper(start, visited)
            count = 1
            for i in range(n):
                if not visited[i]:
                    count += 1
                    dfs_helper(i, visited)
            
            return count
        return dfs(0)

        
