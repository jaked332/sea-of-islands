from data import DataLoader
from algorithms import shortest_path


# Let's use this to get the static data
data_loader = DataLoader()
edges = data_loader.get_island_edges()

graph = {}

# Populate graph using an adjacency list
for e in edges:
    starting_vertex = e["from"]

    # If starting vertex is not in graph
    if starting_vertex not in graph:
        graph[starting_vertex] = []

    destination_vertex = e["to"]
    weight = e["travel_time"]

    graph[starting_vertex].append((destination_vertex, weight))


print("The original graph:")
print(graph)
print()

print("Shortest path:")
print()

island_names = set()
for e in edges:
    island_names.add(e["from"])

for island_name in island_names:
    print(f"\n\tThe shortest paths with Vertex= {island_name}\n")
    shortest_distances = shortest_path(graph, island_name)
    print(shortest_distances)
