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
         
        
    
    
    
# if __name__=="__main__":
#     # # print('hello')  
    
#     # graphi=Graph()
#     # y=graphi.add_node(1)
#     # x=graphi.add_node(5)
#     # z=graphi.add_node(3)
#     # f=graphi.add_node('w')



#     # graphi.add_edge(y,x,2)
#     # graphi.add_edge(z,f,2)
#     # graphi.add_edge(y,z,2)


#     # print(graphi.get_neighbors(y))
        
        
