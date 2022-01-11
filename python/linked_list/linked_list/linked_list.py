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

    def append_method(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
            current.next = node

    def insert_before(self, newNode, new_value):
        if self.head.value == newNode:
            node = Node(new_value)
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next != None:
                if current.next.value == newNode:
                    temp = current.next
                    current.next = Node(new_value, temp)
                    break
                current = current.next

    def insert_After(self, new_Node, value):
        new_node = Node(value)
        current = self.head
        while current != None:
            if current.value == new_Node:
                new_node.next = current.next
                current.next = new_node
            current = current.next

    def zip_lists(self, list1, list2):
        zipped_list = LinkedList()
        current1 = list1.head
        current2 = list2.head

        while current1 or current2:
            if current1:
                zipped_list.append(current1.value)
                current1 = current1.next
            if current2:
                zipped_list.append(current2.value)
                current2 = current2.next
        return zipped_list
