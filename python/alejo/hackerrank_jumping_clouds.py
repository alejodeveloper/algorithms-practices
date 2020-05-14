#!/bin/python3

import os

# Complete the jumpingOnClouds function below.
def jumping_clouds(clouds: list, number_clouds: int) -> int:
    index = 0
    steps = 0

    while index < number_clouds:
        if (index + 2) < number_clouds and clouds[index + 2] == 0:
            index += 2
            steps += 1
        elif (index + 1) < number_clouds and clouds[index + 1] == 0:
            index += 1
            steps += 1
        else:
            index = number_clouds
    return steps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumping_clouds(c, n)

    fptr.write(str(result) + '\n')

    fptr.close()
