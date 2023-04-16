from typing import List
import heapq as hq 

class Entry:
    def __init__(self, in_time, cost, idx):
        self.in_time = in_time
        self.cost = cost
        self.idx = idx
    
    def __lt__(self, b: 'Entry'):
        return self.cost < b.cost or (self.cost == b.cost and self.idx < b.idx)

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks = sorted(tasks, key=lambda x: x[0])
        time = 0
        cpu = []
        i, res = 0, []
        while i < len(tasks) or len(cpu) > 0:
            if len(cpu) != 0:
                cur = hq.heappop(cpu)
                time += cur.cost
                res.append(cur.idx)
            else:
                time += 1
            while i < len(tasks) and tasks[i][0] <= time:
                hq.heappush(cpu, Entry(tasks[i][0], tasks[i][1], tasks[i][2]))
                i += 1
        return res


if __name__ == "__main__":
    print(Solution().getOrder([[1,2],[2,4],[3,2],[4,1]]))
    print(Solution().getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]]))
    print(Solution().getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))
