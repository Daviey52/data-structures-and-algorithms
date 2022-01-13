from linked_list.linked_list import LinkedList, Node
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


def test_includes():
    ll = LinkedList()
    node1 = Node("Honda")
    ll.head = node1
    node2 = Node("Tesla")
    node1.next = node2
    ll.insert("BMW")
    assert ll.head.value == "BMW" and node1.value == "Honda" and node2.value == "Tesla"


def test_includes_not():
    ll = LinkedList()
    node1 = Node("Honda")
    ll.head = node1
    node2 = Node("Tesla")
    node1.next = node2
    ll.insert("BMW")
    assert ll.head.value != "Toyota" and ll != "Mazda" and ll != "Camaro"


@pytest.mark.skip("pending")
def test_to_string():
    ll = LinkedList()
    node1 = Node("Honda")
    ll.head = node1
    node2 = Node("Tesla")
    node1.next = node2
    ll.insert("BMW")
    ll.to_string(ll)
    assert ll.head.value == "{ BMW } ->"


@pytest.mark.skip("pending")
def test_append_method():
    ll = LinkedList()
    node1 = Node("Honda")
    ll.head = node1
    node2 = Node("Tesla")
    node1.next = node2
    ll.insert("BMW")
    ll.append_method("Camaro")
    assert ll.head.value == ("BMW")


@pytest.mark.skip("pending")
def test_Insert_before():
    ll = LinkedList()
    node1 = Node("Honda")
    ll.head = node1
    node2 = Node("Tesla")
    node1.next = node2
    ll.insert("BMW")
    ll.insert_before(node2.next, "Camaro")
    assert ll.includes("Camaro")


@pytest.mark.skip("pending")
def test_Inser_After():
    ll = LinkedList()
    node1 = Node("Honda")
    ll.head = node1
    node2 = Node("Tesla")
    node1.next = node2
    ll.insert("BMW")
    ll.insert_After(node2.next, "Camaro")
    expected = ll.to_string
    assert expected == "BMW -> Honda -> Tesla -> Camaro -> NULL"


@pytest.mark.skip("pending")
def test_zip_lists():
    l1 = LinkedList()
    l2 = LinkedList()
    ll = LinkedList()
    l2.insert(15)
    l2.insert(17)
    l2.insert(16)
    l2.insert(13)
    l1.insert(5)
    l2.insert(7)
    l2.insert(6)
    l2.insert(3)

    ll.zip_lists(l1, l2)
    assert ll == l1 and l2
