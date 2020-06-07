#!/bin/python3

import os

# Complete the hourglassSum function below.
def hourglass_sum(matriz: list):
    hourglass_sums = []
    for my_row in range(len(matriz) -2):
        for my_column in range(len(matriz)-2):
            hourglass = (
                    matriz[my_row][my_column] +
                    matriz[my_row][my_column + 1] +
                    matriz[my_row][my_column + 2] +
                    matriz[my_row + 1][my_column + 1] +
                    matriz[my_row + 2][my_column] +
                    matriz[my_row + 2][my_column + 1] +
                    matriz[my_row + 2][my_column + 2]
            )
            hourglass_sums.append(hourglass)

    return max(hourglass_sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
