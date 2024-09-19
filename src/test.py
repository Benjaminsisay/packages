from graphs_bsisay import sp

graph = {
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 4},
    2: {0: 4, 1: 4}
}

distances, paths = sp.dijkstra(graph, 0)

print("Distances:", distances)
print("Paths:", paths)