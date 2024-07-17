import heapq
from collections import deque


def shortest_path(graph, populations, start_island, alpha=1):
    """Since the weights are non-negative, Dijkstra's is applicable for
    finding the best (shortest) routes from a vertex to other verticies.

    The algorithm was modified to consider the population of the islands.
    Populated islands will take higher priority than less populated ones.
    """

    shortest_distances = {}

    for node in graph:
        shortest_distances[node] = float('inf')

    shortest_distances[start_island] = 0
    priority_queue = [(0, start_island)]

    max_population = max(populations.values())

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_distances[current_node]:
            continue

        neighbors_of_current_node = graph[current_node]

        for neighbor, distance_weight in neighbors_of_current_node:
            population_weight = populations[neighbor] / max_population
            distance = current_distance + distance_weight - alpha * population_weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances


def leader_route_plan(graph, populations, recency, skills, home_island):
    """Find an efficient route for a leader to share knowledge with
    other islands. Considering shortest path, population, recency, and skills.
    """

    route = []
    visited = set()

    current_time = 1
    current_node = home_island

    while len(visited) < len(populations):
        visited.add(current_node)
        route.append(current_node)

        recency[current_node] = current_time
        current_time += 1

        distances = shortest_path(graph, populations, current_node)
        next_node = None

        min_score = float('inf')

        for node in populations:
            if node not in visited:
                recency_priority = current_time - recency[node]
                max_recent_visit = max(recency.values())
                
                skill_priority = len(skills[home_island] - skills[node])
                
                score = (distances[node] * 
                         (1 + recency_priority / (max_recent_visit if max_recent_visit > 0 else 1)) /
                         (1 + skill_priority))
                
                if score < min_score:
                    min_score = score
                    next_node = node      
        
        if next_node is None:
            break

        current_node = next_node
        skills[current_node] = skills[current_node].union(skills[home_island])

    return route


def bfs_paths(graph, start):
    """BFS to find shortest paths from the start node to all other nodes.
    """

    queue = deque([(start, [])])
    visited = set()
    paths = {start: []}
    
    while queue:
        current, path = queue.popleft()
        
        if current not in visited:
            visited.add(current)
            
            for neighbor, travel_time in graph[current]:
                if neighbor not in visited:
                    paths[neighbor] = path + [(current, neighbor)]
                    queue.append((neighbor, path + [(current, neighbor)]))
    
    return paths


def distribute_resources(graph, start_island, resource_quantity, canoe_capacity):
    """Distribute resources from the start island to the other islands.
    """
    
    resources_distribution = {island: 0 for island in graph}
    paths = bfs_paths(graph, start_island)
    
    remaining_quantity = resource_quantity

    for island in paths:
        if island == start_island:
            continue
        
        path = paths[island]
        for u, v in path:
            if remaining_quantity <= 0:
                break
            
            quantity_for_segment = min(remaining_quantity, canoe_capacity - resources_distribution[v])
            resources_distribution[v] += quantity_for_segment
            remaining_quantity -= quantity_for_segment
    
    return resources_distribution
