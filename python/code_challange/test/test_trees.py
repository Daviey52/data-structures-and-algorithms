from Trees.node import Node
from Trees.binary_tree import BinaryTree
#from Trees.binary_search_tree import BinarySearchTree
import pytest


def test_empty_bt():
    bt = BinaryTree()
    assert bt

def test_empty_bt_none():
    bt = BinaryTree()
    assert bt.root == None

def test_bt_preorder():
    bmw = Node('bmw')
    tesla = Node('tesla')
    subaru = Node('subaru')

    bt = BinaryTree(bmw)
    bmw.left = subaru
    bmw.right = tesla

    assert bmw.left == bt.root.left
    assert bmw.right == tesla
    best_car_list = bt.pre_order()
    assert best_car_list == ['bmw','subaru','tesla']
    
def test_bt_order():
    bmw = Node('bmw')
    tesla = Node('tesla')
    subaru = Node('subaru')

    bt = BinaryTree(bmw)
    bmw.left = subaru
    bmw.right = tesla

    best_car_list = bt.in_order()
    assert best_car_list == ['subaru','bmw','tesla']

def test_bt_post_order():
    bmw = Node('bmw')
    tesla = Node('tesla')
    subaru = Node('subaru')

    bt = BinaryTree(bmw)
    bmw.left = subaru
    bmw.right = tesla

    best_car_list = bt.post_order()
    assert best_car_list == ['subaru','tesla','bmw']
