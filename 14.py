"""
Problem 14 - Euler Project
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import sys

one_million = 1000000

def get_chain_length(x: int) -> int:
    chain = []
    while x != 1:
        chain.append(x)
        if x%2 == 0:
            x = x // 2
        else:
            x = x * 3 + 1
    
    chain.append(1)

    # print(chain, len(chain))
    return len(chain)

if __name__ == '__main__':
    max_value = int(sys.argv[1])

    start_number_with_max_chain = 0
    max_chain_length = 0
    for x in range(1, max_value):
        chain_length = get_chain_length(x)

        if chain_length > max_chain_length:
            max_chain_length = chain_length
            start_number_with_max_chain = x

            # print(start_number_with_max_chain, chain_length)
            

    print(f'Max Chain Length: {start_number_with_max_chain}, {max_chain_length}')
