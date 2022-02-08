from Trees.binary_tree import BinaryTree
from Trees.node import Node

from fizz_buzz_tree.fizz_buzz_tree import fizz_buzz_tree
import pytest

def test_fizz_buzz_tree():
    pass

@pytest.mark.skip("pending")
def test_fizz_buzz_tree():
    tree = BinaryTree()
    tree.root = Node(3)
    tree.root.left = Node(5)
    tree.root.right = Node(7)
    fizz_buzz_tree(tree)
    assert tree.root.value == 'Fizz'
    
