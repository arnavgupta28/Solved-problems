

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0]*size for _ in range(size)]
        self.size = size 
        self.vertex = [0]*size 
        
    def add_edge(self,u,v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1 
            self.adj_matrix[v][u] = 1
    
    def add_vertex(self,idx, data):
        if 0 <= idx < self.size:
            self.vertex[idx] = data
    
    def print_graph(self):
        # print the adjacency matrix 
        print("The adjacency matrix for the graph")
        for row in self.adj_matrix:
            print(row)
            
        print("The vertex/nodes in the graph")
        for node in self.vertex:
            print(node)
        # OR we can use this to print 
        # print(self.vertex)
        
        
        # print the vertexes of the table 


# if i have to use this now i have to make an obj of this class 


g = Graph(5)
g.add_vertex(0,'A')
g.add_vertex(1,'B')
g.add_vertex(2,'C')
g.add_vertex(3,'D')
g.add_vertex(4,'E')


g.add_edge(0 , 1)
g.add_edge(0 , 2)
g.add_edge(0 , 3)
g.add_edge(1 , 2)


g.print_graph()

        