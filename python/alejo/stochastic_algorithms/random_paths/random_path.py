from coordinate import Coordinate
from drunk import ClassicDrunk, Drunk, RandomDrunk
from field import Field

from bokeh.plotting import figure, show


def walked(field: Field, drunk: Drunk, steps: int):
    begin = field.get_coordinate(drunk)

    for _ in range(steps):
        field.move_drunk(drunk)

    return begin.distance(field.get_coordinate(drunk))


def simulate_walk(steps: int, number_tries: int, drunk_type: Drunk) -> list:
    drunk = drunk_type(name='Alex')
    origin = Coordinate(0, 0)
    distances_walked = []

    for _ in range(number_tries):
        field = Field()
        field.add_drunk(drunk, origin)
        walk_simulation = walked(field, drunk, steps)
        distances_walked.append(round(walk_simulation, 1))

    return distances_walked


def graph_drunk(x: list, y: list, legend_label: str):
    graph = figure(title='Random Path', x_axis_label='Steps',
                   y_axis_label='Distances')
    graph.line(x, y, legend_label=legend_label)
    show(graph)


def main(walks_distances: list, tries: int, drunk_type: Drunk):
    average_distances_walk = []
    for steps in walks_distances:
        distances = simulate_walk(steps, tries, drunk_type)
        avg_distances = round(sum(distances)/len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)
        print(f'{drunk_type.__name__} random walk')
        print(f'{avg_distances} average walked distance')
        print(f'{max_distance} max walked distance')
        print(f'{min_distance} min walked distance')
        average_distances_walk.append(avg_distances)

    graph_drunk(walk_distances, average_distances_walk, drunk_type.__name__)


if __name__ == '__main__':
    walk_distances = [10, 100, 1000, 10000]
    number_times = 100

    main(walk_distances, number_times, ClassicDrunk)
    main(walk_distances, number_times, RandomDrunk)
