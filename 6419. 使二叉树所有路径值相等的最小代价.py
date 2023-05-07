from typing import List


class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        def dfs(idx):
            nonlocal res
            l_idx, r_idx = idx*2+1, idx*2+2
            c_l = dfs(l_idx) if l_idx < n else 0
            c_r = dfs(r_idx) if r_idx < n else 0
            c = max(c_l, c_r)
            res += abs(c_l - c_r)
            return cost[idx] + c
        dfs(0)
        return res

if __name__ == "__main__":
    print(Solution().minIncrements(7, [1,5,2,2,3,3,1]))