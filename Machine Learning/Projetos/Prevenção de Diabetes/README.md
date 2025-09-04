# 🧠 Projeto de Classificação com Machine Learning: Previsão de Diabetes

Este projeto tem como objetivo construir e comparar modelos de classificação utilizando **Machine Learning supervisionado** para prever se um paciente possui diabetes com base em variáveis clínicas. Os dados foram obtidos de um dataset real e amplamente utilizado: o *Pima Indians Diabetes Database*.

---

## 📊 Objetivo do Projeto

Prever o diagnóstico de diabetes em pacientes com base em características médicas, como níveis de glicose, pressão arterial, índice de massa corporal, entre outros. O foco está na **análise exploratória, pré-processamento, modelagem, ajuste de hiperparâmetros e avaliação de desempenho dos modelos**.

---

## 📁 Dados Utilizados

- **Fonte:** Dataset *Pima Indians Diabetes* (Kaggle / UCI)
- **Total de registros:** 768
- **Variável-alvo (`Outcome`)**:
  - `0` → Paciente sem diabetes
  - `1` → Paciente com diabetes

---

## 🧪 Etapas do Projeto

### 1. Carregamento e Entendimento dos Dados
- Análise inicial das variáveis, tipos de dados, presença de valores zero e distribuição das classes.
- Identificação de colunas com valores inválidos (como 0 em variáveis que não podem ser 0, como glicose e pressão arterial).

### 2. Análise Exploratória de Dados (EDA)
- Visualizações com histogramas, boxplots e matriz de correlação.

### 3. Pré-processamento dos Dados
- Tratamento de valores inválidos substituindo zeros por valores ausentes (`NaN`).
- Preenchimento dos `NaNs` com a média de cada coluna (estratégia de imputação).
- Normalização das variáveis com o escalonador MinMaxScaler para trazer os dados para uma escala entre 0 e 1.
- Divisão dos dados em conjuntos de treino e teste (85/15).

---

## 🔍 Modelos Utilizados

Foram testados diversos algoritmos de classificação, com seus hiperparâmetros ajustados via validação cruzada (GridSearchCV):

- Árvore de Decisão (`DecisionTreeClassifier`)
- Floresta Aleatória (`RandomForestClassifier`)
- K-Nearest Neighbors (`KNeighborsClassifier`)
- Regressão Logística (`LogisticRegression`)
- Máquinas de Vetores de Suporte (`SVC`)
- Rede Neural Multicamadas (`MLPClassifier`)

Cada modelo foi avaliado utilizando validação cruzada com 5 divisões (KFold), focando na **métrica de acurácia**.

---

## 🧠 Técnicas e Bibliotecas Utilizadas

- **Manipulação e análise de dados:** `pandas`, `numpy`
- **Visualizações:** `matplotlib`, `seaborn`, `plotly.express`
- **Pré-processamento:** `MinMaxScaler`, `SimpleImputer`
- **Modelos:** `sklearn.tree`, `sklearn.ensemble`, `sklearn.neighbors`, `sklearn.linear_model`, `sklearn.svm`, `sklearn.neural_network`
- **Validação e métricas:** `GridSearchCV`, `KFold`, `accuracy_score`

---

## 📈 Avaliação dos Modelos

Cada modelo foi testado com diferentes combinações de hiperparâmetros, utilizando **validação cruzada** para evitar overfitting e garantir uma avaliação robusta.

As métricas de desempenho permitiram identificar o(s) modelo(s) com maior acurácia na predição da condição de diabetes.

---

## ✅ Conclusão

Este projeto demonstra a aplicação prática do pipeline de machine learning em um problema real de saúde, cobrindo desde a análise de dados até a escolha do melhor modelo. Ele mostra também a importância do pré-processamento, da escolha dos algoritmos e da validação adequada para garantir bons resultados preditivos.

---

## 📌 Próximos Passos

- Avaliar outras métricas além da acurácia (F1-score, precisão, recall)
- Implementar balanceamento de classes (ex: `SMOTE`)
- Fazer o deploy do melhor modelo com uma interface via Streamlit ou Flask
- Testar outros algoritmos como `XGBoost` ou `LightGBM`
