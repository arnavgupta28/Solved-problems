

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
    def dfs_util(self, v , visited):
        visited[v] = True
        print(self.vertex[v] , end=' ')
        
        for i in range(self.size):
            if self.adj_matrix[v][i] and not visited[i]:
                self.dfs_util(i , visited)
        
        
        
        # print the vertexes of the table 
    def dfs(self , start_vertex_data):
        visited = [False] * self.size 
        start_vertex = self.vertex.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)
        
        
# if i have to use this now i have to make an obj of this class 


g = Graph(7)

g.add_vertex(0, 'A')
g.add_vertex(1, 'B')
g.add_vertex(2, 'C')
g.add_vertex(3, 'D')
g.add_vertex(4, 'E')
g.add_vertex(5, 'F')
g.add_vertex(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F


g.print_graph()

g.dfs('D')

        