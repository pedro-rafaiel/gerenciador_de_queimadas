from collections import deque

def simular_propagacao_fogo(grafo, vertice_inicial):
    # Usa BFS para propagar o fogo em ondas
    queimados = set()
    tempo_por_vertice = {}
    fila = deque()

    # Começa o fogo no vértice inicial no tempo 0
    fila.append((vertice_inicial, 0))
    queimados.add(vertice_inicial)
    tempo_por_vertice[vertice_inicial] = 0

    while fila:
        atual, tempo = fila.popleft()
        for vizinho, _ in grafo.obter_vizinhos(atual):
            if vizinho not in queimados:
                # Marca o vizinho como queimado e define o tempo de queima
                queimados.add(vizinho)
                tempo_por_vertice[vizinho] = tempo + 1
                fila.append((vizinho, tempo + 1))

    return queimados, tempo_por_vertice
