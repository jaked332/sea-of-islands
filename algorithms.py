import heapq


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


def leader_route_plan(graph, populations, recency, home_island):
    """Find an efficient route for a leader to share knowledge with
    Other islands. Considering shortest path, population, recency.

    Route determination algorithm:

    1. Initialize the route and visited set to track the visited islands.
    2. Set the current node to the starting vertex and explore other
    verticies than have not been visited.
    3. While not all the destination islands have been visited:
        a. Add the current node to the visited set and route
        b. Update the last island visit time for the current
        c. Get the shortest path using the custom Dijkstra's
        d. Consider the smallest distance with the constraints
        e. Set the next node as the current node in the search
    4. Return the optimal leader route.
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

        min_distance = float('inf')

        for node in populations:
            if node not in visited:
                recency_priority = current_time - recency[node]
                max_recent_visit = max(recency.values())
                
                updated_distance = distances[node] * (1 + recency_priority
                    / (max_recent_visit if max_recent_visit > 0 else 1))
                
                if updated_distance < min_distance:
                    min_distance = updated_distance
                    next_node = node      
        
        if next_node is None:
            break

        current_node = next_node

    return route
