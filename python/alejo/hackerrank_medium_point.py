#!/bin/python3
import bisect


def running_median(accumulated_numbers: list, total_amount_numbers: int):
    if total_amount_numbers % 2:
        #impar case
        return float(accumulated_numbers[int(total_amount_numbers/2)])

    middle_point = int(total_amount_numbers/2)

    return float((accumulated_numbers[middle_point] + accumulated_numbers[middle_point-1])/2)


store_numbers = []
for number_new in range(int(input())):
    number = int(input())
    bisect.insort(store_numbers, number)
    print(running_median(store_numbers, number_new+1))
