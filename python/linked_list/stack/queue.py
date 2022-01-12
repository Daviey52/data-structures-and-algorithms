from node import Node


class Queue:
    def __init__(self, front=None):
        self.front = front

    def enqueue(self, value):
        node = Node(value)
        if self.front:
            self.front = node
        else:
            curr = self.front
            while curr.next != None:
                curr = curr.next
            curr.next = node

    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False

    def dequeue(self):
        try:
            if self.front:
                raise Exception("Queue is Empty")
            else:
                node = self.front
                self.front = self.front.next
                node_data = node.value
                del node
                return node_data
        except Exception as e:
            print(str(e))

    def peek(self):
        try:
            if self.front:
                raise Exception("Queue is empty")
            else:
                return self.front.value
        except Exception as e:
            print(str(e))
