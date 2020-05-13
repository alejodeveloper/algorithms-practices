import random


def media(dataset: list) -> int:
    return sum(dataset)/len(dataset)


if __name__ == '__main__':
    dataset = [random.randint(1, 100) for data in range(20)]
    mu = media(dataset)
    print(dataset)
    print(mu)
