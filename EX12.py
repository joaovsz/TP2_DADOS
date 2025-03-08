import time
import random
import heapq

class DijkstraAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_paths(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


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


def generate_random_graph(size, max_weight=10):
    graph = {str(i): {} for i in range(size)}
    
    for i in range(size):
        for j in range(i + 1, size):
            if random.random() > 0.3:  
                weight = random.randint(1, max_weight)
                graph[str(i)][str(j)] = weight
                graph[str(j)][str(i)] = weight  
    
    return graph


def compare_algorithms(graph_sizes):
    results = []

    for size in graph_sizes:
        graph = generate_random_graph(size)

        dijkstra = DijkstraAlgorithm(graph)
        start_node = "0"

        start_time = time.time()
        dijkstra.find_shortest_paths(start_node)
        dijkstra_time = time.time() - start_time

        floyd = FloydWarshallAlgorithm(graph)

        start_time = time.time()
        floyd.shortest_paths()
        floyd_time = time.time() - start_time

        results.append((size, dijkstra_time, floyd_time))
        print(f"Para {size} vértices: Dijkstra {dijkstra_time:.5f}s | Floyd-Warshall {floyd_time:.5f}s")

    return results


if __name__ == "__main__":
    graph_sizes = [10, 20, 50, 100, 200, 500]
    compare_algorithms(graph_sizes)
