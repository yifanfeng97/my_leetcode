class Solution:
    def findNumberOfLIS(self, nums) -> int:
        dp = [[1] for _ in range(len(nums))]
        max_len = 1
        res = []
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    cur = dp[j][-1] + 1
                    if cur >= dp[i][-1]:
                        dp[i].append(cur)
                        if cur > max_len:
                            max_len = cur
        cnt = 0
        for t in dp:
            j = -1
            while -j<=len(t) and t[j]==max_len:
                j-=1
                cnt+=1
        return cnt

if __name__ == "__main__":
    # print(Solution().findNumberOfLIS([1,3,5,4,7]))
    # print(Solution().findNumberOfLIS([2,2,2,2,2]))
    print(Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]))