class Solution:
    def trap(self, height ) -> int:
        i, res = 0, 0
        max_idx = -1
        # left
        while max_idx == -1:
            tmp = 0
            for j in range(i+1, len(height)):
                if height[j] < height[i]:
                    if j == len(height) - 1:
                        max_idx = i
                        break
                    tmp += height[i] - height[j]
                else:
                    res += tmp
                    if j == len(height) - 1:
                        return res
                    break
            if tmp > 0:
                i = j
            else:
                i += 1
        # right
        i = len(height) - 1
        while i > max_idx:
            tmp = 0
            for j in range(i-1, max_idx-1, -1):
                if height[j] < height[i]:
                    tmp += height[i] - height[j]
                else:
                    res += tmp
                    break
            if tmp > 0:
                i = j
            else:
                i -= 1
        return res

if __name__ == "__main__":
    # print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(Solution().trap([4,2,0,3,2,5]))
    # print(Solution().trap([5,4,1,2]))
    # print(Solution().trap([9,6,8,8,5,6,3]))
    print(Solution().trap([4, 2, 3]))