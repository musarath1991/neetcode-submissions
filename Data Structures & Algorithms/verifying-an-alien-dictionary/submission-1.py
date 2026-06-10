class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return False
            for j in range(min(len(w1), len(w2))):
                if order_map[w1[j]] > order_map[w2[j]]:
                    return False
                if order_map[w1[j]] < order_map[w2[j]]:
                    break
        return True