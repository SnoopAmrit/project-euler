"""
Problem 16 - Euler Project
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) 
    contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import sys
from typing import Dict, List


def get_counts_numbers(numbers: List[int]) -> int:
    counts = 0
    for number in numbers:
        counts += len(number)

    return counts


def get_counts_one_nine() -> int:
    one_nine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    return get_counts_numbers(one_nine)


def get_counts_eleven_nineteen() -> int:
    eleven_nineteen = [
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen"
    ]

    return get_counts_numbers(eleven_nineteen)


def get_counts_one_ninetynine() -> int:
    counts = get_counts_one_nine() + len("ten") + get_counts_eleven_nineteen()

    tens = [
        "twenty",
        "thirty",
        "fourty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    for ten in tens:
        counts += (10 * len(ten)) + get_counts_one_nine()

    return counts


def get_counts_first_thousand() -> int:
    counts = get_counts_one_ninetynine()
    hundred_len = len("hundred")

    counts += hundred_len

    hundreds = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for hundred in hundreds:
        counts += (len(hundred) + hundred_len + len("and")) * 99 + get_counts_one_ninetynine()

    counts += len("thousand")

    return counts

if __name__ == "__main__":
    print(get_counts_one_nine())
    print(get_counts_eleven_nineteen())
    print(get_counts_one_ninetynine())
    print(get_counts_first_thousand())