from functools import reduce


def merge_the_tools(my_string: str, substring_size: int):
    """
    Create different substrings from the amount passed by in substring size
    """
    how_many_substrings = len(my_string)//substring_size
    for _ in range(how_many_substrings):
        new_str = reduce(
            lambda acc, char: acc + char if char not in acc else acc + '',
            my_string[:substring_size], ''
        )

        print(new_str)
        my_string = my_string[substring_size:]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
