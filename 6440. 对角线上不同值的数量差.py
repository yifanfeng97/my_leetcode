from typing import List
class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0]*n for _ in range(m)]
        # 最上
        for j in range(n):
            tmp = {}
            for i in range(min(n-j, m)):
                cur = grid[i][j+i]
                if cur in tmp:
                    tmp[cur] += 1
                else:
                    tmp[cur] = 1
            left_t = set()
            for i in range(min(n-j, m)):
                cur = grid[i][j+i]
                if tmp[cur] == 1:
                    tmp.pop(cur)
                else:
                    tmp[cur] -= 1
                res[i][j+i] = abs(len(left_t) - len(tmp))
                left_t.add(cur)
        # 最左
        for i in range(m):
            tmp = {}
            for j in range(min(n, m-i)):
                cur = grid[i+j][j]
                if cur in tmp:
                    tmp[cur] += 1
                else:
                    tmp[cur] = 1
            left_t = set()
            for j in range(min(n, m-i)):
                cur = grid[i+j][j]
                if tmp[cur] == 1:
                    tmp.pop(cur)
                else:
                    tmp[cur] -= 1
                res[i+j][j] = abs(len(left_t) - len(tmp))
                left_t.add(cur)
        return res

if __name__ == "__main__":
    # print(Solution().differenceOfDistinctValues([[1,2,3],[3,1,5],[3,2,1]]))
    print(Solution().differenceOfDistinctValues([[6,28,37,34,12,30,43,35,6],[21,47,38,14,31,49,11,14,49],[6,12,35,17,17,2,45,27,43],[34,41,30,28,45,24,50,20,4]]))