import os


def sherlock_anagrams(my_string: str) -> int:
    """
    How many permutions (anagrams) can have a string
    :param my_string: The string to be evaluated
    :return: The number of permutations (anagrams) that the string has
    """
    anagrams = {}
    string_size = len(my_string)
    anagrams_result = 0
    for index in range(1, string_size):
        for another_index in range(string_size - index + 1):
            substring = ''.join(
                sorted(
                    my_string[another_index: another_index+index]
                )
            )
            if anagrams.get(substring):
                anagrams[substring] += 1
            else:
                anagrams[substring] = 1

            anagrams_result += anagrams.get(substring) - 1

    return anagrams_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlock_anagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
