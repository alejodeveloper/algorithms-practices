
from functools import reduce


class BaseNumbers:
    def __init__(self, number_size: int = 1):
        if number_size >= 10 or number_size < 1:
            exception_message = f"Size {number_size} out of bounds, must be " \
                                f"between 0 and 9"

            raise Exception(exception_message)
        self.hyphen = '-'
        self.pipe = '|'
        self.blank_space = ' '
        self.break_line = '\n'
        self.number_size = number_size

    def get_hyphen_line(self):
        hyphen_line = reduce(
            lambda base, _: base + self.hyphen,
            range(self.number_size),
            ' '
        )
        hyphen_line += f' {self.break_line}'

        return hyphen_line

    def get_pip_lines(self, begin_pipe: bool = True, end_pipe: bool = True):
        pipe_line = ''
        base_pipe = self.pipe if begin_pipe else ' '
        for i in range(self.number_size):
            pipes = reduce(
                lambda base, _: base + self.blank_space,
                range(self.number_size),
                base_pipe
            )
            end_pipes = f'{self.pipe}{self.break_line}' if end_pipe \
                else f' {self.break_line}'
            pipe_line += pipes + end_pipes

        return pipe_line

    def get_number_str(
            self,
            first_line: bool,
            middle_up_first: bool,
            middle_up_second: bool,
            middle_line: bool,
            middle_down_first: bool,
            middle_down_second: bool,
            down_line: bool,
    ):

        base_up = self.get_hyphen_line() if first_line else ' \n'
        middle_up = self.get_pip_lines(
            begin_pipe=middle_up_first, end_pipe=middle_up_second)
        middle_line = self.get_hyphen_line() if middle_line else ' \n'
        middle_down = self.get_pip_lines(
            begin_pipe=middle_down_first, end_pipe=middle_down_second)
        down_line = self.get_hyphen_line() if down_line else ' \n'

        return base_up + middle_up + middle_line + middle_down + down_line

    def get_number(self, number: int) -> str:
        if number == 0:
            return self.get_number_str(
                first_line=True,
                middle_up_first=True,
                middle_up_second=True,
                middle_line=False,
                middle_down_first=True,
                middle_down_second=True,
                down_line=True,
            )
        elif number == 1:
            return self.get_number_str(
                first_line=False,
                middle_up_first=True,
                middle_up_second=False,
                middle_line=False,
                middle_down_first=True,
                middle_down_second=False,
                down_line=False,
            )
        elif number == 2:
            return self.get_number_str(
                first_line=True,
                middle_up_first=False,
                middle_up_second=True,
                middle_line=True,
                middle_down_first=True,
                middle_down_second=False,
                down_line=True,
            )
        elif number == 3:
            return self.get_number_str(
                first_line=True,
                middle_up_first=False,
                middle_up_second=True,
                middle_line=True,
                middle_down_first=False,
                middle_down_second=True,
                down_line=True,
            )
        elif number == 4:
            return self.get_number_str(
                first_line=False,
                middle_up_first=True,
                middle_up_second=True,
                middle_line=True,
                middle_down_first=False,
                middle_down_second=True,
                down_line=False,
            )
        elif number == 5:
            return self.get_number_str(
                first_line=True,
                middle_up_first=True,
                middle_up_second=False,
                middle_line=True,
                middle_down_first=False,
                middle_down_second=True,
                down_line=True,
            )
        elif number == 6:
            return self.get_number_str(
                first_line=True,
                middle_up_first=True,
                middle_up_second=False,
                middle_line=True,
                middle_down_first=True,
                middle_down_second=True,
                down_line=True,
            )
        elif number == 7:
            return self.get_number_str(
                first_line=True,
                middle_up_first=False,
                middle_up_second=True,
                middle_line=False,
                middle_down_first=False,
                middle_down_second=True,
                down_line=False,
            )
        elif number == 8:
            return self.get_number_str(
                first_line=True,
                middle_up_first=True,
                middle_up_second=True,
                middle_line=True,
                middle_down_first=True,
                middle_down_second=True,
                down_line=True,
            )
        elif number == 9:
            return self.get_number_str(
                first_line=True,
                middle_up_first=True,
                middle_up_second=True,
                middle_line=True,
                middle_down_first=False,
                middle_down_second=True,
                down_line=True,
            )
        else:
            exception_message = f"Number {number} out of bounds, must be " \
                                f"between 0 and 9"

            raise Exception(exception_message)


my_input = str(input())

if my_input != '0,0':
    size, number_str = my_input.strip().split(',')
    size = int(size)
    numbers = BaseNumbers(size)
    numbers_str = reduce(
        lambda base, my_number: base + numbers.get_number(int(my_number)),
        number_str, ''
    )
