import random

class Drunk:
    def __init__(self, name: str):
        self.name = name

    def walk(self):
        pass


class ClassicDrunk(Drunk):

    def __init__(self, name: str):
        super().__init__(name)

    def walk(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])


class RandomDrunk(Drunk):

    def __init__(self, name: str):
        super().__init__(f"I'm not {name}, I'm pregnant")

    def walk(self):
        return random.choice([
            (random.randint(-1, 1), random.randint(-1, 1)),
            (random.randint(-2, 2), random.randint(-2, 2)),
            (random.randint(-3, 3), random.randint(-3, 3)),
            (random.randint(-4, 4), random.randint(-4, 4)),
            (random.randint(-5, 5), random.randint(-5, 5)),
        ])
