def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    res = s[0]
    for i in range(1, len(s)):
        # 偶数
        _half_max = min(i, len(s) - i)
        for j in range(_half_max):
            if s[i-1-j] == s[i+j]:
                if (j+1)*2 > len(res):
                    res = s[i-1-j:i+j+1]
            else:
                break
        # 奇数
        _half_max = min(i, len(s)-1-i)
        for j in range(1, _half_max+1):
            if s[i-j] == s[i+j]:
                if j * 2 + 1 > len(res):
                    res = s[i-j:i+j+1]
            else:
                break
    return res

if __name__ == "__main__":
    # print(longestPalindrome("babad"))
    print(longestPalindrome("aaaa"))