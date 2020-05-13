from coordinate import Coordinate
from drunk import Drunk


class Field:

    def __init__(self):
        self.drunk_coordinate = {}

    def add_drunk(self, drunk: Drunk, coordinate: Coordinate):
        self.drunk_coordinate[drunk] = coordinate

    def move_drunk(self, drunk: Drunk):
        delta_x, delta_y = drunk.walk()
        actual_coordinate = self.drunk_coordinate.get(drunk)
        new_coordinate = actual_coordinate.move(delta_x, delta_y)

        self.drunk_coordinate[drunk] = new_coordinate

    def get_coordinate(self, drunk: Drunk):
        return self.drunk_coordinate.get(drunk)
