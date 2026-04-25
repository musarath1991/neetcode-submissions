class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj[pattern].append(word)
        
        queue = deque()
        queue.append((beginWord))
        visited = set()
        visited.add(beginWord)
        res = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neigh in adj[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)
            res += 1
        return 0