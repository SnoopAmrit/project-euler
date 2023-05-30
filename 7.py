"""
Problem 7 - Project Euler

Problem Statement:
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10 001st prime number?
"""

import sys
import time

def check_prime(n: int) -> bool:
    if n == 2 or n == 3:
        return True

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


def find_next_prime(n: int) -> int:
    for i in range(n + 1, 2 * n + 1):
        if check_prime(i):
            return i

    return None


def find_xth_prime(x: int) -> int:
    n = 1
    for i in range(x):
        n = find_next_prime(n)

    return n


if __name__ == "__main__":
    start = time.time()

    x = int(sys.argv[1])
    print(find_xth_prime(x))

    end = time.time()

    print(f'Time taken = {round(end-start, 2)} seconds')
