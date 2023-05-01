from typing import List
import heapq

class Solution:
    class Entry:
        def __init__(self, s, e):
            self.s = s
            self.e = e
        def __lt__(self, that):
            return self.s < that.s

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        tmp = []
        for e, s in zip(efficiency, speed):
            tmp.append(Solution.Entry(s, e))
        tmp.sort(key=lambda x: -x.e)

        res, h, total_S = 0, [], 0
        for idx in range(n):
            min_E, total_S = tmp[idx].e, total_S + tmp[idx].s
            res = max(res, min_E * total_S)
            heapq.heappush(h, tmp[idx])
            if len(h) == k:
                item = heapq.heappop(h)
                total_S -= item.s
        return res%(10**9+7)

if __name__ == "__main__":
    print(Solution().maxPerformance(6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3))