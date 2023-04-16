from copy import deepcopy
from typing import List


def largest1BorderedSquare(grid: List[List[int]]) -> int:
    col_cum, row_cum = deepcopy(grid), deepcopy(grid)
    res = 1 if grid[0][0] == 1 else 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i - 1 >= 0 and col_cum[i][j] != 0:
                col_cum[i][j] = col_cum[i - 1][j] + col_cum[i][j]
            if j - 1 >= 0 and row_cum[i][j] != 0:
                row_cum[i][j] = row_cum[i][j - 1] + row_cum[i][j]
            cur_max = min(col_cum[i][j], row_cum[i][j])
            for cur in range(1, cur_max+1):
                if (i - cur + 1 >= 0
                    and j - cur + 1 >= 0
                    and row_cum[i - cur + 1][j] >= cur
                    and col_cum[i][j - cur + 1] >= cur
                ):
                    res = max(cur, res)
    return res ** 2


if __name__ == "__main__":
    # print(largest1BorderedSquare([[1,1,1],[1,0,1],[1,1,1]]))
    # print(largest1BorderedSquare([[1,1,0,0]]))
    print(
        largest1BorderedSquare(
            [
                [0, 1, 1, 1, 1, 0],
                [1, 1, 0, 1, 1, 0],
                [1, 1, 0, 1, 0, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
            ]
        )
    )
