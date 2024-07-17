from data import DataLoader
from algorithms import leader_route_plan, distribute_resources


title = "Polynesian Navigation"

print(f"{'=' * 40}")
print(f"{title:^40}")
print(f"{'=' * 40}")

edges = DataLoader.get_island_edges()
populations = DataLoader.get_island_populations()
resources = DataLoader.get_resources()

graph = {}
for e in edges:
    starting_vertex = e["from"]
    if starting_vertex not in graph:
        graph[starting_vertex] = []
    destination_vertex = e["to"]
    weight = e["travel_time"]
    graph[starting_vertex].append((destination_vertex, weight))

for island in populations:
    if island not in graph:
        graph[island] = []


# Task 1: Leader Knowledge Sharing
print(f"\n\nTask 1: Leader Knowledge Sharing\n")

recent_visits = {island: 0 for island in populations}
skills = {island: set() for island in populations}
years = 10

for year in range(years):
    print(f"Year {year + 1}")
    for island in populations:
        route = leader_route_plan(graph, populations, recent_visits, skills, island)
        print(f"Leader from {island}")
        print(" => ".join(route))
        print(f"Skills shared: {skills[island]}")
        print()
    
    # Simulate skill acquisition and population growth
    for island in populations:
        if year % 2 == 0:  # New skill every 2 years
            skills[island].add(f"Skill_Year{year}")
        populations[island] *= 1.01


# Task 2: Resource Distribution
print(f"\n\nTask 2: Resource Distribution\n")

for resource_name, resource_info in resources.items():
    start_island = resource_info["produced_at"]
    resource_quantity = resource_info["quantity"]
    canoe_capacity = resource_info["canoe_capacity"]

    resource_distribution = distribute_resources(graph, start_island, resource_quantity, canoe_capacity)

    print(f"Distributing {resource_name} from {start_island} with total quantity {resource_quantity} and canoe capacity {canoe_capacity}")
    for island, quantity in resource_distribution.items():
        print(f"Island: {island}, {resource_name} Received: {quantity:.2f}")
    print()


# Task 4: Tourism across Islands
# Not implemented yet.
