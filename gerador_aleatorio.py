import random

def gerar_grafo_aleatorio(num_vertices=6, num_arestas_extra=1, peso_min=1, peso_max=5):
    vertices = [f"V{i}" for i in range(num_vertices)]
    arestas = set()

    for i in range(1, num_vertices):
        origem = vertices[i]
        destino = random.choice(vertices[:i])
        peso = random.randint(peso_min, peso_max)
        arestas.add((origem, destino, peso))

    while len(arestas) < num_vertices - 1 + num_arestas_extra:
        origem, destino = random.sample(vertices, 2)
        if origem != destino and not any(
            (o == origem and d == destino) or (o == destino and d == origem)
            for o, d, _ in arestas
        ):
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
