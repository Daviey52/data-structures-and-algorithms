class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Put docstring here
    """

    def __init__(
        self,
        head=None,
    ):
        self.head = head

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        node = Node(value)
        while node != None:
            if node.value == node.value:
                return True
            else:
                return False

    def to_string(self, value):
        node = Node(value)
        while node:
            return str(node.value)
