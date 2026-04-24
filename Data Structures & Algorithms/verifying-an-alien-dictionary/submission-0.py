class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i
        
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            if len(word1) > len(word2) and word1.startswith(word2):
                return False
            for j in range(min(len(word1), len(word2))):
                if order_map[word1[j]] < order_map[word2[j]]:
                    break
                elif order_map[word1[j]] > order_map[word2[j]]:
                    return False
        return True