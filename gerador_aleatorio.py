import random

def gerar_grafo_aleatorio(num_vertices=6, num_arestas=8, peso_min=1, peso_max=5):
    vertices = [f"V{i}" for i in range(num_vertices)]
    arestas = set()

    while len(arestas) < num_arestas:
        origem, destino = random.sample(vertices, 2)
        if (origem, destino) not in arestas and (destino, origem) not in arestas:
            peso = random.randint(peso_min, peso_max)
            arestas.add((origem, destino, peso))

    grafo_dict = {
        "vertices": vertices,
        "arestas": [
            {"origem": o, "destino": d, "peso": p} for o, d, p in arestas
        ]
    }

    postos = random.sample(vertices, 3)
    pontos_de_coleta = random.sample([v for v in vertices if v not in postos], 2)
    origem_fogo = random.choice([v for v in vertices if v not in postos])

    return grafo_dict, postos, pontos_de_coleta, origem_fogo
