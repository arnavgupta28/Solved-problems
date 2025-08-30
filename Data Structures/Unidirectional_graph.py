
# Unidirectional Graph is implemented using adjacency list 


# Value of the all nodes in the graph
vertexData = ['A','B','C','D']

adjacencyMatrix = [
    [0 , 1 , 1 , 1],
    [1 , 0 , 1 , 0],
    [1 , 1 , 0 , 9],
    [1 , 0 , 0 , 0]

]

def printAdjacencyMatrix():
    for row in adjacencyMatrix:
        print(row)

printAdjacencyMatrix()
