#!/bin/python3
import os

# Complete the repeatedString function below.

A = 'a'


def repeated_string(my_str: str, final_len: int) -> int:
    """
    Get a string and set the amount of a inside that string and then
    multiplies by the value of the potential substring
    :param my_str: The string to evaluate
    :param final_len: The len of the string
    :return: The number of time that the initial string is repeated in the
    final string
    """

    many_times = final_len//len(my_str)
    my_char = my_str.count(A)

    count_decimal = my_str[:final_len % len(my_str)].count(A)
    repeated_times = my_char*many_times + count_decimal
    return repeated_times


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
