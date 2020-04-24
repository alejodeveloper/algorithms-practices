from functools import reduce


class Solution(object):
    def myAtoi(self, my_str: str) -> int:
        """
        Implement atoi which converts a string to an integer.
        The function first discards as many whitespace characters as necessary
        until the first non-whitespace character is found. Then, starting from
        this character, takes an optional initial plus or minus sign followed by
        as many numerical digits as possible, and interprets them as a
        numerical value.
        The string can contain additional characters after those that form
        the integral number, which are ignored and have no effect on the
        behavior of this function.
        If the first sequence of non-whitespace characters in str is not a valid
        integral number, or if no such sequence exists because either str is
        empty or it contains only whitespace characters, no conversion is
        performed.
        If no valid conversion could be performed, a zero value is returned.
        :param my_str: str
        :rtype: int
        """

        str_to_convert = my_str.strip(' ')
        is_negative = str_to_convert[0] == '-'

        if not str_to_convert[0].isdigit() and str_to_convert[0] != '-':
            return 0

        my_number_str = reduce(
            lambda accumulated, numb_str: accumulated + numb_str if
            numb_str.isdigit() else accumulated + '',
            str_to_convert, ''
        )

        my_number_str = int(my_number_str) if my_number_str else 0
        my_number_str = my_number_str * -1 if is_negative else my_number_str

        my_range = 2 ** 31
        negative_range = -1 * 2 ** 31
        if negative_range < my_number_str < (my_range - 1):
            return my_number_str

        return negative_range if my_number_str < negative_range else (my_range - 1)
