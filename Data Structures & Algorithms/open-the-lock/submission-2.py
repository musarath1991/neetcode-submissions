class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = deque()
        visited = set()
        queue.append(("0000", 0))
        visited.add("0000")
        while queue:
            state, step = queue.popleft()
            if state == target:
                return step
            for i in range(len(state)):
                digit = int(state[i])
                for move in [-1,1]:
                    new_digit = (digit+move)%10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    if new_state not in visited and new_state not in dead:
                        queue.append((new_state, step+1))
                        visited.add(new_state)
        return -1