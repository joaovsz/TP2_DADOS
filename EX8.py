from FloydWarshall import FloydWarshallAlgorithm

if __name__ == "__main__":
    # As distâncias estão em quilômetros
    city_routes = {
        'Centro': {'Setor Bueno': 5, 'Setor Oeste': 10},
        'Setor Bueno': {'Centro': 5, 'Setor Marista': 8, 'Setor Sul': 12},
        'Setor Oeste': {'Centro': 10, 'Setor Marista': 6},
        'Setor Marista': {'Setor Bueno': 8, 'Setor Oeste': 6, 'Setor Sul': 7},
        'Setor Sul': {'Setor Bueno': 12, 'Setor Marista': 7}
    }

    floyd = FloydWarshallAlgorithm(city_routes)
    shortest_paths = floyd.shortest_paths()

    print("Menor caminho entre todos os pares:")
    for origin, destinations in shortest_paths.items():
        for destination, distance in destinations.items():
            print(f"{origin} → {destination}: {distance} km")
