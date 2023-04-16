class Solution:  
    def area(self, height, i, j):
            return (j - i) * min(height[i], height[j])

    def maxArea(self, height) -> int:
        res = 0
        i, j = 0, len(height) - 1
        res = self.area(height, i, j)
        while i < j:
            if height[i] < height[j]:
                i += 1
                while i < j and self.area(height, i, j) < res:
                    i += 1
                res = max(self.area(height, i, j), res)
            else:
                j -= 1
                while i < j and self.area(height, i, j) < res:
                    j -= 1
                res = max(self.area(height, i, j), res)
        return res

if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))