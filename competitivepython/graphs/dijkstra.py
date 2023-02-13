import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    path = {vertex: [] for vertex in graph}
    queue = [(0, start)]

    while queue:
        (current_distance, current_vertex) = heapq.heappop(queue)

        if current_vertex == end:
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                path[neighbor] = path[current_vertex] + [neighbor]

    return {'distance': distances[end], 'path': path[end]}
