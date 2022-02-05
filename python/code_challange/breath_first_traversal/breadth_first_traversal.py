import queue
from Trees.binary_tree import BinaryTree
from stack.queue import Queue
from Trees.node import Node

def Breadth_first(tree):
    if tree is None:
        return

    queue = Queue()
    queue.enqueue(tree.root)
    node = Node()

    while tree:
        node =queue.dequeue(tree.root)

        if node.left is not None:
            queue.enqueue(node.left)
        if node.right is not None:
            queue.enqueue(node.right)

    return (queue)






