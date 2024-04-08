# Lunar Lander Reinforcement Learning Project

## Descrição

Este projeto envolve o treinamento de um agente de aprendizado por reforço no ambiente `LunarLander` utilizando algoritmos modernos de RL. O objetivo é desenvolver um agente capaz de pousar com sucesso um módulo de pouso lunar entre as bandeiras de pouso. A simulação e o treinamento são feitos utilizando o `gymnasium` para o ambiente e `stable_baselines3` para os algoritmos de RL.

## Instalação

> [!WARNING]
> Antes de iniciar, certifique-se de ter Python 3.7+ instalado em sua máquina. Siga os passos abaixo para configurar o ambiente:

```bash
pip install gymnasium[box2d] matplotlib stable_baselines3
```

## Uso

### Notebook Jupyter

Para interagir com o projeto através do notebook Jupyter, inicie o Jupyter Lab ou Notebook e abra o arquivo `Lunar_Lander.ipynb`.

### Script Python

Para o Script Python também disponível, você pode executá-lo diretamente:

```bash
python lunar_lander.py
```

## Estrutura do Projeto

1. **Exploração do Ambiente:** Uma introdução ao ambiente LunarLander e suas regras.
2. **Algoritmo de RL Utilizado:** Descrição do algoritmo de RL escolhido e sua implementação.
3. **Processo de Treinamento:** Como o agente é treinado, incluindo hiperparâmetros e estratégias de otimização.
4. **Resultados e Avaliação:** Como os resultados são avaliados e quais métricas são usadas.