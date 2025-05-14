from collections import deque

def calcular_tempo_fogo(grafo, origem_incendio):
    """
    Retorna um dicionário com o tempo em que o fogo chega a cada vértice.
    """
    tempo_fogo = {origem_incendio: 0}
    fila = deque([(origem_incendio, 0)])

    while fila:
        atual, tempo = fila.popleft()

        for vizinho, peso in grafo.obter_vizinhos(atual):
            novo_tempo = tempo + peso
            if vizinho not in tempo_fogo or novo_tempo < tempo_fogo[vizinho]:
                tempo_fogo[vizinho] = novo_tempo
                fila.append((vizinho, novo_tempo))

    return tempo_fogo


def simular_combate_fogo(grafo, origem_incendio, postos, pontos_de_coleta, agua_necessaria, brigadistas_necessarios):
    tempo_fogo = calcular_tempo_fogo(grafo, origem_incendio)
    resultado = {}
    caminhos = {}
    total_agua_usada = 0
    tempo_total = max(tempo_fogo.values())

    print(f"\n🔄 Simulando combate com fogo iniciado em {origem_incendio}...\n")

    for vertice in sorted(tempo_fogo, key=tempo_fogo.get):
        agua_req = agua_necessaria.get(vertice, 3)
        brigadistas_req = brigadistas_necessarios.get(vertice, 1)
        tempo_queima = tempo_fogo[vertice]
        pode_apagar = False

        print(f"\n🔥 Fogo chegará em {vertice} no tempo {tempo_queima}")
        print(f"➡️ Requisitos: {agua_req}L de água, {brigadistas_req} brigadistas")

        for posto in postos:
            caminho, tempo = posto.enviar_para(vertice, grafo, pontos_de_coleta)
            if caminho:
                print(f"🚒 Posto {posto.localizacao} → {vertice}")
                print(f"    Caminho: {' -> '.join(caminho)} | Tempo estimado: {tempo}")
                print(f"    Caminhões disponíveis: {len(posto.caminhoes)}")
                for idx, c in enumerate(posto.caminhoes):
                    print(f"      🛻 Caminhão {idx + 1}: {c.agua_restante}/{c.capacidade_agua}L em {c.localizacao}")

                if tempo < tempo_queima:
                    # Verifica caminhões disponíveis com água suficiente
                    caminhoes_ok = [c for c in posto.caminhoes if c.agua_restante >= agua_req]

                    if len(caminhoes_ok) >= brigadistas_req:
                        caminhao_usado = caminhoes_ok[0]
                        caminhao_usado.usar_agua(agua_req)
                        caminhao_usado.localizacao = vertice
                        print(f"    ✅ Chegou com {agua_req}L e apagou o fogo. Restante: {caminhao_usado.agua_restante}L")
                        pode_apagar = True
                        caminhos[vertice] = caminho
                        total_agua_usada += agua_req
                        break
                    else:
                        print("    ❌ Chegou a tempo, mas sem água ou caminhões suficientes.")
                else:
                    print("    ❌ Chegou tarde demais, o fogo já queimou o local.")
            else:
                print(f"    ❌ Nenhum caminho viável até {vertice}")

        resultado[vertice] = "✅ Salvo" if pode_apagar else "🔥 Queimado"

    salvos = [v for v in resultado if resultado[v] == "✅ Salvo"]
    queimados = [v for v in resultado if resultado[v] == "🔥 Queimado"]

    return {
        "inicio": origem_incendio,
        "salvos": salvos,
        "queimados": queimados,
        "tempo_total": tempo_total,
        "agua_usada": total_agua_usada,
        "caminhos": caminhos
    }
