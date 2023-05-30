"""
Problem 9 - Project Euler

Problem Statement:
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

        a2 + b2 = c2

    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
"""

from typing import Tuple
import sys


def get_pythagorean_triples(n: int) -> Tuple[int, int]:
    limit_a = n // 3 + 1
    limit_b = n // 2 + 1

    for i in range(1, limit_a):
        for j in range(i + 1, limit_b):
            if (i**2 + j**2) == (n - i - j) ** 2:
                return [i, j]

    return (None, None)


def get_pythagorean_triplets_products(n: int) -> int:
    a, b = get_pythagorean_triples(n)

    if a != None:
        return a * b * (n - a - b)

    return None


if __name__ == "__main__":
    target_sum = sys.argv[1]
    print("Pythagorean triplets problem")

    triples_product = get_pythagorean_triplets_products(int(target_sum))

    if triples_product != None:
        print(triples_product)
    else:
        print("No triples found")
