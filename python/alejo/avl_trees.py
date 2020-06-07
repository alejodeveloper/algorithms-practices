class Node:
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.left = None
        self.right = None


class AVLTree:

    def __str__(self):
        if self.root:
            return self.print_avl(self.root)

        return ""
    
    def print_avl(self, node: Node) -> str:
        str_tree = ""
        if node.left:
            str_tree += f" {self.print_avl(node.left)}"
        str_tree += f" {node.data}"

        if node.right:
            str_tree += f" {self.print_avl(node.right)}"

        return str_tree

    def __init__(self):
        self.root = None

    def insert_data(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node) -> Node:
        if not node:
            return Node(data)
        if data > node.data:
            node.right = self.insert_node(data, node.right)
        elif data < node.data:
            node.left = self.insert_node(data, node.left)

        node.height = self.calculate_height(node)

        return self.settle_violation(data, node)

    def settle_violation(self, data, node) -> Node:
        balance = self.calculate_balance(node)
        if balance > 1 and data < node.left.data:
            print("Rotating to the right.... three linked nodes on the left")
            print(f"Node {node.data}, left node child {node.left.data}, "
                  f"data {data}")
            return self.right_rotate(node)
        elif balance < -1 and data > node.right.data:
            print("Rotating to the left.... three linked nodes on the right")
            print(f"Node {node.data}, right node child {node.right.data}, "
                  f"data {data}")
            return self.left_rotate(node)

        elif balance > 1 and data > node.data:
            print("Unbalance in the left on the right... rotating the root "
                  "node")
            print(f"Node data {node.data}, left {node.left.data}, data {data}")
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        elif balance < -1 and data < node.data:
            print("Unbalance in the right on the left... rotating the root "
                  "node")
            print(f"Node data {node.data}, right {node.right.data}, data {data}")
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    @staticmethod
    def node_height(node: Node):
        if not node:
            return -1

        return node.height

    def calculate_height(self, node: Node):
        height = max(
            self.node_height(node.left), self.node_height(node.right)
        ) + 1

        return height

    def calculate_balance(self, node: Node):
        if not node:
            return 0

        return self.node_height(node.left) - self.node_height(node.right)

    def right_rotate(self, node: Node) -> Node:
        # Rotate into the right
        left_node = node.left
        right_node = left_node.right
        left_node.right = node
        node.left = right_node
        node.height = self.calculate_height(node)
        left_node.height = self.calculate_height(left_node)
        return left_node

    def left_rotate(self, node: Node) -> Node:
        # Rotate into the left
        right_node = node.right
        left_node = right_node.left

        right_node.left = node
        node.right = left_node
        node.height = node.height = self.calculate_height(node)
        right_node.height = self.calculate_height(right_node)

        return right_node
