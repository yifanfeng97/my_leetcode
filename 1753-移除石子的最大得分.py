import heapq as hq

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        h = [a, b, c]
        hq.heapify(h)
        score = 0
        while(h[1]!=0 and h[2]!=0):
            h[1] -= 1
            h[2] -= 1
            score += 1
            hq.heapify(h)
        return score

if __name__ == "__main__":
    # print(Solution().maximumScore(2, 4, 6))
    print(Solution().maximumScore(3, 8, 2))
    print(Solution().maximumScore(1, 8, 8))