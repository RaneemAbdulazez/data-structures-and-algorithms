from collections import deque
from typing import get_args


class Vertex:
    def __init__(self,value):
        self.value=value
        
        
class Edge:
    def __init__(self,start,end,weight):
        self.start=start
        self.end=end
        self.weight=weight
        
        
class Graph:
    def __init__(self):
        self.adjancency_list={}
        
    def add_node(self,value):
        v=Vertex(value)
        self.adjancency_list[v]=[]
        return v

    
    def add_edge(self,start,end,weight=1):
        if start not in self.adjancency_list:
            raise KeyError("start vertex not found in graph")
        if end not in self.adjancency_list:
            raise KeyError("end vertex not found in graph")
            
        self.adjancency_list[start].append((end, weight))
        
    def get_nodes(self):
        lista=[]
        for i in self.adjancency_list:
            lista.append(i.value)
        return lista
        
    def get_size(self):
        return len(self.adjancency_list)
        
    def get_neighbors(self,vertex):
        return self.adjancency_list[vertex]
    
    

    def graph_breadth_first(self,node):
        visited=set()
        output=[]
        q=deque()
        q.append(node.value)
        
        current=q.popleft()
        while current not in visited: 
            visited.add(current)
            print(visited)
            output.append(current)
            print(output)
            
            neighbors=self.get_neighbors(current)
            
            for i in neighbors:
                print(i[0][1])
                # self.graph_breadth_first(i)
                
        return output
        
            
        
    
    
    
if __name__=="__main__":
    # # print('hello')  
    
    graphi=Graph()
    a=graphi.add_node(1)
    b=graphi.add_node(2)
    c=graphi.add_node(3)
    d=graphi.add_node(4)
    e=graphi.add_node(5)
    g=graphi.add_node(6)
    
    
#     # f=graphi.add_node('w')

    graphi.add_edge(a,b)
    graphi.add_edge(b,c)
    graphi.add_edge(b,d)
    graphi.add_edge(c,d)
    graphi.add_edge(d,g)
    graphi.add_edge(c,g)
    graphi.add_edge(c,e)
    graphi.add_edge(g,e)
    
    print(graphi.get_neighbors(a))
    
    
    
    


        
        
