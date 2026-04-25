class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        queue = deque()
        pre = [set() for _ in range(numCourses)]
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            for neigh in adj[node]:
                pre[neigh].add(node)
                pre[neigh].update(pre[node])
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return [u in pre[v] for u, v in queries]
