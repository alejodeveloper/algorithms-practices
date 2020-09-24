import sys


class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier:
    def __init__(self):
        self.frontier = []
        self.solution = []

    def add(self, node: Node):
        self.frontier.append(node)

    def contains_state(self, state) -> bool:
        return any(node.state == state for node in self.frontier)

    def empty(self) -> bool:
        return not self.frontier

    def remove(self) -> Node:
        if self.empty():
            raise Exception("Frontier is empty")

        return self.frontier.pop(-1)


class QueueFrontier(StackFrontier):
    def remove(self) -> Node:
        if self.empty():
            raise Exception("Frontier is empty")

        return self.frontier.pop(0)


class Maze:
    def __init__(self, start_state, goal_state):
        # Keep track of the number of explored states
        self.num_explored = 0

        # Empty explored set
        self.explored = set()

        self.start = start_state
        self.goal = goal_state
        self.solution = ()

    def neighbors(self, state) -> list:
        """
        Get the neighbors node from a current state
        :param state: Current state to check the neighbors
        :return: A list of tuples composed by action and states from the
        neighbors of the current state
        """
        return []

    def solve_maze(self):
        """
        Finds a solution to a maze if exists
        """
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        while True:
            if frontier.empty():
                raise Exception("No solution")

            node = frontier.remove()

            self.num_explored += 1

            if node.state == self.goal:
                actions = []
                cells = []

                while node.parent:
                    actions.append(node.action)
                    cells.append(node.state)

                actions.reverse()
                cells.reverse()

                self.solution = (actions, cells)

                return

            self.explored.add(node.state)

            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in \
                        self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)
