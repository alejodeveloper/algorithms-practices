import random


def throw_dice(number_shots: int) -> list:
    return [random.choice([1, 2, 3, 4, 5, 6]) for _ in range(number_shots)]


def main(number_shots: int, number_tries: int):
    shots = [throw_dice(number_shots) for _ in range(number_tries)]
    one = sum([1 for shot in shots if 1 in shot])
    probabilistic_one = one/number_tries
    print(f'Prob of one is {probabilistic_one} over {number_tries}')


if __name__ == '__main__':
    number_shots = int(input())
    number_tries = int(input())

    main(number_shots, number_tries)
