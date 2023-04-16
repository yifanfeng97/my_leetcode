def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    freq = numRows * 2 - 2
    max_len = len(s)
    res = ['' for _ in range(numRows)]
    for i in range(0, max_len, freq):
        res[0] += s[i]
        if i + numRows - 1 < max_len:
            res[-1] += s[i+numRows - 1]
        for j in range(1, numRows - 1):
            if i + j < max_len:
                res[j] += s[i+j]
            if i + freq - j < max_len:
                res[j] += s[i + freq -j]
    res_s = "".join(res)
    return res_s

if __name__ == "__main__":
    # print(convert("PAYPALISHIRING", 3))
    # print(convert("PAYPALISHIRING", 4))
    # print(convert("A", 1))
    print(convert("AB", 2))