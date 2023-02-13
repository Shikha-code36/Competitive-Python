import logging

def depth_first_search(graph, node): 
    try: 
        visited = set()
        visited = dfs_helper(graph, node, visited)
        return visited
    except Exception as e:
        logging.exception("An error occurred during binary search: %s", e)
        return "An error occurred during deapth first search: {}".format(str(e))


def dfs_helper(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs_helper(graph, neighbour, visited)
    return visited
