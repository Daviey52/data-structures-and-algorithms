from node import Node


class Stack:
    def __init__(self, top=None, value=None):
        self.top = top
        self.value = value
        pass

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def pop(self):
        try:
            if self.top == None:
                raise Exception("Stack is Empty")
            else:
                # node = Node()
                node = self.top
                self.top = self.top.next
                node_value = node.value
                del node
                return node_value
        except Exception as e:
            print(str(e))

    def peek(self):
        try:
            if self.top == None:
                raise Exception("Stack is Empty")
            else:
                return self.top.value

        except Exception as e:
            print(str(e))


s = Stack()
s.push(1)
s.push(2)

print(s)
print(s.isEmpty())
print(s.pop())
print(s.peek())
print(s.isEmpty)
