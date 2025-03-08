from Dijkstra import DijkstraAlgorithm

def find_fastest_route(graph, start, destination):
    dijkstra_instance = DijkstraAlgorithm(graph)
    return dijkstra_instance.find_shortest_path(start, destination)

if __name__ == "__main__":
    air_network = {
        'GRU - São Paulo': {'GIG - Rio de Janeiro': 500, 'BSB - Brasília': 700},
        'GIG - Rio de Janeiro': {'GRU - São Paulo': 500, 'REC - Recife': 300, 'POA - Porto Alegre': 200},
        'BSB - Brasília': {'GRU - São Paulo': 700, 'POA - Porto Alegre': 400},
        'REC - Recife': {'GIG - Rio de Janeiro': 300, 'POA - Porto Alegre': 100},
        'POA - Porto Alegre': {'GIG - Rio de Janeiro': 200, 'BSB - Brasília': 400, 'REC - Recife': 100}
    }
    
    print("Melhor rota aérea de Aeroporto1 para Aeroporto5:", find_fastest_route(air_network, 'Aeroporto1', 'Aeroporto5'))
