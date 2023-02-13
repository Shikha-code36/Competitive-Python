import logging

def breadth_first_search(graph, node): 
    try:
        visited, queue = set(), [node]
        visited.add(node)

        while queue:
            vertex = queue.pop(0) 
            visited.add(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)

        return visited
    except Exception as e:
        logging.exception("An error occurred during binary search: %s", e)
        return "An error occurred during breadth first search: {}".format(str(e))

