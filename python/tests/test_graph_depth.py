from challenges.graph_depth_first.graph_depth_first import Graph 
import pytest



def test_depth(ghraphi):
    excepted=[0, 1, 2, 3]
    actual=ghraphi.DFS(0)
    assert actual==excepted


# def test_depth():
#     g=Graph()
#     excepted=[0, 1, 2, 3]
#     actual=ghraphi.DFS(0)
#     assert actual==excepted
    

    












@pytest.fixture
def ghraphi():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    return g
 


