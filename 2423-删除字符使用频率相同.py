from collections import Counter 
class Solution:
    def equalFrequency(self, word: str) -> bool:
        s = Counter(word)
        f_min = min(s.values())
        f_max = max(s.values())
        if f_min == 1 and f_max == 1:
            return True
        flag = True
        if f_max - f_min == 1 or (f_max == 1 and f_min == 1) or (f_min == 1 and (len(word)-1)%f_max==0):
            return True
        else:
            return False

if __name__ == "__main__":
    print(Solution().equalFrequency("ddaccb"))