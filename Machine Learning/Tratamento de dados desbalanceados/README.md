# 🌲 Tratamento de Dados Desbalanceados — Cobertura Vegetal

Este projeto tem como objetivo aplicar técnicas de balanceamento de dados — **subamostragem com Tomek Links** e **sobreamostragem com SMOTE** — utilizando uma base de dados de tipos de cobertura vegetal. O projeto foi desenvolvido em Python, com foco em experimentação e avaliação do impacto das técnicas sobre um modelo de classificação.

---

## 📁 Estrutura do Projeto


├── cover_type.csv
└── cover_type.pkl
└── dados.ipynb
└── README.md

---

## 📌 Objetivos

- Visualizar o desbalanceamento entre classes da base.
- Aplicar subamostragem com **Tomek Links**.
- Aplicar sobreamostragem com **SMOTE**.
- Treinar um **RandomForestClassifier** com os dados balanceados.
- Avaliar a acurácia e o relatório de classificação dos modelos.

---

## 📊 Descrição da Base

A base utilizada contém atributos sobre regiões geográficas e seu respectivo tipo de cobertura vegetal. A variável-alvo é a coluna `Cover_Type`, com múltiplas classes (multiclasse).  

O arquivo `.csv` contém os dados brutos e o arquivo `.pkl` contém os dados já pré-processados.

---

## 🔍 Análise Inicial

- A variável `Cover_Type` foi analisada com `value` e com gráfico de barras via Seaborn.
- A distribuição revelou forte desbalanceamento entre as classes.

---

## ⚙️ Subamostragem com Tomek Links

- Utilizamos `TomekLinks(sampling_strategy="all")` apenas sobre os dados de **treinamento**.
- As classes majoritárias foram reduzidas ao remover pares Tomek.
- Após a subamostragem:
  - Algumas classes foram mais bem representadas.
  - Outras perderam muitos exemplos.

### 🧠 Treinamento

- Modelo: `RandomForestClassifier`
- Acurácia: **ligeiramente menor** que a versão sem balanceamento (80.64%).

---

## 🔁 Sobreamostragem com SMOTE

- Utilizamos `SMOTE(sampling_strategy="auto")`, que gera novas amostras para todas as classes **menos a majoritária**.
- Isso equilibra a base sem remover exemplos reais.

### 🧠 Treinamento

- Modelo: `RandomForestClassifier`
- Acurácia: **similar** à versão original.
- O recall das classes minoritárias aumentou, embora a precisão tenha diminuído.

---


## 📚 Bibliotecas Utilizadas

- `pandas`, `numpy`
- `matplotlib`, `seaborn`
- `scikit-learn`
- `imblearn`

---

## 📝 Conclusão

Tanto o SMOTE quanto o Tomek Links mostraram impacto na performance do modelo, especialmente nas **métricas por classe**. O uso dessas técnicas é essencial quando lidamos com bases de dados desbalanceadas, principalmente em problemas multiclasse.

---

## 👨‍💻 Autor

Matheus — Estudante de Análise e Desenvolvimento de Sistemas, com foco em Ciência de Dados.
