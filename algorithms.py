import heapq


def shortest_path(graph, populations, start_island):
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

        for neighbor, weight in neighbors_of_current_node:
            population_weight = populations[neighbor] / max_population
            distance = current_distance + weight - population_weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances


def leader_route_plan(graph, populations, home_island):
    """Find an efficient route for a leader to share knowledge with
    Other islands. Considering shortest path as well as population.

    Route determination algorithm:

    1. Initialize the route and visited set to track the visited islands.
    2. Set the current node to the starting vertex and explore other
    verticies than have not been visited.
    3. While not all the destination islands have been visited:
        a. Add the current node to the visited set and route
        b. Get the shortest path using the custom Dijkstra's
        c. Set the next node as the current node in search
    4. Return the optimal leader route.
    """
    
    route = []
    visited = set()

    current_node = home_island

    while len(visited) < len(populations.keys()):
        visited.add(current_node)
        route.append(current_node)

        distances = shortest_path(graph, populations, current_node)
        next_node = None

        min_distance = float('inf')

        for node in populations:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                next_node = node            
        
        if next_node is None:
            break

        current_node = next_node

    return route
