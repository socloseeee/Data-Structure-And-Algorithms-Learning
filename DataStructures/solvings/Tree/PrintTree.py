class Node:
    def __init__(self, val: int = None):
        self.value = val
        self.left_child = None
        self.right_child = None


class BinaryTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def insert_left(parent_node, value):
        new_node = Node(value)
        parent_node.left_child = new_node
        return new_node

    @staticmethod
    def insert_right(parent_node, value):
        new_node = Node(value)
        parent_node.right_child = new_node
        return new_node


def Height(node):
    if node is None:
        return 0
    else:
        left_height = Height(node.left_child)
        right_height = Height(node.right_child)
        return max(left_height, right_height) + 1


def PrintTree(node):
    if node is not None:
        print(node.value)
        PrintTree(node.left_child)
        PrintTree(node.right_child)


tree = BinaryTree()
root = Node(1)
tree.root = root
left_child = tree.insert_left(root, 2)
right_child = tree.insert_right(root, 3)
tree.insert_left(left_child, 4)
tree.insert_right(left_child, 5)
tree.insert_left(right_child, 6)
tree.insert_right(right_child, 7)
print(Height(root))
PrintTree(root)
