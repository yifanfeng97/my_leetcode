from typing import List
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        b = [(c, t) for c, t in zip(cost, time)]
        b = sorted(b, key = lambda x: x[0])
        res = 10**8
        cum_t, cum_c = 0, 0
        for i in range(n):
            if cum_t >= n-i:
                res = cum_c
                break
            else:
                cum_c += b[i][0]
                cum_t += b[i][1]
        return res

if __name__ == "__main__":
    print(Solution().paintWalls([2,3,4,2], [1,1,1,1]))