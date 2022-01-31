from Trees.node import Node
from binary_tree import BinaryTree
class BinarySearchTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    def add(self , value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root , value)

    def _add(self , node,value):
        pass




    def contains(self , value):
        self.value = value
        pass
