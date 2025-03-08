from Dijkstra import DijkstraAlgorithm

class LogisticsDelivery(DijkstraAlgorithm):
    def __init__(self, graph):
        super().__init__(graph)
    
    def find_routes(self, distribution_center):
        shortest_paths = self.find_shortest_path(distribution_center)
        return {destination: f"{distance} km" for destination, distance in shortest_paths.items()}

if __name__ == "__main__":
    city_graph = {
        'Setor Central': {'Setor Bueno': 5.0, 'Setor Oeste': 10.0},
        'Setor Bueno': {'Setor Central': 5.0, 'Setor Marista': 8.0, 'Setor Sul': 12.0},
        'Setor Oeste': {'Setor Central': 10.0, 'Setor Marista': 6.0},
        'Setor Marista': {'Setor Bueno': 8.0, 'Setor Oeste': 6.0, 'Setor Sul': 7.0},
        'Setor Sul': {'Setor Bueno': 12.0, 'Setor Marista': 7.0}
    }
    
    logistics = LogisticsDelivery(city_graph)
    print("Rotas mais curtas do centro de distribuição:", logistics.find_routes('Setor Central'))
