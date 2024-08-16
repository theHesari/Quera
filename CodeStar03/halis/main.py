def create_graph(v, n):
    adj = {int(_): [] for _ in range(1, n + 1)}
    for vertex in v:
        n1, n2 = vertex.split(" ")
        adj[int(n1)].append(int(n2))
        adj[int(n2)].append(int(n1))
    return adj


def find_cycles(graph):
    cycles = []
    checked = set()

    def dfs(node, visited, path):
        visited.add(node)
        path.append(node)

        neighbors = graph.get(node, [])

        for neighbor in neighbors:
            if neighbor in visited:
                # Cycle detected
                start_index = path.index(neighbor)
                cycle = path[start_index:]
                m = tuple(sorted(cycle))
                if len(cycle) > 2 and m not in checked:
                    checked.add(m)
                    cycles.append(cycle)
            else:
                dfs(neighbor, visited, path)

        visited.remove(node)
        path.pop()

    for node in graph.keys():
        dfs(node, set(), [])

    return cycles


def bfs(graph, start, goal):
    explored = []
    queue = [[start]]

    if start == goal:
        print("Same Node")
        return

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path
            explored.append(node)

    print("So sorry, but a connecting path doesn't exist :(")
    return


if __name__ == "__main__":
    startV = int(input())
    nodes = int(input())
    vert = int(input())
    vertexes = [input() for _ in range(vert)]

    graph = create_graph(vertexes, nodes)
    ans = find_cycles(graph)
    paths = [
        bfs_result if bfs_result is not None else -1
        for m in range(len(ans))
        for n in ans[m]
        for bfs_result in [bfs(graph, startV, n)]
    ]
    shortest_path = min(paths, key=len)
    print(' '.join([str(path) for path in shortest_path]))