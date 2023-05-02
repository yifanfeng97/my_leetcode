from typing import List

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        res, doing, done = '', False, False
        for c in num:
            if not done:
                o = str(change[int(c)])
                if c == o:
                    res += c
                elif c < o:
                    res += o
                    doing = True
                else:
                    if doing:
                        done = True
                    res += c
            else:
                res += c
        return res

if __name__ == "__main__":
    print(Solution().maximumNumber("334111", [0,9,2,3,3,2,5,5,5,5]))