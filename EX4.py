from Dijkstra import DijkstraAlgorithm

def find_fastest_route(graph, start, destination):
    dijkstra_instance = DijkstraAlgorithm(graph)
    return dijkstra_instance.find_shortest_path(start, destination)

if __name__ == "__main__":
    cargo_network = {
        'São Paulo': {'Rio de Janeiro': 50, 'Belo Horizonte': 70},
        'Rio de Janeiro': {'São Paulo': 50, 'Brasília': 30, 'Salvador': 20},
        'Belo Horizonte': {'São Paulo': 70, 'Salvador': 40},
        'Brasília': {'Rio de Janeiro': 30, 'Salvador': 10},
        'Salvador': {'Rio de Janeiro': 20, 'Belo Horizonte': 40, 'Brasília': 10}
    }
    
    print("Rota mais barata de São Paulo para Salvador:", find_fastest_route(cargo_network, 'São Paulo', 'Salvador'))