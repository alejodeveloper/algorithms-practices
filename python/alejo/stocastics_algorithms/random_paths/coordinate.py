
class Coordinate:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def move(self, delta_x: int, delta_y: int):
        return Coordinate(self.x + delta_x, self.y + delta_y)

    def distance(self, another_coordinate) -> int:
        delta_x = self.x - another_coordinate.x
        delta_y = self.y - another_coordinate.y

        return (delta_x**2 + delta_y**2)**0.5
