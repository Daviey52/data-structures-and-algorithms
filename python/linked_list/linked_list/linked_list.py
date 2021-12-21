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

    def to_string(self):
        pass
        result = ""

        current = self.head
        while current:
            result += f"{ {current.value} } ->"
            current = current.next
            result += f"None"
            return result

    def append():
        pass

    def insert_before():
        pass

    def insert_After():
        pass
