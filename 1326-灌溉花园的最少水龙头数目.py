class Solution:
    def minTaps(self, n: int, ranges ) -> int:
        done_idx, head_idx = 0, 0
        res = 0
        while head_idx <= n and done_idx < n:
            cur_max = head_idx
            try_idx = 0
            while try_idx <= n:
                if try_idx - ranges[try_idx] <= done_idx and try_idx + ranges[try_idx] > cur_max:
                    cur_max = try_idx + ranges[try_idx]
                try_idx += 1
            if cur_max != head_idx:
                head_idx = cur_max
                done_idx = cur_max
                res += 1
            else:
                head_idx += 1
        if done_idx >= n:
            return res
        else:
            return -1

if __name__ == "__main__":
    # print(Solution().minTaps(5, [3,4,1,1,0,0]))
    # print(Solution().minTaps(8, [4,0,0,0,4,0,0,0,4]))
    print(Solution().minTaps(5, [4,3,1,2,0,0]))