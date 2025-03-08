from Dijkstra import DijkstraAlgorithm

class LogisticsDelivery(DijkstraAlgorithm):
    def __init__(self, graph):
        super().__init__(graph)
    
    def find_routes(self, distribution_center):
        return self.find_shortest_path(distribution_center)

if __name__ == "__main__":
    city_graph = {
        'Centro': {'Bairro1': 5, 'Bairro2': 10},
        'Bairro1': {'Centro': 5, 'Bairro3': 8, 'Bairro4': 12},
        'Bairro2': {'Centro': 10, 'Bairro3': 6},
        'Bairro3': {'Bairro1': 8, 'Bairro2': 6, 'Bairro4': 7},
        'Bairro4': {'Bairro1': 12, 'Bairro3': 7}
    }
    
    logistics = LogisticsDelivery(city_graph)
    print("Rotas mais curtas do centro de distribuição:", logistics.find_routes('Centro'))
