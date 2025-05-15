import heapq

class CaminhaoBrigada:
    def __init__(self, localizacao, capacidade_agua):
        self.localizacao = localizacao
        self.capacidade_agua = capacidade_agua
        self.agua_restante = capacidade_agua

    def usar_agua(self, quantidade):
        if self.agua_restante < quantidade:
            return False
        self.agua_restante -= quantidade
        return True

    def reabastecer(self):
        print(f" Caminhão reabastecendo em {self.localizacao}")
        self.agua_restante = self.capacidade_agua


class PostoBrigada:
    def __init__(self, localizacao, quantidade_caminhoes, capacidade_caminhao):
        self.localizacao = localizacao
        self.caminhoes = [
            CaminhaoBrigada(localizacao=localizacao, capacidade_agua=capacidade_caminhao)
            for _ in range(quantidade_caminhoes)
        ]

    def enviar_para(self, destino, grafo, pontos_de_coleta):
        for caminhao in self.caminhoes:
            caminho, tempo = grafo.dijkstra(caminhao.localizacao, destino)
            if not caminho:
                continue

            agua_necessaria = len(caminho)  # simulação: 1 litro por vértice

            print(f"\n Caminhão saindo de {caminhao.localizacao} com {caminhao.agua_restante}L de água")
            print(f"    Destino: {destino} | Caminho: {' -> '.join(caminho)} | Tempo: {tempo}")

            if caminhao.agua_restante >= agua_necessaria:
                caminhao.usar_agua(agua_necessaria)
                caminhao.localizacao = destino
                print(f"     Chegou e ainda tem {caminhao.agua_restante}L restantes")
                return caminho, tempo

            else:
                print(f"     Água insuficiente ({caminhao.agua_restante}L). Buscando reabastecimento...")

                menor_tempo = float('inf')
                melhor_rota = None

                for ponto in pontos_de_coleta:
                    caminho_reab, tempo_reab = grafo.dijkstra(caminhao.localizacao, ponto)
                    caminho_final, tempo_final = grafo.dijkstra(ponto, destino)
                    if caminho_reab and caminho_final:
                        tempo_total = tempo_reab + tempo_final
                        if tempo_total < menor_tempo:
                            menor_tempo = tempo_total
                            melhor_rota = caminho_reab[:-1] + caminho_final

                if melhor_rota:
                    print(f"     Fez reabastecimento em ponto de coleta")
                    caminhao.reabastecer()
                    caminhao.usar_agua(len(melhor_rota))
                    caminhao.localizacao = destino
                    print(f"     Caminho após reabastecimento: {' -> '.join(melhor_rota)}")
                    print(f"     Chegou com {caminhao.agua_restante}L restantes")
                    return melhor_rota, menor_tempo

        print(f"   Nenhum caminhão disponível ou com rota viável para {destino}")
        return [], float('inf')
