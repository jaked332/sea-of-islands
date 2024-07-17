from collections import defaultdict, deque

"Breadth-First-Search Algorithm to help find paths with avalibly capacity"
def bfs(source, sink, parent, capacity, adj):
    "Creating Variables"
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        node = queue.popleft()
      for neighbor in adj[node]:
          
          if neghbor not in visited and capacity[node][neighbor] - flow[node][neighbor] >  0:
              parent[neighbor] = node
              
          if neighbor == sink:
              return true
              
          queue.append(neighbor)
          visited.add(neighbor)
          
    return false


"An algorithm that helps determine maximum flow from origin node to other nodes"
def ford_fulkerson(source, sink, capacity, adj):
    "Creating Variables"
    global flow
    parent = {}
    max_flow = 0


    while bfs(source, sink, parent, capacity, adj):
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        
        while != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow


    return max_flow

"""
Testing Section of The File
"""

capacity = defaultdict(lambda: defaultdict(int))
adj = defaultdict(list)

"Creating nodes and edges"
capacity[0][1] = 10
capacity[0][2] = 15
capacity[1][2] = 4
capacity[1][3] = 6
capacity[2][3] = 8
capacity[2][4] = 10

adj[0] = [1, 2]
adj[1] = [2, 3]
adj[2] = [3, 4]
adj[3] = []
adj[4] = []

" Assigning test Source and Sink Values "
source = 0
sink = 4

"Finding Max_flow"
max_flow = ford_fulkerson(source, sink, capacity, adj)
print("max_flow is :", max_flow)
