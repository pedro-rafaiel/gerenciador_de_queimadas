## Simulador de Combate a Queimadas com Grafos

### Projeto da disciplina de Algoritmos em Grafos – 2024.2

---

### Objetivo

Este projeto simula o combate a incêndios em regiões representadas por grafos. O sistema modela a propagação do fogo e a atuação de brigadistas, considerando:

- Custo dos caminhos entre regiões
- Quantidade limitada de água por caminhão
- Pontos de coleta de água
- Requisitos de recursos em cada vértice para extinguir o fogo

---

### Algoritmos utilizados

- **BFS (Busca em Largura)**  
  Usado para simular a propagação do fogo ao longo dos vértices, atribuindo um tempo de queima baseado nas distâncias (pesos das arestas).

- **Dijkstra**  
  Aplicado para encontrar os caminhos de menor custo entre um caminhão de brigada e um vértice em chamas ou um ponto de coleta de água.

---

### Como funciona a simulação

#### 1. Criação do grafo
- O grafo é gerado aleatoriamente com número configurável de vértices e arestas.
- É garantido que o grafo seja conexo.
- As arestas possuem pesos aleatórios que representam tempo ou dificuldade de deslocamento.

#### 2. Designação dos elementos
- Três vértices aleatórios são definidos como postos de brigada.
- Dois vértices aleatórios são definidos como pontos de coleta de água (além dos postos).
- Os postos também funcionam como pontos de coleta.

#### 3. Requisitos por vértice
- Cada vértice exige:
  - Uma quantidade de água (entre 2 e 6 litros)
  - Uma quantidade de brigadistas (1 ou 2)

#### 4. Propagação do fogo
- O fogo começa em um vértice aleatório (ou múltiplos, um por simulação).
- Propaga-se para os vizinhos com base nos tempos das arestas (BFS adaptado).

#### 5. Combate ao fogo
- Cada caminhão de brigada:
  - Possui uma capacidade fixa de água
  - Parte do posto e segue até o local afetado
  - Se não tiver água suficiente, vai ao ponto de coleta mais próximo, reabastece e continua
- O fogo é apagado se o caminhão chega antes da queima e atende aos requisitos de água e equipe

#### 6. Registro e relatório
- A simulação roda uma vez para cada vértice (exceto os que são postos)
- Para cada simulação, é registrado:
  - Vértices salvos e queimados
  - Tempo total da propagação
  - Caminhos seguidos pelos brigadistas
  - Quantidade total de água usada
- Todo o conteúdo impresso no terminal também é salvo automaticamente em um arquivo `.txt`

---

### Exemplo de saída

```
Fogo iniciado em: V2
Vértices salvos (4): V0, V1, V3, V6
Vértices queimados (2): V4, V5
Tempo total até fim da propagação: 6
Água total usada: 15 litros
Caminhos dos brigadistas:
  - V0: V1 -> V0
  - V1: V1
  - V3: V1 -> V3
  - V6: V1 -> V3 -> V6
```

---

### Testes realizados e limitações

#### Testes
- Diferentes grafos aleatórios com até 20 vértices
- Diversos focos de incêndio sucessivos
- Validação de chegada antes da queima
- Verificação da lógica de reabastecimento

#### Limitações
- Os caminhões não são otimizados para múltiplas missões simultâneas
- Ainda não há balanceamento inteligente entre caminhões disponíveis
- Visualização apenas via terminal

---

### Possíveis melhorias futuras
- Visualização gráfica do grafo e propagação do fogo
- Interface com botões para iniciar ou resetar simulações
- Heurística para distribuição mais eficiente dos brigadistas
- Simulação contínua com reabastecimento e múltiplas ondas de fogo

---

### Como executar

1. Certifique-se de ter Python instalado
2. Execute o projeto com:

```bash
python main.py
```

3. Ao fim da execução, será gerado um relatório no formato:

```
relatorio.txt
```

#### Esse arquivo tem toda a simulação realizada.

* Criadores: Pedro Rafael e Vinícius Inácio
* Professor da Disciplina: Carlos Vinícius