from linked_list import LinkedList, Node
import pytest


def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1


def test_node_instance_fail():
    node = Node(1, None)
    assert node.next != node
    assert node.value != 2


def test_linked_list():
    node = Node(1, None)
    ll = LinkedList(node)
    assert ll.head == node


def test_linked_list_empty():
    ll = LinkedList()
    assert ll.head == None


def test_insert_to_empty_linked_list():
    ll = LinkedList()
    ll.insert("BMW")
    assert ll.head.value == "BMW"


def test_insert_to_linked_list():
    ll = LinkedList()
    node1 = Node("Honda")
    ll.head = node1
    node2 = Node("Tesla")
    node1.next = node2
    ll.insert("BMW")
    assert ll.head.value == "BMW"


def test_insert_multiple_to_linked_list():
    ll = LinkedList()
    ll.insert("BMW")
    ll.insert("Honda")
    ll.insert("Tesla")
    assert ll.head.value == "Tesla"
