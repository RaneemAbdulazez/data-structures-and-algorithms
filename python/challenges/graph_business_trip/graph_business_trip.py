from python.graph.graph import Graph



def trip(graph, lst):
   cost=0
   for i in lst :
        for n in graph.adjancy_list:
                if i == n.vlaue:
                    if  lst[i+1] in i.get_neighbors:
                            cost+=i.weight
                    else:
                            return 0