""" asymmetric ctyptography algorithm
"""

import random
import timeit

import sympy


def random_bit(bit):
    return random.randrange(2**(bit-1)+1, 2**bit-1)


def low_prime_test(num):
    primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 
        71, 73, 79, 83, 89, 97, 101, 103, 
        107, 109, 113, 127, 131, 137, 139, 
        149, 151, 157, 163, 167, 173, 179, 
        181, 191, 193, 197, 199, 211, 223,
        227, 229, 233, 239, 241, 251, 257,
        263, 269, 271, 277, 281, 283, 293,
        307, 311, 313, 317, 331, 337, 347, 349
    ]
    
    for p in primes:
        if p**2 <= num:
            break
        elif num%p == 0: 
            return False

    return True


def miller_rabin_test(num):
    max_div_2 = 0
    even_num = num - 1

    while even_num % 2 == 0:
        even_num >>= 1
        max_div_2 += 1
    
    assert(2**max_div_2 * even_num == num - 1)

    def trial_composite(round_tester):
        if pow(round_tester, even_num, num) == 1:
            return False

        for i in range(max_div_2):
            if pow(round_tester, 2**1 * even_num, num) == num-1:
                return False

        return True

    num_radian_trials = 20
    for i in range(num_radian_trials):
        round_tester = random.randrange(2, num)
        if trial_composite(round_tester):
            return False

        return True


def prime_num():
    while True:
        num = random_bit(1024)

        if not low_prime_test(num):
            continue

        if not miller_rabin_test(num):
            continue

        return num


def main():
    p1 = prime_num()
    p2 = prime_num()

    n = p1*p2
    l = (p1-1)*(p2-1)
    
    e = 1

    k = 1
    d = (k*l + 1) / e


if __name__=='__main__':
    pr = prime_num()
    print(pr)
    print(sympy.isprime(pr))