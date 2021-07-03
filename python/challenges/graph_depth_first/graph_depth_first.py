from collections import defaultdict

class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def DFSUtil(self, v, visited,result):
        
        visited.add(v)
        # print(v, end=' ')
        result.append(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited,result)
        
    def DFS(self, v):
        result=[]
        visited = set()
        self.DFSUtil(v, visited,result)
        return result
        

 
# Driver code
 
 
# Create a graph given
# in the above diagram
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
 