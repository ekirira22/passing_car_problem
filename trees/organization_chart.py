import ipdb

class TreeNode:
    '''Baseline Tree Class'''
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.left = None
        self.right = None

class OrganizationChart:
    def __init__(self, root_id, root_name) -> None:
        self.root = TreeNode(root_id, root_name)

    def insert(self, id, name):
        self._insert(self.root, id, name)

    def _insert(self, current_node, id, name):
        if id < current_node.id:
            if current_node.left:
                self._insert(current_node.left, id, name)
            else:
                current_node.left = TreeNode(id, name)
        else:
            if current_node.right:
                self._insert(current_node.right, id, name)
            else:
                current_node.right = TreeNode(id, name)
    
    def search_by_id(self, id):
        self._search_by_id(self.root, id)

    def _search_by_id(self, current_node, id):
        # ipdb.set_trace()
        if id is current_node.id:
            return print(f"ID: {current_node.id} | Name: {current_node.name}")
        
        self._search_by_id(current_node.left, id)  if current_node.left else None
        self._search_by_id(current_node.right, id) if current_node.right else None
        
    def delete_by_id(self, id):
        self._delete_by_id(self.root, id)

    def _delete_by_id(self, current_node, id):
        if id is current_node.id:
            # ipdb.set_trace()
            print(f"ID: {current_node.id} | Deleted Successfully")
            del current_node
            return
        
        self._delete_by_id(current_node.left, id)  if current_node.left else None
        self._delete_by_id(current_node.right, id) if current_node.right else None
    
    # print root node 
    def print_tree(self):
        self._print_tree(self.root, 0)

    def _print_tree(self, node, depth):
        if node:
            self._print_tree(node.right, depth + 1)
            print(' ' * depth + '|-- ' , node.name)
            self._print_tree(node.left, depth + 1)


binary_tree = OrganizationChart(55643, "Eric Maranga")
binary_tree.insert(16466, "Mary Nyawira")
binary_tree.insert(76456, "Betty Nduta")
binary_tree.insert(14853, "Alex Macharia")
binary_tree.insert(28761, "Biudun Murage")
binary_tree.insert(61083, "Miguna Miguna")
binary_tree.insert(89245, "Vusi Thembekwayo")
# ipdb.set_trace()
print(binary_tree.print_tree())
print(binary_tree.search_by_id(61083))
print(binary_tree.delete_by_id(61083))
print(binary_tree.print_tree())