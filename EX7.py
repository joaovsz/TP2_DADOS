from PrimAlgorithm import PrimAlgorithm

if __name__ == "__main__":
    internet_network = {
        'Setor Bueno': {'Setor Oeste': 4, 'Setor Marista': 8},
        'Setor Oeste': {'Setor Bueno': 4, 'Setor Sul': 6, 'Setor Universitário': 3},
        'Setor Marista': {'Setor Bueno': 8, 'Setor Universitário': 5},
        'Setor Sul': {'Setor Oeste': 6, 'Setor Pedro Ludovico': 2},
        'Setor Universitário': {'Setor Oeste': 3, 'Setor Marista': 5, 'Setor Pedro Ludovico': 4},
        'Setor Pedro Ludovico': {'Setor Sul': 2, 'Setor Universitário': 4, 'Jardim Goiás': 6},
        'Jardim Goiás': {'Setor Pedro Ludovico': 6}
    }

    prim = PrimAlgorithm(internet_network)
    mst, total_cost = prim.minimum_spanning_tree('Setor Bueno')

    print(f"Árvore Geradora Mínima: {mst}")
    print(f"Custo total: R${total_cost}")
