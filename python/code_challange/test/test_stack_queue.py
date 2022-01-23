from stack.stack import Stack
from stack.queue import Queue
from stack.stack import CustomError
from stack.stack import Pseudo_Queue
import pytest


def test_push():
    stack = Stack()
    stack.push(5)
    stack.push(7)
    assert stack.top.value == 7


def test_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    assert stack.stacklength == 4


def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.stacklength == 2
    stack.pop()
    assert stack.pop() == 1


def test_pop_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    assert stack.stacklength == 4
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.isEmpty() == True


def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2


def test_stack():
    stack = Stack()
    assert stack.isEmpty() == True
    assert stack.peek() == None


@pytest.mark.skip("pending")
def test_empty_stack():
    # stack = Stack()
    with pytest.raises(CustomError) as e:
        stack = Stack()
        stack.pop()
        stack.peek()
        str(e) == "Stack is Empty"

    # assert stack.peek() == "Stack is Empty"


def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front.value == 2


def test_multiple_enqueu():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.queuelenght == 2
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.queuelenght == 4


def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.queuelenght == 3
    assert queue.dequeue() == 3


def test_peek_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 2


# @pytest.mark.skip("pending")
def test_multiple_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.queuelenght == 2
    queue.dequeue()
    queue.dequeue()
    assert queue.queuelenght == 1


def test_empty_queue():
    queue = Queue()
    assert queue.queuelenght == 0


# @pytest.mark.skip("pending")
def test_exception():
    queue = Queue()
    assert queue.peek() == None


def test_psedo_enqueue():
    p = Pseudo_Queue()
    p.enqueue(1)
    p.enqueue(2)
    assert p.stack_1.stacklength == 2
    assert p.stack_1.peek() == 2


def test_empty_psedo_queue():
    p = Pseudo_Queue()
    assert p.stack_1.stacklength == 0
    assert p.stack_2.stacklength == 0


def test_psedo_dequeue():
    p = Pseudo_Queue()
    p.enqueue(1)
    p.enqueue(2)
    assert p.stack_1.stacklength == 2
    assert p.stack_2.stacklength == 0
    assert p.stack_1.peek() == 2
    p.dequeue()
    assert p.stack_2.peek() == 1
    assert p.stack_1.stacklength == 0
    assert p.stack_2.stacklength == 2


@pytest.mark.skip("pending")
def test_empty_dequeue():
    p = Pseudo_Queue()
    assert p.dequeue() == IndexError("can't deque from an empty queue!")
