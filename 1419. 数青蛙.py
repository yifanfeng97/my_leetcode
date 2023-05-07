class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # cur = croakOfFrogs
        # res, temp = 0, "croak"
        # while len(cur)!=0:
        #     if len(cur) % 5 != 0:
        #         return -1
        #     rest, t_i = "", 0
        #     for c in cur:
        #         if c == temp[t_i%5]:
        #             t_i += 1
        #             continue
        #         else:
        #             rest += c
        #     if len(rest) == len(cur):
        #         break
        #     else:
        #         res += 1
        #         cur = rest
        # if len(cur) != 0:
        #     return -1
        # else:
        #     return res
        res, tmp = 0, {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        prev = {'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        for c in croakOfFrogs:
            if c == 'c':
                tmp[c] += 1
                res = max(res, tmp[c])
            else:
                if tmp[prev[c]] != 0:
                    tmp[c] += 1
                else:
                    return -1
                res = max(res, tmp[c])
                if c == 'k':
                    for k in tmp.keys():
                        tmp[k] -= 1
        for v in tmp.values():
            if v != 0:
                return -1
        return res

if __name__ == "__main__":
    print(Solution.minNumberOfFrogs("crroakcoak"))
