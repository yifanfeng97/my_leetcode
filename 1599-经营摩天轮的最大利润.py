from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        res, profit, i, his = -1, -1, 0, 0
        wait = customers[i]
        while wait > 0:
            if wait >= 4:
                his += 4
                wait -= 4
            else:
                his += wait
                wait = 0
            cur_profit = his * boardingCost - (i+1)*runningCost
            if cur_profit > 0 and cur_profit > profit:
                profit = cur_profit
                res = i + 1
            i += 1
            if i < len(customers):
                wait += customers[i]
        return res

if __name__ == "__main__":
    # print(Solution().minOperationsMaxProfit([8,3], 5, 6))
    # print(Solution().minOperationsMaxProfit([10, 10, 1, 0, 0], 4, 4))
    print(Solution().minOperationsMaxProfit([2], 2, 4))