import math
import random


def media(dataset: list) -> int:
    return sum(dataset)/len(dataset)


def variation(dataset: list, media_st: int) -> int:
    return sum([(x - media_st)**2 for x in dataset])/len(dataset)


def standard_deviation_sqrt(variation_st: int):
    return math.sqrt(variation_st)


if __name__ == '__main__':
    dataset = [random.randint(1, 100) for data in range(20)]
    mu = media(dataset)
    sigma_variation = variation(dataset, mu)
    sigma = standard_deviation_sqrt(sigma_variation)
    print('My dataset')
    print(dataset)
    print('------------------------------------')
    print(f'Media (mu): {mu}')
    print(f'Variation (sigma)²: {sigma_variation}')
    print(f'Standard deviation (sigma): {sigma}')

