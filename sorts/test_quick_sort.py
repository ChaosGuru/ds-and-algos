from random import randint

from quick_sort import quick_sort


def test_random(num=100):
    unsorted = [randint(1, num) for _ in range(num)]

    assert sorted(unsorted) == quick_sort(unsorted)