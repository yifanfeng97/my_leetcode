from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        l_set = set(letters)
        word_score = {}
        tmp = []
        for w in words:
            s, flag = 0, True
            for c in w:
                if c in l_set:
                    s += score[ord(c)-ord('a')]
                else:
                    flag = False
                    break
            if flag:
                tmp.append(w)
                word_score[w] = s 
        # dfs
        words = tmp
        res = 0
        state = {}
        for l in letters:
            if l not in state:
                state[l] = 1
            else:
                state[l] += 1
        def dfs(idx, state, rest, cur_score):
            if idx >= len(words):
                nonlocal res
                res = max(res, cur_score)
                return 
            word = words[idx]
            if len(word) > rest:
                dfs(idx+1, state, rest, cur_score)
                return 
            flag = True
            cur_cost = {}
            for w in word:
                if w not in cur_cost:
                    cur_cost[w] = 1
                else:
                    cur_cost[w] += 1
                if cur_cost[w] > state[w]:
                    flag = False
                    break
            if flag:
                for w, cost in cur_cost.items():
                    state[w] -= cost
                dfs(idx+1, state, rest-len(word), cur_score+word_score[word])
                for w, cost in cur_cost.items():
                    state[w] += cost
            dfs(idx+1, state, rest, cur_score)
        dfs(0, state, len(letters), 0)
        return res
            
if __name__ == "__main__":
    # print(Solution().maxScoreWords(["azb", "ax", "awb", "ayb", "bpppp"], ["z","a","w","x","y","b","p","p","p"], [10,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,3,2,3,3]))
    print(Solution().maxScoreWords(["cbc", "bca", "cbb", "bbc"], ["a","b","c","c","c"], [8,2,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
