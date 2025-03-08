from DijkstraModified import DijkstraModifiedAlgorithm

if __name__ == "__main__":
    flight_graph = {
        'GRU - São Paulo': {'JFK - Nova York': (800, 2), 'LHR - Londres': (1200, 3)},
        'JFK - Nova York': {'GRU - São Paulo': (800, 2), 'CDG - Paris': (500, 1.5), 'DXB - Dubai': (900, 4)},
        'LHR - Londres': {'GRU - São Paulo': (1200, 3), 'CDG - Paris': (200, 1), 'DXB - Dubai': (850, 4)},
        'CDG - Paris': {'JFK - Nova York': (500, 1.5), 'LHR - Londres': (200, 1), 'HKG - Hong Kong': (950, 5)},
        'DXB - Dubai': {'JFK - Nova York': (900, 4), 'LHR - Londres': (850, 4), 'HKG - Hong Kong': (700, 3)},
        'HKG - Hong Kong': {'CDG - Paris': (950, 5), 'DXB - Dubai': (700, 3)}
    }

    mandatory_stops = {
        ('JFK - Nova York', 'DXB - Dubai'): 100,
        ('LHR - Londres', 'HKG - Hong Kong'): 150
    }

    max_connection_time = 5.0  # Aumentado para permitir mais conexões

    flight_dijkstra = DijkstraModifiedAlgorithm(flight_graph=flight_graph, mandatory_stops=mandatory_stops, max_connection_time=max_connection_time)
    
    start, destination = 'GRU - São Paulo', 'HKG - Hong Kong'
    routes = flight_dijkstra.find_cheapest_routes(start, destination)
    
    if routes:
        print("Rotas mais econômicas encontradas:")
        for i, (route, cost) in enumerate(routes, 1):
            print(f"{i}. Rota: {route}, Custo total: R${cost}")
    else:
        print("Não há rota viável dentro das restrições definidas.")
