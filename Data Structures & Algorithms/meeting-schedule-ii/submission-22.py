"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        heap = []
        rooms = 0
        for i in range(len(intervals)):
            if heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            rooms = max(len(heap), rooms)
        return rooms