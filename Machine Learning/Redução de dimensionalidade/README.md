# 🌲 Redução de Dimensionalidade — Base de Cobertura Vegetal

Este projeto tem como objetivo aplicar técnicas de redução de dimensionalidade — **PCA**, **Kernel PCA** e **LDA** — utilizando uma base de dados de tipos de cobertura vegetal. O foco é comparar o impacto dessas técnicas na performance de um classificador Random Forest.

---

## 📁 Estrutura do Projeto

├── cover_type_num.pkl  
├── dimensionalidade.ipynb  
└── README.md  

---

## 📌 Objetivos

- Carregar e preparar os dados numéricos normalizados da base de cobertura vegetal.
- Dividir os dados em treino (75%) e teste (25%), mantendo a proporção das classes.
- Aplicar redução de dimensionalidade com:
  - PCA com 6 componentes
  - Kernel PCA com 6 componentes e kernel RBF
  - LDA com número de componentes baseado no número de classes
- Treinar um modelo Random Forest para cada técnica e avaliar a acurácia.
- Comparar o desempenho dos modelos e entender o impacto da redução.

---

## 📊 Descrição da Base

A base contém atributos normalizados referentes a regiões geográficas e a variável alvo codificada com LabelEncoder, representando tipos de cobertura vegetal. O arquivo `cover_type_num.pkl` contém os dados prontos para uso.

---

## 🔍 Processos realizados

### Preparação dos dados

- Os dados foram carregados do arquivo `.pkl`.
- Divisão dos dados em treino e teste, com 25% para teste.

### PCA

- Aplicação do PCA para reduzir as dimensões para 6 componentes principais.
- Avaliação da variância explicada por componente.
- Treinamento do Random Forest com dados reduzidos e avaliação da acurácia.

### Kernel PCA

- Aplicação do Kernel PCA com kernel RBF, mantendo 6 componentes.
- Treinamento e avaliação semelhantes ao PCA.

### LDA

- Aplicação do LDA para redução supervisionada, com o número máximo permitido de componentes (n_classes - 1).
- Treinamento e avaliação do modelo com os dados transformados pelo LDA.

---

## ⚙️ Resultados

- O PCA manteve uma boa parcela da variância original e obteve uma acurácia satisfatória.
- O Kernel PCA, por capturar relações não lineares, apresentou desempenho competitivo.
- O LDA, que utiliza a informação das classes para reduzir dimensões, mostrou-se eficiente quando o número de componentes respeitou o limite permitido.

---

## 📚 Bibliotecas Utilizadas

- `pickle` para carregar os dados pré-processados  
- `scikit-learn` para PCA, Kernel PCA, LDA, Random Forest, métricas e divisão dos dados  
- `numpy` e `pandas` para manipulação dos dados (caso necessário)

---

## 📝 Conclusão

A redução de dimensionalidade mostrou-se útil para simplificar os dados e acelerar o treinamento do modelo, sem perda significativa de desempenho.  
Cada técnica possui suas vantagens: PCA para redução geral, Kernel PCA para dados com estrutura não linear e LDA para casos supervisionados com múltiplas classes.

---

## 👨‍💻 Autor

Matheus — Estudante de Análise e Desenvolvimento de Sistemas com foco em Ciência de Dados.
