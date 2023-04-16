def isMatch(s: str, p: str) -> bool:
    dp = [[False for _ in range(len(p)+1)] for __ in range(len(s)+1)]
    dp[0][0] = True
    for j in range(2, len(p)+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if p[j-1] == '*':
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i-1][j-2] or dp[i][j-2] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-2]
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
    return dp[-1][-1]


if __name__ == "__main__":
    # print(isMatch("aa", "a"))
    # print(isMatch("abbbbac", "b*a."))
    # print(isMatch("aa", "a*"))
    # print(isMatch("aab", "c*a*b"))
    # print(isMatch("issippi", "is*p*."))
    # print(isMatch("a", "ab*"))
    # print(isMatch("abcd", "d*"))
    # print(isMatch("abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*"))
    print(isMatch("aab", "c*a*b"))
