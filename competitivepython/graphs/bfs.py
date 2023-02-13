def breadth_first_search(graph, node): 
    visited, queue = set(), [node]
    visited.add(node)

    while queue:
        vertex = queue.pop(0) 
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)

    return visited
