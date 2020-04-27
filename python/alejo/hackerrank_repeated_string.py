#!/bin/python3
import os

# Complete the repeatedString function below.
from functools import reduce


def repeated_string(my_str: str, final_len: int) -> int:
    """
    Get a string and sum itself until reach the length that is passed in
    repeated arg
    :param my_str: The string to evaluate
    :param final_len: The len of the string
    :return: The number of time that the initial string is repeated in the
    final string
    """
    final_str = ''
    while len(final_str) < final_len:
        for char in my_str:
            final_str += char
            if len(final_str) == final_len:
                break
    return final_str.count(my_str[0])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
