
def min4factors(num):
    res = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if len(res) == 4:
            return res
        if num % i == 0:
            res.append(i)
    return res

if __name__ == '__main__':
    for num in range(4, 10000):
        res = min4factors(num)
        if len(res) == 4:
            if res[1]**2 + res[2]**2 + res[3]**2 == num - 1:
                print(num)
