class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        degree = [0]*numCourses
        for u, v in prerequisites:
            adj[u].append(v)
            degree[v] += 1
        pre = [set() for _ in range(numCourses)]
        queue = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for neigh in adj[node]:
                pre[neigh].add(node)
                pre[neigh].update(pre[node])
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    queue.append(neigh)
        return [u in pre[v] for u, v in queries] 