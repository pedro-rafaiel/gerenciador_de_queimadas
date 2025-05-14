---

## 📘 README.md – Simulador de Combate a Queimadas com Grafos

### 🔥 Projeto da disciplina de Algoritmos em Grafos

---

### 📌 Objetivo

Este projeto simula o combate a incêndios em regiões representadas por grafos. O foco é modelar a propagação do fogo e a atuação de brigadistas para conter o incêndio, levando em consideração:

* Custo das rotas,
* Recursos limitados,
* Pontos de coleta de água,
* E requisitos específicos de combate por local.

---

### 🧠 Algoritmos usados

* **BFS (Busca em Largura)**:
  Utilizado para simular a propagação do fogo em tempos discretos, partindo de um vértice inicial e se espalhando para os vizinhos de forma progressiva.

* **Dijkstra**:
  Aplicado para calcular o caminho de menor custo entre um posto de brigadistas e o vértice em chamas, considerando o peso das arestas (tempo/dificuldade de deslocamento).

---

### ⚙️ Como funciona a simulação

#### 1. **Criação do grafo**

* O grafo é gerado de forma aleatória com número configurável de vértices e arestas.
* Cada aresta possui um peso aleatório representando o custo do deslocamento.

#### 2. **Designação de funções**

* Três vértices aleatórios são definidos como **postos de brigadistas**.
* Dois vértices aleatórios são definidos como **pontos de coleta de água**.
* Os postos também funcionam como pontos de coleta.

#### 3. **Requisitos por vértice**

* Cada vértice exige uma quantidade aleatória de:

  * Litros de água (2 a 6),
  * Equipes de brigadistas (1 ou 2),
    para que o fogo possa ser contido.

#### 4. **Propagação do fogo**

* O fogo começa em um vértice aleatório (ou múltiplos, em simulações sucessivas).
* Ele se propaga para os vizinhos a cada unidade de tempo, com base nos pesos das arestas (simulação baseada em BFS).

#### 5. **Combate ao fogo**

* Os caminhões de brigadistas saem dos postos, seguindo o caminho de menor custo até o local do fogo.
* Se não tiverem água suficiente, vão até o ponto de coleta mais próximo (incluindo os próprios postos).
* Se chegarem **antes do fogo** e tiverem recursos suficientes, o fogo é extinto e o vértice é salvo.

#### 6. **Relatório**

* Para cada vértice como ponto inicial do fogo, o sistema imprime:

  * Quantos vértices foram salvos ou queimados,
  * Tempo total da propagação,
  * Caminhos usados pelos brigadistas,
  * Quantidade total de água utilizada.

---

### 📈 Exemplo de saída (terminal)

```
🔥 Fogo iniciado em: V2
✅ Vértices salvos (3): V0, V1, V4
🔥 Vértices queimados (2): V3, V5
🕒 Tempo total até fim da propagação: 5
💧 Água total usada: 13 litros
🧭 Caminhos dos brigadistas:
  - V0: B -> V0
  - V1: B -> V0 -> V1
  - V4: B -> V3 -> V4
```

---

### 🧪 Testes e limitações

#### ✅ Testado com:

* Diferentes grafos aleatórios
* Múltiplas simulações em sequência
* Verificação de chegada dos brigadistas antes do fogo

#### ⚠️ Limitações:

* Os caminhões não têm reuso entre várias ocorrências.
* Não há controle de reabastecimento após o uso (pode ser estendido).
* O envio de múltiplos caminhões ao mesmo vértice ainda não é otimizado.

---

### 💡 Possíveis melhorias futuras

* Visualização gráfica do grafo e do fogo (ex: com `networkx` + `matplotlib`)
* Interface gráfica para interação com o usuário
* Otimização da alocação de brigadistas (ex: evitar duplicidade)
* Simulação contínua com reabastecimento e múltiplas ondas de fogo

---

### 🚀 Como executar

```bash
python main.py
```

---