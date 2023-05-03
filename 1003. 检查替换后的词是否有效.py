class Solution:
    def isValid(self, s: str) -> bool:
        tmp = ''
        for c in s:
            tmp += c
            if tmp[-1] == 'c':
                if len(tmp) >= 3 and tmp[-2] == 'b' and tmp[-3] == 'a':
                    tmp = tmp[:-3]
                else:
                    return False
        if len(tmp) > 0:
            return False
        else:
            return True

if __name__ == "__main__":
    print(Solution().isValid("aabcbc"))