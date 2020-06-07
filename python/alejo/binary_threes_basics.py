class Node:

    def __init__(self, data: int):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def __str__(self):
        if self.root is None:
            return ""

        return self.print_three(self.root)

    def print_three(self, node: Node) -> str:
        binary_tree_str = ""
        if node.left:
            binary_tree_str += f" {self.print_three(node.left)} - "

        binary_tree_str += f' {node.data}'

        if node.right:
            binary_tree_str += f" - {self.print_three(node.right)}"

        return binary_tree_str

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)

        else:
            self.insert_data(data, self.root)

    def insert_data(self, new_data, node: Node):
        if node.data >= new_data:
            if node.left:
                self.insert_data(new_data, node.left)
            else:
                node.left = Node(new_data)
        else:
            if node.right:
                self.insert_data(new_data, node.right)
            else:
                node.right = Node(new_data)

    def contains_value(self, new_data: int, node: Node) -> bool:
        if node.data == new_data:
            return True
        elif node.data > new_data:
            if node.left:
                self.contains_value(new_data, node.left)

            else:
                return False

        elif node.data < new_data:
            if node.right:
                self.contains_value(new_data, node.right)

            else:
                return False

    def remove(self, data):
        if self.root:
            self.delete_node(data, self.root)

    def delete_node(self, data, node: Node) -> Node:
        if not node:
            return node

        if node.data == data:

            if not node.right and not node.left:
                return None

            elif not node.left:
                return node.right

            elif not node.right:
                return node.left

            else:
                return self.get_predecessor(node.left)

        elif node.data < data:
            node.right = self.delete_node(data, node.right)

        elif node.data > data:
            node.left = self.delete_node(data, node.left)

        else:
            print("404 Not found")

    def get_predecessor(self, node: Node) -> Node:
        if node.right:
            return self.get_predecessor(node.right)
        return node
