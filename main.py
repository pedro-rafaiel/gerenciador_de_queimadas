from grafo import Grafo
from gerador_aleatorio import gerar_grafo_aleatorio
from brigadistas import PostoBrigada
from simulador import simular_combate_fogo
from incendio import simular_propagacao_fogo
import random
import sys
import datetime

agora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
arquivo = open(f"relatorio_{agora}.txt", "w", encoding="utf-8")
sys.stdout = arquivo

# Gera o grafo e posições aleatórias de postos, coleta e foco inicial
grafo_dados, postos, pontos_de_coleta, origem_incendio = gerar_grafo_aleatorio()

grafo = Grafo()
for aresta in grafo_dados["arestas"]:
    grafo.adicionar_aresta(aresta["origem"], aresta["destino"], aresta["peso"])

grafo.mostrar_grafo()

print(f"\n Postos de Brigadistas: {postos}")
print(f" Pontos de Coleta de Água: {pontos_de_coleta}")
print(f" Incêndio começa em: {origem_incendio}")

pontos_de_coleta_completos = list(set(pontos_de_coleta + postos))

agua_necessaria = {}
brigadistas_necessarios = {}
for vertice in grafo.adjacencia:
    agua_necessaria[vertice] = random.randint(2, 6)
    brigadistas_necessarios[vertice] = random.randint(1, 2)

print("\n Requisitos por vértice:")
for v in sorted(grafo.adjacencia):
    print(f"{v}: {agua_necessaria[v]}L de água, {brigadistas_necessarios[v]} brigadista(s)")

# Simula a propagação do fogo (usando BFS)
_, tempos = simular_propagacao_fogo(grafo, origem_incendio)
print(f"\n Propagação do fogo a partir de '{origem_incendio}':")
for v in sorted(tempos, key=tempos.get):
    print(f"{v} queimado no tempo {tempos[v]}")

postos_objetos = [
    PostoBrigada(localizacao=p, quantidade_caminhoes=2, capacidade_caminhao=10)
    for p in postos
]

print("\nRESULTADO GERAL DAS SIMULAÇÕES:\n")

for origem in grafo.adjacencia:
    if origem in postos:
        continue

    dados = simular_combate_fogo(
        grafo,
        origem,
        postos_objetos,
        pontos_de_coleta_completos,
        agua_necessaria,
        brigadistas_necessarios
    )

    print("────────────────────────────────────────")
    print(f"Fogo iniciado em: {dados['inicio']}")
    print(f"Vértices salvos ({len(dados['salvos'])}): {', '.join(dados['salvos'])}")
    print(f"Vértices queimados ({len(dados['queimados'])}): {', '.join(dados['queimados'])}")
    print(f"Tempo total até fim da propagação: {dados['tempo_total']}")
    print(f"Água total usada: {dados['agua_usada']} litros")

    print("Caminhos dos brigadistas:")
    if dados['caminhos']:
        for destino, caminho in dados['caminhos'].items():
            print(f"  - {destino}: {' -> '.join(caminho)}")
    else:
        print("  Nenhum brigadista conseguiu chegar a tempo.")

sys.stdout = sys.__stdout__
arquivo.close()
print(f"\n✅ Relatório salvo como relatorio_{agora}.txt")
