from PrimAlgorithm import PrimAlgorithm

if __name__ == "__main__":
    phone_network = {
        'Torre_A': {'Torre_B': 5, 'Torre_C': 9},
        'Torre_B': {'Torre_A': 5, 'Torre_D': 4, 'Torre_E': 7},
        'Torre_C': {'Torre_A': 9, 'Torre_E': 6},
        'Torre_D': {'Torre_B': 4, 'Torre_F': 3},
        'Torre_E': {'Torre_B': 7, 'Torre_C': 6, 'Torre_F': 8},
        'Torre_F': {'Torre_D': 3, 'Torre_E': 8}
    }

    prim = PrimAlgorithm(phone_network)
    mst, total_cost = prim.minimum_spanning_tree('Torre_A')

    print(f"Árvore Geradora Mínima: {mst}")
    print(f"Custo total: R$ {total_cost},00")
