import collections
from functools import reduce
from itertools import product
import random

DECKS = ['spades', 'hearts', 'trees', 'diamond']
VALUES = [
    'ace', '2', '3', '4', '5', '6', '7', '8', '9', 'jack', 'queen', 'king'
]


def create_deck():
    return list(product(DECKS, VALUES))


def get_hand(hand_size: int, deck: list):
    return random.sample(deck, hand_size)


def get_pair_probability(hand: list, number_tries: int, hand_size: int):
    pairs = 0
    values = [value[1] for value in hand]
    counter = dict(collections.Counter(values))
    for value in counter.values():
        if value == 2:
            pairs += 1
            break

    pair_probability = pairs / number_tries
    print(
        f'The probability of get a flush in one hand of {hand_size} is '
        f'{pair_probability}'
    )


def get_flush_probability(hand: list, number_tries: int, hand_size: int):
    flush = 0
    my_hand = reduce(
        lambda acc, value: acc + value[1],
        hand, ''
    )
    my_values = ''.join(VALUES)
    if my_hand in my_values:
        flush += 1
    print(
        f'The probability of get a flush in one hand of {hand_size} is '
        f'{flush/number_tries}')


def main(hand_size: int, number_tries: int):
    deck = create_deck()
    hands = [get_hand(hand_size, deck) for _ in range(number_tries)]

    flush = 0
    for hand in hands:

        my_hand = reduce(
            lambda acc, value: acc + value[1],
            hand, ''
        )
        my_values = ''.join(VALUES)
        if my_hand in my_values:
            flush += 1
    print(
        f'The probability of get a flush in one hand of {hand_size} is '
        f'{flush / number_tries : .2%}')


if __name__ == '__main__':
    hand_size = int(input())
    tries = int(input())

    main(hand_size, tries)
