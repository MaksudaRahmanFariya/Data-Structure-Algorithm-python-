def dfs(node, destination, graph, visited, count):
    # if destination is reached increment count
    if node == destination:
        count[0] += 1
        return
    visited[node] = True
    for nei in graph[node]:
        if not visited[nei]:
            dfs(nei, destination, graph, visited, count)
    visited[node] = False

def count_path(n, edgelist, source, destination):
    graph = [[] for _ in range(n+1)]
    for u,v in edgelist:
        graph[u].append(v)
    visited = [False]*(n+1)
    count = [0]
    dfs(source, destination, graph, visited, count)
    return count[0]
if __name__ == "__main__":

    n = 5

    # Edge list: [u, v] represents u -> v
    edgeList = [
        [1, 2], [1, 3], [1, 5],
        [2, 5], [2, 4], [3, 5], [4, 3]
    ]

    source = 1
    destination = 5

    print(count_path(n, edgeList, source, destination))
