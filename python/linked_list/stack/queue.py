from linked_list.linked_list import Node


class Queue:
    def __init__(self, front=None, queuelenght=0, tail=None):
        self.front = front
        self.queuelenght = queuelenght
        self.tail = tail

    def enqueue(self, value):
        node = Node(value)
        if self.tail is None:
            self.front = node
            self.queuelenght = self.queuelenght + 1
        else:
            self.tail.next = node(value)
            self.last = self.last.next
            self.queuelenght = self.queuelenght + 1

    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False

    def dequeue(self):
        try:
            if self.front is None:
                raise Exception("Queue is Empty")
            else:
                temp = self.front.value
                self.front = self.front.next
                self.queuelenght = self.queuelenght - 1
                return temp
        except Exception as e:
            print(str(e))

    def peek(self):
        try:
            if self.front is None:
                raise Exception("Queue is empty")
            else:
                return self.front.value
        except Exception as e:
            print(str(e))
