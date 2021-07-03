from graph_breadth_first.graph_breadth_first import Graph 
import pytest


def test_breadth(bgf):
    # g = Graph()
    # g.addEdge(0, 1)
    expected = [1, 2, 0, 3]
    actual = bgf.BFS(1)
    assert actual == expected




# Fixtures


@pytest.fixture
def bgf():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    return g
        