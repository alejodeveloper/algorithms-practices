import random
import math

from stochastic_statistics import standard_deviation_sqrt, media, variation


def throw_needle(number_needles: int):
    inside_circle = 0

    for _ in range(number_needles):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distance = math.sqrt((x**2 + y**2))

        if distance <= 1:
            inside_circle += 1

    return (4 * inside_circle)/number_needles


def estimation(needle_number: int, number_tries: int):
    estimates = [throw_needle(needle_number) for _ in range(number_tries)]
    media_estimated = media(estimates)
    variation_estimated = variation(estimates, media_estimated)
    sigma = standard_deviation_sqrt(variation_estimated)
    print(f'Est={round(media_estimated, 5)}, sigma={sigma}')
    return media_estimated, sigma


def pi_estimation(precision: float, number_tries: int):
    needle_numbers = 1000
    pi_sigma = precision

    while pi_sigma >= precision / 1.96:
        pi_media, pi_sigma = estimation(needle_numbers, number_tries)
        needle_numbers *= 2

    return pi_media


if __name__ == '__main__':
    my_media = pi_estimation(0.01, 1000)
    print(my_media)
