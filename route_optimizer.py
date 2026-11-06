
def nearest_neighbour(graph, start):
    unvisited = set(graph.keys())
    route = [start]
    unvisited.remove(start)

    total_distance = 0
    current = start

    while unvisited:
        neighbours = [
            (weight, node)
            for node, weight in graph[current]
            if node in unvisited
        ]

        if not neighbours:
            return route, total_distance

        distance, next_node = min(neighbours)

        route.append(next_node)
        total_distance += distance

        unvisited.remove(next_node)
        current = next_node

    return route, total_distance
