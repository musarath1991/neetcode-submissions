class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, price in flights:
            adj[u].append((v, price))
        queue = deque()
        queue.append((src, 0))
        min_cost = [float("inf")]*n
        min_cost[src] = 0
        stops = 0
        while queue and stops <= k:
            temp = min_cost[:]
            for _ in range(len(queue)):
                node, price = queue.popleft()
                for neigh, cost in adj[node]:
                    if price + cost < temp[neigh]:
                        temp[neigh] = price + cost
                        queue.append((neigh, temp[neigh]))
            min_cost = temp
            stops += 1
        
        return min_cost[dst] if min_cost[dst] != float("inf") else -1

