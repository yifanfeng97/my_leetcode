from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 1
        r_cnt, c_cnt = defaultdict(int), defaultdict(int)
        for i in range(n):
            r_cnt[tuple(grid[i])] += 1
            c_cnt[tuple([grid[j][i] for j in range(n)])] += 1
        res = 0
        for k, v in r_cnt.items():
            if k in c_cnt:
                res += r_cnt[k]*c_cnt[k]
        return res

if __name__ == "__main__":
    print(Solution().equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
