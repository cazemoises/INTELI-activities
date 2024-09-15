# Cálculo da Entropia Inicial para Previsão de Desigualdade Econômica

Olá, querida Cristina! Estou testando um novo modelo de entregas via .md. Acredito que facilite a legibilidade, mas só testando para saber.

## Conjunto de Dados

Usamos o Índice de Gini para prever a desigualdade econômica em diferentes regiões. Temos quatro regiões com os seguintes índices:

- **Região 1**: Índice de Gini = 0.30
- **Região 2**: Índice de Gini = 0.45
- **Região 3**: Índice de Gini = 0.40
- **Região 4**: Índice de Gini = 0.35

Critério para a classificação:
- **Alta Desigualdade**: Índices de Gini acima de 0.40
- **Baixa Desigualdade**: Índices de Gini abaixo de 0.40


> **Aviso**: Pode ser um mal-entendido, mas no enunciado é dito que duas regiões são de alta e duas de baixa desigualdade. A regra usada para classificar determina que os índices precisam ser **acima** de 0.40, que não é o caso da **região 3** (exatamente 0.40), então eu fiz os cálculos considerando uma Região de alta desigualdade e três de baixa  desigualdade.

## Classificação das Regiões

Com base no critério definido, como explicado antes:

- **Região 1**: Índice de Gini = 0.30 → **Baixa Desigualdade**
- **Região 2**: Índice de Gini = 0.45 → **Alta Desigualdade**
- **Região 3**: Índice de Gini = 0.40 → **Baixa Desigualdade**
- **Região 4**: Índice de Gini = 0.35 → **Baixa Desigualdade**

## Distribuição das Classes

- **Alta Desigualdade**: 1 região (Região 2)
- **Baixa Desigualdade**: 3 regiões (Regiões 1, 3, 4)

## Fórmula da Entropia

A fórmula da entropia \( H \) de um conjunto de dados binário é:

$$
H = - p_1 \log_2(p_1) - p_2 \log_2(p_2)
$$

Onde:
- <p>p<span style="font-size: .8rem;">1</span> é a proporção de regiões classificadas como "Alta Desigualdade"</p>
- <p>p<span style="font-size: .8rem;">2</span> é a proporção de regiões classificadas como "Baixa Desigualdade"

## Cálculo das Proporções

$$
p_1 = \frac{1}{4} = 0.25
$$
(proporção de "Alta Desigualdade")
$$
p_2 = \frac{3}{4} = 0.75
$$
(proporção de "Baixa Desigualdade")

## Cálculo da Entropia

Depois, é só substituir os valores na fórmula da entropia:

$$
H = - \left( 0.25 \log_2(0.25) \right) - \left( 0.75 \log_2(0.75) \right)
$$

E então calcular os valores dos logaritmos:

$$
H = - \left( 0.25 \times (-2) \right) - \left( 0.75 \times (-0.415) \right)
$$

$$
H = 0.5 + 0.31125 = 0.81125
$$

## Resultado

A entropia inicial do conjunto de dados é aproximadamente (marromenos):

$$
H \approx 0.811
$$