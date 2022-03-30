import pytest
from graphs.graph import Graph ,Vertex ,Edge

def test_add_node():
    graph = Graph()
    actual = graph.add_node('graphs').value
    assert actual ==  'graphs'

def test_get_nodes():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    actual = len(graph.get_node())
    assert actual == 2

def test_size():
    graph = Graph()
    graph.add_node('pythonista')
    expected = 1
    actual = graph.size()
    assert actual == expected

def test_size_empty():
    graph = Graph()
    expected = 0
    actual = graph.size()
    assert actual == expected
