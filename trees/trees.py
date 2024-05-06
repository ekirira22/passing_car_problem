class TreeNode:
    '''Baseline Tree Class'''
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value) -> None:
        self.root = TreeNode(root_value)

    def insert(self, value):
        self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left:
                self._insert(current_node.left, value)
            else:
                current_node.left = TreeNode(value)

        else:
            if current_node.right:
                self._insert(current_node.right, value)
            else:
                current_node.right = TreeNode(value)

    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, depth):
        if node:
            self._print_tree(node.right, depth + 1)
            print(' ' * depth + '|-- ' , node.value)
            self._print_tree(node.left, depth + 1)


# instances 1,7,1,2,6,8
binary_tree = BinaryTree(5)
binary_tree.insert(1)
binary_tree.insert(7)
binary_tree.insert(1)
binary_tree.insert(2)
binary_tree.insert(6)
binary_tree.insert(8)

    #            5
    #      1             7  
    #   1     2      6      8

            


print(binary_tree.print_tree())