class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for u, v, w in flights:
            adj[u].append((v, w))
        min_cost = [float("inf")]*(n+1)
        min_cost[src] = 0
        queue = deque()
        queue.append((src, 0))
        stops = 0
        while queue and stops <= k:
            temp = min_cost[:]
            for _ in range(len(queue)):
                node, price = queue.popleft()
                for neigh, neighcost in adj[node]:
                    if neighcost + price < temp[neigh]:
                        temp[neigh] = neighcost + price
                        queue.append((neigh, temp[neigh]))
            stops += 1
            min_cost = temp
        return -1 if min_cost[dst] == float("inf") else min_cost[dst]
            
                