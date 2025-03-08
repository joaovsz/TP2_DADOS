from DijkstraModified import DijkstraModifiedAlgorithm

if __name__ == "__main__":
    city_graph = {
        'Rua das Flores': {'Avenida Central': 5, 'Rua do Comércio': 10},
        'Avenida Central': {'Rua das Flores': 5, 'Rua da Paz': 8, 'Rua do Lago': 12},
        'Rua do Comércio': {'Rua das Flores': 10, 'Rua da Paz': 6},
        'Rua da Paz': {'Avenida Central': 8, 'Rua do Comércio': 6, 'Rua do Lago': 7},
        'Rua do Lago': {'Avenida Central': 12, 'Rua da Paz': 7, 'Rua das Árvores': 9},
        'Rua das Árvores': {'Rua do Lago': 9, 'Rua da Esperança': 4},
        'Rua da Esperança': {'Rua das Árvores': 4, 'Rua do Mercado': 6},
        'Rua do Mercado': {'Rua da Esperança': 6}
    }
    
    charging_stations = ['Avenida Central', 'Rua do Lago', 'Rua do Mercado']
    
    smart_dijkstra = DijkstraModifiedAlgorithm(graph=city_graph, charging_stations=charging_stations)
    
    start, destination, autonomy = 'Rua das Flores', 'Rua do Mercado', 15
    routes = smart_dijkstra.find_best_routes(start, destination, autonomy)
    
    if routes:
        print("Melhores rotas encontradas:")
        for i, (route, time) in enumerate(routes, 1):
            print(f"{i}. Rota: {route}, Tempo total: {time} min")
    else:
        print("Não há rota viável com a autonomia fornecida.")
