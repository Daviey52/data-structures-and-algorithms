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

def test_maximum_value():
    bmw = Node(1)
    tesla = Node(2)
    subaru = Node(3)

    bt = BinaryTree(bmw)
    bmw.left = subaru
    bmw.right = tesla

    maximum_value = bt.maximum_value(bmw)
    assert maximum_value == 3

def test_maximum_left_value():
    bmw = Node(1)
    tesla = Node(2)
    subaru = Node(3)
    toyota = Node(9)
    mustang =Node(5)
    honda = Node(6)
    hyundai = Node(7)

    bt = BinaryTree(bmw)
    bmw.left = subaru
    bmw.right = tesla
    subaru.left = toyota
    subaru.right = mustang
    tesla.left = honda
    tesla.right = hyundai

    maximum_value = bt.maximum_value(bmw)
    assert maximum_value == 9

def test_maximum_Right_value():
    bmw = Node(1)
    tesla = Node(2)
    subaru = Node(3)
    toyota = Node(9)
    mustang =Node(5)
    honda = Node(6)
    hyundai = Node(15)

    bt = BinaryTree(bmw)
    bmw.left = subaru
    bmw.right = tesla
    subaru.left = toyota
    subaru.right = mustang
    tesla.left = honda
    tesla.right = hyundai

    maximum_value = bt.maximum_value(bmw)
    assert maximum_value == 15
def test_maximum_Node_value():
    bmw = Node(20)
    tesla = Node(2)
    subaru = Node(3)
    toyota = Node(9)
    mustang =Node(5)
    honda = Node(6)
    hyundai = Node(15)

    bt = BinaryTree(bmw)
    bmw.left = subaru
    bmw.right = tesla
    subaru.left = toyota
    subaru.right = mustang
    tesla.left = honda
    tesla.right = hyundai

    maximum_value = bt.maximum_value(bmw)
    assert maximum_value == 20
