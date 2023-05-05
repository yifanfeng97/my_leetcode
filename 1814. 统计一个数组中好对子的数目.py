from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        large = 10**9 + 7
        def rev(a):
            b = 0
            while a:
                b = b*10 + a%10
                a //= 10
            return b
        d = [rev(n) - n for n in nums]
        d = sorted(d)
        i, res = 0, 0
        while i < len(d):
            j = i + 1
            while j < len(d) and d[j] == d[i]:
                j += 1
            cnt = j - i
            if cnt > 1:
                res += cnt * (cnt-1) // 2
                res %= large
            i = j
        return res

if __name__ == "__main__":
    print(Solution().countNicePairs([42,11,1,97]))