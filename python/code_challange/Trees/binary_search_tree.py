from Trees.node import Node
from Trees.binary_tree import BinaryTree

class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    def add(self ,value):
        node = Node(value)
        if self.root is None:
            self.root = node

        def traverse(root):
            if self.root.value == node.value:
                return print(f'{node.value} already exist')
            if node.value < root.value:
                if root.left is None:
                    root.left = node
                elif root.left.value < node.value:
                    node.left = root.left
                    root.left = node
                else:
                    traverse(root.left)
            elif node.value > root.value:
                if root.right is None:
                    root.right = node
                elif root .right.value > node.value:
                    node.right = root.right
                    root.right = node
                else:
                    traverse(root.right)
        traverse(self.root)



    def contains(self , value):
        self.value = value
        node = Node(value)

        if node == None:
            return False
        elif value == node.value:
            return True
        elif value <node.value:
            return self.contains(node.left ,value)
        elif value > node.value:
            return self.contains(node.right,value)
