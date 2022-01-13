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


s = Stack()
# s.push(1)
# s.push(2)

# print(s)
##print(s.isEmpty())
print(s.pop())
# print(s.peek())
# print(s.isEmpty)
