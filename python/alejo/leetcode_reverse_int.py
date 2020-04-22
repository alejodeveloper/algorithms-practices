# Easy
from functools import reduce


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        is_negative = x < 0
        my_number_str = str(abs(x))
        my_number_str = reduce(
            lambda number, letter: number + letter, my_number_str[::-1]
        )

        reversed_number = int(my_number_str) * -1 if is_negative else int(
            my_number_str)

        my_range = 2 ** 31
        negative_range = -1 * 2 ** 31
        if negative_range < reversed_number < (my_range - 1):
            return reversed_number

        return 0

