from copy import deepcopy

class Solution:
    def delta(self, p, t, k=1):
        return (t-p)/(t*(t+k))

    def maxAverageRatio(self, classes, extraStudents: int) -> float:
        for i in range(len(classes)):
            classes[i].append(self.delta(classes[i][0], classes[i][1]))
        classes = sorted(classes, key=lambda x: -x[2])
        for i in range(extraStudents):
            classes[0][0] += 1
            classes[0][1] += 1
            classes[0][2] = self.delta(classes[0][0], classes[0][1])
            j = 1
            tmp = deepcopy(classes[0])
            while tmp[2] < classes[j][2]:
                classes[j-1] = classes[j]
                j += 1
            classes[j-1] = tmp
        res = 0
        for c in classes:
            res += c[0] / c[1]
        return res/len(classes)

if __name__ == "__main__":
    # print(Solution().maxAverageRatio([[1,2],[3,5],[2,2]], 2))
    print(Solution().maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))