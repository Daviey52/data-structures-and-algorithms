
from Trees.node import Node
from Trees.binary_tree import BinaryTree

def fizz_buzz_tree(self,tree=None):
    new_k_tree = BinaryTree()
    new_node = Node(value=None)
    tree = BinaryTree()
    old_node = tree.root


    def traverse_node(old_node, new_node):
        new_node = fizz_buzz(old_node.value)
        if old_node.left:
            new_node = Node()
            traverse_node(old_node.left,new_node.left)

        if old_node.right:
            new_node.right = Node()
            traverse_node(old_node.right ,new_node.right)
    def fizz_buzz(old_value):
        result = ''
        if old_value % 3 == 0:
            result += 'Fizz'

        if old_value % 5 == 0:
            result += 'Buzz'
        return result or str(old_value)
    traverse_node(old_node , new_node)

    BinaryTree.root = new_node

    return new_k_tree

if __name__ == "__main__":

     tree = BinaryTree()
     tree.root = Node(3)
     tree.root.left = Node(5)
     tree.root.right = Node(7)
     tree.root.left.left = Node(15)
     print(fizz_buzz_tree(tree))



