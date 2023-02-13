def depth_first_search(graph, node):  
    visited = set()
    visited = dfs_helper(graph, node, visited)
    return visited

def dfs_helper(graph, node, visited):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs_helper(graph, neighbour, visited)
    return visited
