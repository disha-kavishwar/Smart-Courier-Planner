
import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0
    pq = [(0, start)]

    while pq:
        distance, node = heapq.heappop(pq)

        if distance > distances[node]:
            continue

        for neighbour, weight in graph[node]:
            new_distance = distance + weight

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = node
                heapq.heappush(pq, (new_distance, neighbour))

    return distances, previous


def get_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if not path or path[0] != start:
        return []

    return path


def create_graph():
    return {
        "Warehouse": [("A", 4), ("B", 2)],
        "A": [("Warehouse", 4), ("B", 1), ("C", 5)],
        "B": [("Warehouse", 2), ("A", 1), ("C", 8)],
        "C": [("A", 5), ("B", 8), ("D", 3)],
        "D": [("C", 3)]
    }
