# Criando uma reta com Matlibplot
Este projeto é um programa simples em Python que permite ao usuário criar uma reta a partir de duas coordenadas no plano cartesiano. Ele utiliza a biblioteca Matplotlib para desenhar o gráfico da reta entre os pontos informados.

## Sobre o Programa
1. Solicita ao usuário duas coordenadas para o eixo X e duas para o eixo Y.
2. Verifica se as entradas são válidas (números reais e quantidade correta).
3. Mostra as coordenadas que formam a reta.
4. Cria a reta usando a biblioteca Matplotlib.
5. Permite ao usuário criar várias retas ou sair do programa.

## Funções da Matplotlib usadas no código
Principais funções de matplotlib.pyplot usadas:

Função|Descrição|Exemplo no código
---
plt.plot(x, y)|Plota uma linha conectando os pontos definidos em x e y|Plota a reta entre os pontos dados.
plt.xlabel()|Define o rótulo do eixo X|Ex: plt.xlabel("Eixo X")
plt.ylabel()|Define o rótulo do eixo Y|Ex: plt.ylabel("Eixo Y")
plt.title()|Define o título do gráfico|Ex: plt.title("Criando uma Reta")
plt.grid()|Adiciona uma grade ao gráfico para facilitar leitura|Ex: plt.grid(True)
plt.show()|Exibe o gráfico na tela|Necessário para mostrar o gráfico criado.

## Como usar
1. Execute o script Python.
2. Escolha a opção 1 para criar uma reta.
3. Digite duas coordenadas para o eixo X (exemplo: 0 10).
4. Digite duas coordenadas para o eixo Y (exemplo: 5 15).
5. Visualize a reta no gráfico que aparecerá.
6. Repita ou escolha 0 para sair.

