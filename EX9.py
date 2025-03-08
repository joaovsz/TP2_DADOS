from PrimAlgorithm import PrimAlgorithm

if __name__ == "__main__":
    power_grid = {
        'São Paulo': {'Rio de Janeiro': 700, 'Belo Horizonte': 900},
        'Rio de Janeiro': {'São Paulo': 700, 'Curitiba': 600, 'Brasília': 400},
        'Belo Horizonte': {'São Paulo': 900, 'Brasília': 800},
        'Curitiba': {'Rio de Janeiro': 600, 'Porto Alegre': 300},
        'Brasília': {'Rio de Janeiro': 400, 'Belo Horizonte': 800, 'Porto Alegre': 500},
        'Porto Alegre': {'Curitiba': 300, 'Brasília': 500}
    }

    prim = PrimAlgorithm(power_grid)
    mst, total_cost = prim.minimum_spanning_tree('São Paulo')

    print(f"Árvore Geradora Mínima: {mst}")
    print(f"Custo total: R$ {total_cost}")
