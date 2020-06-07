from functools import reduce

VOWELS = ['a', 'e', 'i', 'o', 'u']


def find_substring(my_string: str, my_length: int):
    how_many_vowels = reduce(
        lambda acc, vowel: acc + my_string.count(vowel),
        VOWELS, 0
    )
    if how_many_vowels:
        vowels_str = {}
        vowels_str.update(get_strings(my_string, my_length))
        print(vowels_str)
        vowels_str = {
            k: v for k, v in sorted(
                vowels_str.items(), reverse=True, key=lambda item: item[1]
            )
        }
        return next(iter(vowels_str))
    return 'Not found!'


def get_strings(my_string: str, my_length: int) -> dict:
    strings = {}
    for index in range(len(my_string)):
        new_string = my_string[index:]
        if len(new_string) >= my_length:
            while len(new_string) > my_length:
                new_string = new_string[1:]

            number_of_vowels = reduce(
                lambda acc, vowel: acc + new_string.count(vowel),
                VOWELS, 0
            )
            strings[new_string] = number_of_vowels

        new_string = my_string[::]
        new_string = new_string[index:]
        if len(new_string) >= my_length:
            while len(new_string) > my_length:
                new_string = new_string[:-1]

            number_of_vowels = reduce(
                lambda acc, vowel: acc + new_string.count(vowel),
                VOWELS, 0
            )
            strings[new_string] = number_of_vowels

    return strings

