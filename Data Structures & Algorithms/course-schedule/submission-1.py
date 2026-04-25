class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[]*numCourses for _ in range(numCourses)]
        indegree = [0]*numCourses
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        return count == numCourses
