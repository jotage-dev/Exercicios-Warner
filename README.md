# Lista de Exercícios - Grafos e Estruturas de Dados
**Aluno:** João Guilherme  



## Estrutura do Repositório

- [`exercicio1.py`](./exercicio1.py) - Código fonte do Exercício 1 (Sistema de Agenda).
- [`exercicio4.py`](./exercicio4.py) - Código fonte do Exercício 4 (Validação de Movimento do Cavalo).

---

## Respostas dos Exercícios Teóricos e Práticos

### Exercício 1 - Agenda em Dicionário
A implementação em Python cria um dicionário para gerenciar os contatos. O código lê os dados de forma contínua até que o usuário pressione ENTER deixando a chave em branco. 
*👉 Veja o script completo em [`exercicio1.py`](./exercicio1.py).*

### Exercício 2 - Grafo dos Cavalos (Figura 1)
*Representação Teórica:* As posições atuais dos cavalos representam os vértices iniciais de um grafo. As posições válidas de destino (simulando o movimento em "L") seriam as arestas conectando este ponto de origem aos seus respectivos vértices adjacentes no tabuleiro.

### Exercício 3 - Matriz de Adjacência do Cavalo Branco
A matriz de adjacência (de dimensões 64x64) conteria o valor `1` nas interseções entre a linha da casa atual do cavalo branco (ex: `f3`) e as colunas referentes às suas casas alcançáveis (`d2`, `d4`, `e1`, `e5`, `g1`, `g5`, `h2`, `h4`). Todos os outros espaços dessa linha receberiam o valor `0`.

### Exercício 4 - Validador de Movimentos (Grafo de Xadrez)
Criamos uma função que verifica se a movimentação informada forma um arco válido no grafo do tabuleiro, respeitando os limites da matriz (8x8) e o delta dos eixos x e y para garantir o salto em "L".
*👉 Veja a implementação e os testes rodando em [`exercicio4.py`](./exercicio4.py).*

### Exercício 5 - Lista de Adjacência e Consumo de Memória
**Lista de Adjacência gerada a partir da casa f3:**
`f3 -> [d2, d4, e1, e5, g1, g5, h2, h4]`

**Análise de Desempenho e Memória:**
A **Lista de Adjacência** consome consideravelmente menos espaço. Como os movimentos do cavalo em um tabuleiro resultam em um grafo bastante "esparso", a lista armazena estritamente as conexões que existem. Por outro lado, a Matriz de Adjacência força a alocação de 4096 posições (64x64), a esmagadora maioria sendo inútil (preenchida com zeros), ocupando muita memória à toa.

### Exercício 6 - Graus dos Vértices
Considerando o tabuleiro de xadrez como um grafo não-direcionado:
- **Grau máximo (8):** Acontece nas 16 casas da região central do tabuleiro (um retângulo de `c3` até `f6`). Exemplo: A casa **d4** possui grau 8, pois o cavalo tem espaço para seus 8 pulos teóricos.
- **Grau mínimo (2):** Ocorre nas 4 pontas isoladas do tabuleiro (`a1`, `a8`, `h1` e `h8`). Exemplo: Estando em **a1**, o cavalo só consegue saltar para `b3` e `c2`, resultando em apenas 2 arestas.
