from Dijkstra import DijkstraAlgorithm

def find_fastest_route(graph, start, destination):
    dijkstra_instance = DijkstraAlgorithm(graph)
    return dijkstra_instance.find_shortest_path(start, destination)

if __name__ == "__main__":
    city_graph = {
        'Terminal': {'BairroA': 10, 'BairroB': 15},
        'BairroA': {'Terminal': 10, 'BairroC': 12, 'BairroD': 8},
        'BairroB': {'Terminal': 15, 'BairroC': 10},
        'BairroC': {'BairroA': 12, 'BairroB': 10, 'BairroD': 5},
        'BairroD': {'BairroA': 8, 'BairroC': 5}
    }

    result = find_fastest_route(city_graph, 'Terminal', 'BairroD')
    print("Melhor rota de ônibus de Terminal para BairroD:", result)
