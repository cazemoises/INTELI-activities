# Classificação de Intenções de um Chatbot com NLU

## Resumo

Este projeto tem como objetivo treinar um modelo de Natural Language Understanding (NLU) para classificar intenções em um chatbot. Foi usada uma base de dados com perguntas, intenções e respostas associadas. Foram contemplados os treinamentos de dois modelos diferentes: um utilizando uma rede neural com TensorFlow, e outro utilizando vetorização Word2Vec combinada com um classificador SVM.

## Estrutura do Projeto

- **Dataset**: O conjunto de dados contém perguntas e intenções associadas, pré-processadas para serem usadas como entrada para os modelos.
- **Modelos**:
  - **Rede Neural com TensorFlow**: Uso de um modelo com camadas de Embedding, Conv1D, LSTM, Dense, e Dropout para classificar as intenções.
  - **Word2Vec + SVM**: Vetorização das perguntas usando Word2Vec e uso de um SVM para a classificação.
- **Avaliação**: Métricas de acurácia, recall, e F1-score foram calculadas para ambos os modelos. Os resultados foram analisados utilizando TensorBoard para a rede neural e comparados com a abordagem Word2Vec.

## Instruções para Execução

### 1. Requisitos

Certifique-se de ter as seguintes dependências instaladas:

- Python 3.12.4
- TensorFlow
- Scikit-Learn
- Gensim
- Pandas
- Seaborn
- Matplotlib
- TensorBoard

Você pode instalar as dependências usando pip:

```bash
pip install tensorflow scikit-learn gensim pandas seaborn matplotlib imbalanced-learn
