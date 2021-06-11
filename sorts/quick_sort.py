from random import randint


def quick_sort(arr, start=0, end=None):
    if end == None:
        end = len(arr) - 1

    if end > start:
        piv = partition(arr, start, end)

        quick_sort(arr, start, piv-1)
        quick_sort(arr, piv+1, end)
    
    return arr


def partition(arr, start, end):
    # rand_piv = randint(start, end)
    # arr[rand_piv], arr[end] = arr[end], arr[rand_piv]
    
    piv = end
    ext = start

    for i in range(start, end):
        if arr[i] < arr[piv]:
            arr[ext], arr[i] = arr[i], arr[ext]
            ext += 1

    arr[piv], arr[ext] = arr[ext], arr[piv]

    return ext


if __name__=='__main__':
    arr = [randint(0, 10) for _ in range(2)]
    print(arr)

    res = quick_sort(arr[:], 0, len(arr)-1)   
    print(res)

    assert sorted(arr, reverse=True) == res