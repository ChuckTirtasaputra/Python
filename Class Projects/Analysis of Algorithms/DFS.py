# code from https://www.techiedelight.com/find-path-between-vertices-directed-graph/

# Function to perform DFS traversal in a directed graph to find the
# complete path between source and destination vertices
def DFS(graph, src, dest, discovered, path):
 
    # mark the current node as discovered
    discovered[src] = True
 
    # include the current node in the path
    path.append(src)
    # print("Path:", path)

    # if destination vertex is found
    if src == dest:
        return True, path
 
    # do for every edge
    for i in graph[src]:
        # print("i in DFS:", i)
        if i == "sink":
            return True, path.append('sink')
        # if `i` is not yet discovered
        if not discovered[i]:
            # return true if the destination is found
            if DFS(graph, i, dest, discovered, path)[0]:
                # print("PATH:", path)
                return True, path

    # backtrack: remove the current node from the path
    path.pop()

    # print(path)
    # return false if destination vertex is not reachable from src
    return False, path
