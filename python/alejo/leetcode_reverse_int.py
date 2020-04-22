# Easy
from functools import reduce


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if len(bin(x)[2:]) <=32:
            is_negative = x < 0
            my_number_str = str(abs(x))
            my_number_str = reduce(
                lambda number, letter: number + letter, my_number_str[::-1]
            )

            reversed_number = int(my_number_str) * -1 if is_negative else int(my_number_str)

            return reversed_number
        return 0
