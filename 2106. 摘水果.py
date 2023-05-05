from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        bias, left_v, right_v = 0, 0, 0
        avai_left, avai_right = [], []
        for idx in range(len(fruits)):
            p, v = fruits[idx]
            p -= startPos
            if p == 0:
                bias = v
                continue
            if p < 0 and -p <= k:
                left_v += v
                avai_left.append([-p, v, 0])
            if p > 0 and p <= k:
                right_v += v
                avai_right.append([p, v, right_v])
            if p > 0 and p > k:
                break
        avai_left.reverse()
        tmp = 0
        for idx in range(len(avai_left)):
            p, v ,a = avai_left[idx]
            tmp += v
            avai_left[idx][2] = tmp
        # 不拐弯
        res = max(left_v, right_v)
        # 拐弯
        ## 左 -> 右
        l_idx, r_idx = 0, len(avai_right) - 1
        while l_idx < len(avai_left):
            p, v, a = avai_left[l_idx]
            while r_idx >= 0 and p*2 + avai_right[r_idx][0] > k:
                r_idx -= 1
            if r_idx != -1:
                res = max(res, a + avai_right[r_idx][2])
            else:
                break
            l_idx += 1
        ## 右 -> 左
        l_idx, r_idx = len(avai_left) - 1, 0
        while r_idx < len(avai_right):
            p, v, a = avai_right[r_idx]
            while l_idx >= 0 and p*2 + avai_left[l_idx][0] > k:
                l_idx -= 1
            if l_idx != -1:
                res = max(res, a + avai_left[l_idx][2])
            else:
                break
            r_idx += 1
        return res + bias


if __name__ == "__main__":
    # print(Solution().maxTotalFruits([[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]], 21, 30))
    print(Solution().maxTotalFruits([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], 5, 4))
