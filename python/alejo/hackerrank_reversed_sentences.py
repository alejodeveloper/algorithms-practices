#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

from functools import reduce


def reverse_words_order_and_swap_cases(sentences: str):
    new_sentences = sentences.split(' ')
    new_sentence = []
    for my_sentence in new_sentences[::-1]:

        new_sentence.append(
            reduce(
                lambda acc, letter: acc + letter.lower() if letter.isupper()
                else acc + letter.upper(),
                my_sentence, ''
            )
        )


    return ' '.join(new_sentence)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()

