def readGraphData(file):
    f=open(file,"r")

    graph=[]
    
    vertexAndEdge=f.readline()
    v = int(vertexAndEdge.split()[0])
    e = int(vertexAndEdge.split()[1])
    
    for line in f.readlines():
        row=[]
        row.append(int(line.split()[0]))
        row.append(int(line.split()[1]))
        row.append(int(line.split()[2]))
        graph.append(row)
    return v,e,graph


def printList(vertex,adj):
    for i in range(vertex):
        print(str(i)+"-> ",end=" ")
        print(adj[i])

def adjacencyList(vertex,graph):
    adj={}

    for i in range(vertex):
        adj[i]=[]

    for e in range(len(graph)):
        u=graph[e][0]
        v=graph[e][1]
        w=graph[e][2]
        adj[u].append((v,w))
        adj[v].append((u,w))
    return adj



import queue

def ucs(graph, start, goal):
    
    q =queue.PriorityQueue()
    
    q.put((0, start))

    visited = set()
 
    while q:
        costnode = list(q.get())
        print(costnode)
        cost = costnode[0]
        node = costnode[1]
        
        if node == goal:
            return cost
 
        if node not in visited:
            visited.add(node)
 
            for neighbor, neighbor_cost in graph[node]:
                if neighbor not in visited:
                    q.put((cost + neighbor_cost, neighbor))
 
    return float('inf')
 

vertex,edge,graph=readGraphData("Weigthted_Graph.txt")
print(vertex,edge,graph)
adj=adjacencyList(vertex,graph)
printList(vertex,adj)  #
print(adj)
s = 0
g = 9
shortest_path_cost = ucs(adj, s, g)
print(f"The shortest path cost between {s} and {g} is {shortest_path_cost}.")