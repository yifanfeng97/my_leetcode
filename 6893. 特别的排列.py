from typing import List
from functools import lru_cache as cache
from collections import defaultdict

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        path = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] % nums[i] == 0 or nums[i] % nums[j] == 0:
                    path[i].append(j)
                    path[j].append(i)
        @cache
        def dfs(msk, i):
            if msk == (1<<n)-1:
                return 1
            r = 0
            for p in path[i]:
                if msk & (1<<p) ==0:
                    r += dfs(msk|(1<<p), p)
            return r
        res = 0
        for i in range(n):
            res += dfs(1<<i, i)
        return res

if __name__ == "__main__":
    print(Solution().specialPerm([2, 3, 6]))