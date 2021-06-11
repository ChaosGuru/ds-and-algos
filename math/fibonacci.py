def fibonacci(n):
    arr = []
    f1, f2 = 0, 1

    for _ in range(n):
        arr.append(f1)

        f1, f2 = f2, f1+f2

    return arr


if __name__=='__main__':
    res = fibonacci(10)
    print(res, len(res))

