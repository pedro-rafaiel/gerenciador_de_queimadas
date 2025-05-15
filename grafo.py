import json
import heapq

class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_aresta(self, origem, destino, peso):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        # Como o grafo é não direcionado, adiciona nas duas direções
        self.adjacencia[origem].append((destino, peso))
        self.adjacencia[destino].append((origem, peso))

    def obter_vizinhos(self, vertice):
        return self.adjacencia.get(vertice, [])

    def mostrar_grafo(self):
        for vertice, vizinhos in self.adjacencia.items():
            print(f"{vertice} -> {vizinhos}")

    def dijkstra(self, origem, destino):
        distancias = {vertice: float('inf') for vertice in self.adjacencia}
        anteriores = {vertice: None for vertice in self.adjacencia}
        distancias[origem] = 0

        fila = [(0, origem)]

        while fila:
            distancia_atual, atual = heapq.heappop(fila)

            if atual == destino:
                break

            for vizinho, peso in self.obter_vizinhos(atual):
                nova_distancia = distancia_atual + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    anteriores[vizinho] = atual
                    heapq.heappush(fila, (nova_distancia, vizinho))

        caminho = []
        atual = destino
        while atual:
            caminho.insert(0, atual)
            atual = anteriores[atual]

        return caminho, distancias[destino]

def carregar_grafo_de_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r") as f:
        dados = json.load(f)

    grafo = Grafo()

    for aresta in dados["arestas"]:
        origem = aresta["origem"]
        destino = aresta["destino"]
        peso = aresta["peso"]
        grafo.adicionar_aresta(origem, destino, peso)

    return grafo

