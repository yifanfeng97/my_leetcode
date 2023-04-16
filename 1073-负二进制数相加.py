class Solution:
    def addNegabinary(self, arr1 , arr2 ) :
        arr1.reverse()
        arr2.reverse()
        res = []
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        i, last, next, nnext = 0, 0, 0, 0
        while i < len(arr1) or i < len(arr2) or (last != 0 or next != 0 or nnext != 0):
            cur = 0
            cur += arr1[i] if i < len(arr1) else 0
            cur += arr2[i] if i < len(arr2) else 0
            cur += last
            if cur == -2:
                next += 1
                res.append(0)
            elif cur == -1:
                next += 1
                res.append(1)
            elif cur == 0:
                res.append(0)
            elif cur == 1:
                res.append(1)
            elif cur == 2:
                next -= 1
                res.append(0)
            elif cur == 3:
                next += 1
                nnext += 1
                res.append(1)
            elif cur == 4:
                nnext += 1
                res.append(0)
            elif cur == 5:
                nnext += 1
                res.append(1)
            else:
                print("Error")
            last = next
            next = nnext
            nnext = 0
            i += 1
        while len(res)>1 and res[-1] == 0:
            res.pop()
        res.reverse()
        return res

if __name__ == "__main__":
    # print(Solution().addNegabinary([1,1,1,1,1], [1,0,1]))
    print(Solution().addNegabinary([1], [1,1,0,1]))
    # print(Solution().addNegabinary([1,0,1], [1,0,1]))