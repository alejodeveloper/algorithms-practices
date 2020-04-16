#!/bin/python3

import os

OPEN_BRACKETS = '({['
CLOSING_BRACKETS = ')}]'
CONTRA_PART = {
    '(': ')',
    '{': '}',
    '[': ']',
}


def is_balance(brackets: str):
    closing_brackets = ''
    for index, bracket in enumerate(brackets):
        if index == 0 and bracket in CLOSING_BRACKETS:
            return 'NO'

        if bracket in OPEN_BRACKETS:
            closing_brackets = CONTRA_PART.get(bracket) + closing_brackets

        elif bracket in CLOSING_BRACKETS:
            if len(closing_brackets) > 0 and bracket == closing_brackets[0]:
                closing_brackets = closing_brackets[1:]
                continue
            else:
                return 'NO'

    if closing_brackets != '':
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = is_balance(s)

        fptr.write(result + '\n')

    fptr.close()
