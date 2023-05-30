"""
Problem 12 - Euler Project
    The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    Let us list the factors of the first seven triangle numbers:

    1: 1
    3: 1,3
    6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
    We can see that 28 is the first triangle number to have over five divisors.

    What is the value of the first triangle number to have over five hundred divisors?
"""
import sys
from typing import List


def get_factors(x: int) -> int:
    factors = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            factors = get_factors(int(x/i))
            factors.append(i)

            return factors

    factors.append(x)        
    return factors

def get_num_factors(factors: List[int]) -> int:
    factors.sort()
    i=0
    num_factors=1

    power=1
    while i < len(factors)-1:
        if factors[i] == factors[i+1]:
            power += 1
        else:
            num_factors = num_factors * (power+1)
            power = 1

        i += 1

    if (len(factors)>=2) and (factors[len(factors)-1] != factors[len(factors)-2]):
        num_factors = num_factors*2
    else:
        num_factors = num_factors * (power+1)

    return num_factors
        

        
# factors = get_factors(int(sys.argv[1]))
# factors.sort()
# print(factors, len(factors))
# print(get_num_factors(factors))


num_factors = 0
next_num = 2
while num_factors < 500:
    next_triangle_number = int(next_num * (next_num+1) / 2)
    factors = get_factors(next_triangle_number)
    num_factors = get_num_factors(factors)

    print(next_triangle_number, num_factors)

    next_num += 1

print(next_triangle_number, num_factors)

        