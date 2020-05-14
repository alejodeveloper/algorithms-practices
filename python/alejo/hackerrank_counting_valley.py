#!/bin/python3

import os
# Complete the countingValleys function below.
def counting_valleys(n, steps: str) -> int:
    my_steps_count = 0
    valleys = 0
    for step in steps:
        if step == 'U':
            if my_steps_count == -1:
                valleys += 1
            my_steps_count += 1
        else:
            my_steps_count -= 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = counting_valleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
