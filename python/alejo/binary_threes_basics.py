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

    def delete_node(self, data):
        if self.data == data:
            predecessor = self.get_predecessor(self)
            self.data = predecessor

        if self.data < data:
            self.left.delete_node(data)

        elif self.data > data:
            self.right.delete(data)
        else:
            print("404 Not found")

    def get_predecessor(self, prev_node):
        if self.right:
            predecessor = self.right.get_predecessor(self)

            return predecessor

        if self.left:
            predecessor = self.data
            self.data = self.left.data
            self.left = self.left.left
            self.right = self.left.rigth

            return predecessor

        prev_node.right = None
        predecessor = self.data
        return predecessor
