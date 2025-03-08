from PrimAlgorithm import PrimAlgorithm

if __name__ == "__main__":
    water_distribution = {
        'Setor Central': {'Setor Oeste': 3000, 'Setor Sul': 6000},
        'Setor Oeste': {'Setor Central': 3000, 'Setor Bueno': 5000, 'Setor Marista': 2000},
        'Setor Sul': {'Setor Central': 6000, 'Setor Marista': 7000},
        'Setor Bueno': {'Setor Oeste': 5000, 'Setor Nova Suíça': 4000},
        'Setor Marista': {'Setor Oeste': 2000, 'Setor Sul': 7000, 'Setor Nova Suíça': 3000},
        'Setor Nova Suíça': {'Setor Bueno': 4000, 'Setor Marista': 3000}
    }

    prim = PrimAlgorithm(water_distribution)
    mst, total_cost = prim.minimum_spanning_tree('Setor Central')

    print(f"Árvore Geradora Mínima: {mst}")
    print(f"Custo total: R$ {total_cost}")
