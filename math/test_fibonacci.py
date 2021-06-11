from fibonacci import fibonacci


def test_first_ten():
    first_ten  = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    assert first_ten == fibonacci(10)