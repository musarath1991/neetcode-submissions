class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            ways = dfs(i+1)
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                ways += dfs(i+2)
            memo[i] = ways
            return memo[i]
        return dfs(0)