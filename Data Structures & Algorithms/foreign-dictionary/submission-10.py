class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        queue = deque()
        for c in indegree:
            if indegree[c] == 0:
                queue.append(c)
        
        res = []
        while queue:
            char = queue.popleft()
            res.append(char)
            for neigh in adj[char]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        if len(res) != len(indegree):
            return ""
        return "".join(res)