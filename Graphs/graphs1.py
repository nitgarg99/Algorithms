from collections import defaultdict

#Issues with this graph implementation
# 1.    The nodes need to be indexed from 0-n-1
#       For example, nodes can not be 0, 1, 4, 5
#       This would result in indexing issues with visited[] and recursionStack[]
#Solution:
#       We could re-index the nodes by putting each node into an array and the index of that node in the array 
#       is used to build the graph
#       We can use this to build a graph of nodes containing any information
#       For example, given strings 'bob', 'sally', 'jared' each can be indexed
# 
#2.     We need to implement a function to build a graph

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices       #Number of vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recursionStack):
        #Mark node as visited and set to in recursion stack
        visited[v] = True
        recursionStack[v] = True

        for neighbor in self.graph: 
            if visited[neighbor] == False:
                if isCyclicUtil(neighbor, visited, recursionStack) == True:
                    return True
            elif recursionStack[v] == True:
                return True
        recursionStack[v] = False
        return False


    def isCyclic(self):
        visited = [False] * self.V
        recurstionStack = [False] * self.V
        for node in range(self.V)
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recursionStack) == True:
                    return True
        return false


