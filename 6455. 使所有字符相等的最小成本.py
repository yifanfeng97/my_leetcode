class Solution:
    def minimumCost(self, s: str) -> int:
        if len(s) == 1:
            return 0
        tmp, idx, res, bias = int(s[0]), 0, 0, 0
        while idx < len(s):
            j = idx + 1
            while j < len(s) and (int(s[j])+bias)%2 == tmp:
                j += 1
            if j == len(s):
                return res
            f_l, f_r = j, len(s) - j
            if f_l <= f_r:
                res += f_l
                tmp = 1 - tmp
            else:
                res += f_r
                bias += 1
            idx = j

if __name__ == "__main__":
    # print(Solution().minimumCost("001011101"))
    # print(Solution().minimumCost("0011"))
    # print(Solution().minimumCost("010101"))
    print(Solution().minimumCost("000000011"))