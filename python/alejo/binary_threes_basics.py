class Node:

    def __init__(self, data: int):
        self.left = None
        self.right = None
        self.data = data

    def insert_data(self, new_data: int):
        if self.data >= new_data :
            if self.left:
                self.left.insert_data(new_data)

            else:
                self.left = Node(new_data)

        else:
            if self.right:
                self.right.insert_data(new_data)
            else:
                self.right = Node(new_data)

    def contains_value(self, new_data: int) -> bool:
        if self.data == new_data:
            return True
        elif self.data > new_data:
            if self.left:
                self.left.contains_value(new_data)

            else:
                return False

        elif self.data < new_data:
            if self.right:
                self.left.contains_value(new_data)

            else:
                return False

    def print_three(self):
        if self.left:
            self.left.paint_three()

        print(f'{self.data}')

        if self.right:
            self.right.print_three()
