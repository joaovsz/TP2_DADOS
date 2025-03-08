class FloydWarshallAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def shortest_paths(self):
        nodes = list(self.graph.keys())
        dist = {node: {other: float('inf') for other in nodes} for node in nodes}

        for node in nodes:
            dist[node][node] = 0

        for node in self.graph:
            for neighbor, weight in self.graph[node].items():
                dist[node][neighbor] = weight

        for k in nodes:
            for i in nodes:
                for j in nodes:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        return dist
