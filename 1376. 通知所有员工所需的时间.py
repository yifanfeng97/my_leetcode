from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return informTime[0]
        # find leaf
        leafs, has_child = set(), [False]*n
        for v in manager:
            if v != -1:
                has_child[v] = True
        for idx, v in enumerate(has_child):
            if not v:
                leafs.add(idx)
        res = [0]*n
        while len(leafs):
            new_leafs = set()
            for l in leafs:
                p = manager[l]
                if p != -1:
                    res[p] = max(res[p], res[l]+informTime[p])
                    new_leafs.add(p)
            leafs = new_leafs
        return res[headID]

if __name__ == "__main__":
    s = Solution()
    # print(s.numOfMinutes(1, 0, [-1], [0]))
    # print(s.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]))
    print(s.numOfMinutes(8, 0, [-1,5,0,6,7,0,0,0], [89,0,0,0,0,523,241,519]))
