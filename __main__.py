from data import DataLoader
from algorithms import leader_route_plan


title = "Polynesian Navigation"

print(f"{'=' * 40}")
print(f"{title:^40}")
print(f"{'=' * 40}")


edges = DataLoader.get_island_edges()
populations = DataLoader.get_island_populations()

graph = {}

# Populate graph using an adjacency list
for e in edges:
    starting_vertex = e["from"]

    if starting_vertex not in graph:
        graph[starting_vertex] = []

    destination_vertex = e["to"]
    weight = e["travel_time"]

    graph[starting_vertex].append((destination_vertex, weight))

print(f"\n\nLeader Knowledge Sharing\n")

recent_visits = {}
for island in populations:
    recent_visits[island] = 0

# Plan the leader routes (knowledge sharing)
for island in populations:
    route = leader_route_plan(graph, populations, recent_visits, island)

    print(f"Leader from {island}")
    print(" => ".join(route))
    print()
