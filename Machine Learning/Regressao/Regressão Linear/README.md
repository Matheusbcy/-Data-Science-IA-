# 🧠 Regressão com Dataset de Telemonitoramento de Parkinson

Este projeto tem como objetivo aplicar técnicas de regressão utilizando dados biomédicos de pacientes com Parkinson. As etapas incluem carregamento dos dados, exploração, pré-processamento, modelagem com regressão linear e avaliação de desempenho.

---
## 1. 📥 Preparação dos Dados

- Foi utilizado o dataset "Parkinson's Telemonitoring" da UCI Machine Learning Repository.
- O conjunto de dados foi importado com a biblioteca `ucimlrepo`, que permite acessar diretamente repositórios públicos.
- O dataset contém 42 pacientes com Parkinson, totalizando 5.875 gravações de voz.
- A variável `sex` foi transformada de valores numéricos (0/1) para `male` e `female`, conforme a documentação do dataset.
- Em seguida, foi selecionada apenas a variável `total_UPDRS` como alvo da regressão.
- As variáveis preditoras e a variável alvo foram unidas em um único DataFrame.
- Os dados foram salvos em formato `.csv` em uma pasta no Google Drive.

---

## 2. 📊 Análise Exploratória

- Os dados foram recarregados a partir do arquivo `.csv` salvo.
- Foram geradas estatísticas descritivas para compreender a distribuição das variáveis.
- Foi feita a verificação da presença de valores ausentes.
- A correlação entre os atributos numéricos foi calculada e visualizada com um heatmap.
- A matriz de correlação permitiu identificar possíveis relações entre as variáveis de entrada e a variável de saída `total_UPDRS`.

---

## 3. 🧹 Pré-processamento

- A variável categórica `sex` foi novamente convertida para valores numéricos, com `0` representando `male` e `1` representando `female`.
- Os dados foram divididos em atributos preditores (`X`) e alvo (`y`).
- Em seguida, foram separados em conjuntos de treino e teste com uma proporção de 75% para treino e 25% para teste, utilizando uma semente de aleatoriedade para reprodutibilidade.
- As dimensões de cada conjunto foram verificadas para garantir a integridade dos dados.
- Por fim, os dados foram salvos em formato `.pkl`, para facilitar o reuso nas etapas seguintes.

---

## 4. 📈 Regressão Linear

- Foi utilizado o algoritmo de Regressão Linear Múltipla.
- O modelo foi treinado com os dados de treino e seus coeficientes e intercepto foram exibidos.
- O desempenho do modelo foi avaliado por meio do coeficiente de determinação (R²) tanto no treino quanto no teste.
- As previsões foram comparadas com os valores reais usando gráficos para identificar o quanto as curvas estavam sobrepostas.
- A diferença entre os valores preditos e reais indicou que o modelo teve um desempenho ruim.

---

## 5. 📉 Avaliação dos Erros

- Foi calculado o erro absoluto médio (MAE) para o conjunto de teste, tanto utilizando bibliotecas quanto cálculos manuais.
- Em seguida, foi calculado o erro quadrático médio (MSE) e sua raiz (RMSE), para entender melhor a escala do erro.
- Por fim, um gráfico de resíduos foi gerado com a biblioteca Yellowbrick, reforçando a má performance do modelo.

---

## 📌 Conclusão

O modelo de regressão linear não apresentou bom desempenho ao prever a variável `total_UPDRS`, evidenciado pelos baixos scores e alta divergência entre valores reais e preditos. Isso abre espaço para experimentar outros algoritmos mais robustos e técnicas adicionais de pré-processamento.

---

## ✅ Próximos Passos

- Testar algoritmos de regressão mais complexos: SVR, MLP, Decision Tree, Random Forest.
- Realizar ajuste de hiperparâmetros.
- Aplicar técnicas de engenharia de atributos e normalização.
- Avaliar métricas adicionais e interpretar os resíduos de forma mais profunda.

---

**Fonte dos dados:** [UCI Parkinson Telemonitoring Dataset](https://archive.ics.uci.edu/dataset/189/parkinsons+telemonitoring)  
**Autor:** Matheus Freitas  
**Curso:** Machine Learning / Ciência de Dados - IA EXPERT ACADEMY
