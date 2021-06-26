# # from python.graph.graph import Graph, Vertex
# from typing import get_args
# import pytest
# from graph.graph import Vertex,Graph


# def test_add_node(graph):
#     """
#     Add a vertex to a graph.
#     """
#     value = 'raneem'

#     expected = Vertex(value).value
#     vertex = graph.add_node(value)

#     assert isinstance(vertex, Vertex)
#     assert vertex.value == expected

# # An edge can be successfully added to the graph

# def test_add_edge_no_start_vertex(graph):
#     graph.add_node('raneem')
#     sami = graph.add_node('sami')
#     omar = Vertex('omar')
    
#     with pytest.raises(KeyError):
#         graph.add_edge(sami, omar)

    

# def test_add_edge_no_end_vertex(graph):
#     """
#     Fail to add edge to vertex not in graph.
#     """

#     raneem = graph.add_node('raneem')
#     graph.add_node('omar')
#     sami = Vertex('sami')

#     with pytest.raises(KeyError):
#         graph.add_edge(raneem, sami)


# def test_add_edge(graph):
#     """
#     Add directed edge between two vertices in graph.
#     """

#     # raneem = graph.add_node('raneem')
#     # omar = graph.add_node('omar')

#     # graph.add_edge(raneem, omar)

#     # expected = (omar, 0)
#     # actual = graph.adjancency_list[raneem][0]

#     # assert actual == expected


# def test_add_edge_with_weight(graph):
#     """
#     Add directed edge between two vertices in graph with weight.
#     """

#     apple = graph.add_node('apple')
#     banana = graph.add_node('banana')
#     weight = 102

#     graph.add_edge(apple, banana, weight)

#     expected = (banana, weight)
#     actual = graph.adjacency_list[apple][0]

#     assert actual == expected


# def test_get_nodes_empty(graph):
#     """
#     Get an empty collection of vertices when a graph has no vertices.
#     """

#     expected = set({})
#     actual = set(graph.get_nodes())

#     assert actual == expected


# def test_get_nodes(graph):
#     """
#     Get a collection of al vertices in a graph.
#     """

#     apple = graph.add_node('apple')
#     banana = graph.add_node('banana')
#     carrot = graph.add_node('carrot')

#     expected = set({apple, banana, carrot})
#     actual = set(graph.get_nodes())

#     assert actual == expected


# def test_get_nodes_no_neighbors(graph):
#     """
#     A graph vertex with no neighbors is shown as an empty collection.
#     """

#     apple = graph.add_node('apple')

#     expected = []
#     actual = graph.get_neighbors(apple)

#     assert actual == expected


# def test_get_neighbors(graph):
#     """
#     Neighbors of a graph vertex are gotten.
#     """

#     apple = graph.add_node('apple')
#     banana = graph.add_node('banana')

#     graph.add_edge(apple, banana)

#     expected = [(banana, 0)]
#     actual = graph.get_neighbors(apple)

#     assert actual == expected


# def test_size_empty(graph):
#     """
#     See size of empty graph.
#     """

#     expected = 0
#     actual = graph.size()

#     assert actual == expected


# def test_size(graph):
#     """
#     See size of non-empty graph.
#     """

#     graph.add_node('apple')

#     expected = 1
#     actual = graph.size()

#     assert actual == expected


# # # Fixtures


# @pytest.fixture
# def graph():
#     """
#     Create Graph instance.
#     """

#     return Graph()
