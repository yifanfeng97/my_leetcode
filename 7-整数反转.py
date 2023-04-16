def reverse(x: int) -> int:
    flag = -1 if x < 0 else 1
    x = abs(x)
    res = 0
    while x != 0:
        res = res * 10 + x % 10
        x = x // 10
    return flag * res

if __name__ == '__main__':
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))