from typing import List
class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        if m == 1 and n == 1:
            return 1
        row_max, col_max = [max(mat[i]) for i in range(m)], [max([mat[i][j] for i in range(m)]) for j in range(n)]
        res = 0
        def dfs(_i, _j, _p):
            cur = mat[_i][_j]
            if cur >= row_max[_i] and cur >= col_max[_j]:
                nonlocal res
                res = max(res, _p)
                return
            if cur < row_max[_i]:
                for __j in range(n):
                    if mat[_i][__j] > cur:
                        dfs(_i, __j, _p+1)
            if cur < col_max[_j]:
                for __i in range(m):
                    if mat[__i][_j] > cur:
                        dfs(__i, _j, _p+1)
        for i in range(m):
            for j in range(n):
                dfs(i, j, 1)
        return res
    
if __name__ == "__main__":
    # print(Solution().maxIncreasingCells([[3,1],[3,4]]))
    print(Solution().maxIncreasingCells([[3,1,6],[-9,5,7]]))
    # print(Solution().maxIncreasingCells([[1,5],[2,4]]))
    # print(Solution().maxIncreasingCells([[1,5,1],[4,1,4]]))
    # print(Solution().maxIncreasingCells([[11,13,21,3,8,1,16],[15,17,22,4,9,2,18],[12,14,23,5,10,6,19],[24,0,0,0,0,0,20],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[7,6,5,4,3,2,1]]))
    # print(Solution().maxIncreasingCells([[3,4,5],[3,2,6],[2,2,1]]))