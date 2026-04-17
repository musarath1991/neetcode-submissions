class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in flights:
            adj[u].append((v, w))
        queue = deque()
        queue.append((src, 0))
        min_cost = [float('inf')]*n
        min_cost[src] = 0
        stops = 0
        while queue and stops <= k:
            size = len(queue)
            temp = min_cost[:]
            for _ in range(size):
                node, wt = queue.popleft()
                for neigh, price in adj[node]:
                    if wt + price < temp[neigh]:
                        temp[neigh] = wt + price
                        queue.append((neigh, wt+price))
            min_cost = temp
            stops += 1
        return -1 if min_cost[dst] == float("inf") else min_cost[dst]