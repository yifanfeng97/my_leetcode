from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n, res = len(grid), -1
        visit = [[0]*n for _ in range(n)]
        cells = [(0, 0, 1)]
        visit[0][0] = 1
        while len(cells) != 0:
            cur = cells.pop(0)
            x, y, p = cur
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                _x = x + dx
                _y = y + dy
                if _x == n-1 and _y == n-1:
                    return p + 1
                if _x < 0 or _x >= n or _y < 0 or _y >= n or visit[_x][_y] == 1 or grid[_x][_y] == 1:
                    continue
                visit[_x][_y] = 1
                cells.append((_x, _y, p+1))
        return -1

if __name__ == "__main__":
    print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))