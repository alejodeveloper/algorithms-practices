#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.


def sherlock_anagrams(my_string: str) -> int:
    """
    How many permutions (anagrams) can have a string
    :param my_string: The string to be evaluated
    :return: The number of permutations (anagrams) that the string has
    """
    anagrams = {}
    unique_words = list(set([char for char in my_string]))
    accumulated = ''
    for index, char in enumerate(unique_words):
        anagrams[char] = my_string.count(char)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlock_anagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
