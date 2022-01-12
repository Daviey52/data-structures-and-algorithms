from linked_list.s
import pytest


def test_node_instance():
    node = Node(1, None)
    assert node.next == None
    assert node.value == 1
