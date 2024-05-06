"""
        node
        (A)
        / \
     (B)  (C)
      /\    \
    (D)(E)  (F)
        
    BINARY TREES
    1. At most 2 children per node
    2. Exactly 1 root node
    3. Exactly 1 path b/w root and any node

    HOW TO REPRESENT::
    1. We have to represent these as objects i.e every node will be an object or an instance  of a class
    2. The properties to store within this object would be the current value, eg. A in our current node.
    - But we also need to refer to children. Left and right pointers to the children.
    - In the case of (C) that has one child to the right you would have to use null or undefined for a non-existent child
    - The same will apply for leaf nodes
    3. 
"""

class Node:
    '''Baseline Binary Tree Class'''
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


# HOW DO WE DO A DEPTH FIRST SEARCH
# 1. Iteratively

# def depthFirstValues(root):
#     stack = [ root ] # stick to stack rules, only use .pop() and .push()
#     result = []

#     if root is None:
#         return []
    
#     while len(stack) > 0:
#         current = stack.pop()
#         result.append(current.val)

#         stack.append(current.right) if current.right else None
#         stack.append(current.left) if current.left else None

#     return result

# HOW DO WE DO A DEPTH FIRST SEARCH
# 2. Recurrsively
def depthFirstValues(root):
    if root is None:
        return []
    
    leftValues = depthFirstValues(root.left)
    rightValues = depthFirstValues(root.right)

    return [root.val] + leftValues + rightValues    

print(depthFirstValues(a))