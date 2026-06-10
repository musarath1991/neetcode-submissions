class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, p in flights:
            adj[u].append((v, p))
        queue = deque()
        queue.append((src, 0))
        min_cost = [float("inf")]*n
        min_cost[src] = 0
        stops = 0
        while queue and stops <= k:
            size = len(queue)
            temp = min_cost[:]
            for _ in range(size):
                node, cost = queue.popleft()
                for neigh, price in adj[node]:
                    if cost + price < temp[neigh]:
                        temp[neigh] = cost + price
                        queue.append((neigh, cost + price))
            min_cost = temp
            stops += 1
        return min_cost[dst] if min_cost[dst] != float("inf") else -1