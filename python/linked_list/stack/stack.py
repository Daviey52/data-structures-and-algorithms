from linked_list.linked_list import Node


class CustomError(Exception):
    pass


class Stack:
    def __init__(self, top=None, value=None, stacklength=0):
        self.top = top
        self.value = value
        self.stacklength = stacklength

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
            self.stacklength = self.stacklength + 1
        else:
            node.next = self.top
            self.top = node
            self.stacklength = self.stacklength + 1

    def isEmpty(self):
        if self.stacklength == 0:
            return True
        else:
            return False

    def pop(self):
        try:
            if self.top == None:
                raise CustomError("Stack is Empty")
            else:
                # node = Node()
                node = self.top
                self.top = self.top.next
                node_value = node.value
                self.stacklength = self.stacklength - 1
                del node
                return node_value
        except CustomError as e:
            print(str(e))

    def peek(self):
        try:
            if self.top == None:
                raise CustomError("Stack is Empty")
            else:
                return self.top.value

        except CustomError as e:
            print(str(e))


class Pseudo_Queue:
    def __init__(self, value=None):
        self.value = value
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def enqueue(self, value):
        self.value = value
        self.stack_1.push(value)

    def dequeue(self):
        if self.stack_1.stacklength == 0:
            raise IndexError("can't deque from an empty queue!")

        while self.stack_1.stacklength != 0:
            last_stack_1_node = self.stack_1.pop()
            self.stack_2.push(last_stack_1_node)


p = Pseudo_Queue()
p.enqueue(2)
p.enqueue(3)
print(p.stack_1.peek())
print(p.stack_1.stacklength)
print(p.stack_2.stacklength)
p.dequeue()
print(p.stack_2.peek())
print(p.stack_1.stacklength)
print(p.stack_2.stacklength)
# s.push(1)
# print(s.value)
##print(s.isEmpty())
# print(s.pop())
# print(s.peek())
# print(s.isEmpty)
