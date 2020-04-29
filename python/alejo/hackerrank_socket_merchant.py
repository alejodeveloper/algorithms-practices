#!/bin/python3

import os
# Complete the sockMerchant function below.
from functools import reduce


def sock_merchant(socks_amount: int, socks: list) -> int:
    """
    Get a list of socks and then classify them into their colors pair
    :param socks_amount: The total number of socks
    :param socks: The socks for each pair
    :return: The maximum pairs per color possible
    """
    unique_socks = list(set(socks))
    total_amount = reduce(
        lambda pairs, sock: pairs + (socks.count(sock) // 2),
        unique_socks, 0
    )

    return total_amount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
