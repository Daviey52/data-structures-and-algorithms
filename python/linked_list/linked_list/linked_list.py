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

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        last_Node = self.head
        while last_Node.next:
            last_Node = last_Node.next
            last_Node = node

    def insert_before(self, newNode, value):
        node = Node(newNode)
        node.next = Node(value).next = node

    def insert_After(self, newNode, value):
        before_new_node = Node(value)
        node = Node(newNode)
        node.next = Node(value).next = before_new_node
        before_new_node.next = node
