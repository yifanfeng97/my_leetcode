class Solution:
    def minimumLengthEncoding(self, words) -> int:
        words = sorted(words, key=lambda x: len(x))
        res, d_idx = [], []
        for i in range(len(words)):
            d = False
            for j in range(len(words)):
                if j != i and j not in d_idx and words[j].endswith(words[i]):
                    d = True
                    d_idx.append(i)
                    break
            if not d:
                res.append(words[i])
        res_len = 0
        for w in res:
            res_len += len(w)+1
        return res_len
    
if __name__ == "__main__":
    # print(Solution().minimumLengthEncoding(["time", "me", "bell"]))
    print(Solution().minimumLengthEncoding(["time", "time", "time", "timeee"]))