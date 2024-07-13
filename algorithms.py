import heapq

def shortest_path(graph, start_vertex):
    """Since the weights are non-negative, Dijkstra's is applicable for
    finding the best (shortest) routes from a vertex to other verticies.
    """
    shortest_distances = {}

    for node in graph:
        shortest_distances[node] = float('inf')

    shortest_distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]

    # Keep looping until PQ is empty
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_distances[current_node]:
            continue

        neighbors_of_current_node = graph[current_node]

        for neighbor, weight in neighbors_of_current_node:
            distance = current_distance + weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distances
