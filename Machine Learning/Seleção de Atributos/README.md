# 🌳 Seleção de Atributos  

## 📘 Descrição

Este exercício teve como foco a aplicação de técnicas de **seleção de atributos** com o objetivo de melhorar o desempenho de algoritmos de classificação e reduzir a dimensionalidade dos dados. Foram utilizadas duas abordagens principais: **eliminação por baixa variância** e **seleção baseada na importância dos atributos** com o modelo `ExtraTreesClassifier`.

## 📂 Base de Dados

A base utilizada foi a de **cobertura vegetal**, previamente tratada em exercícios anteriores. Para esta etapa:

- Foram removidas as **colunas categóricas**, pois o método de variância é voltado para atributos numéricos.
- O conjunto de dados foi escalado com `MinMaxScaler`.
- A variável alvo foi codificada com `LabelEncoder`.

## 🧪 Etapas do Exercício

### 🔹 Preparação dos Dados

- Leitura da base de dados.
- Remoção das três últimas colunas (duas categóricas + variável alvo).
- Separação das variáveis independentes (`X`) e dependentes (`y`).
- Aplicação do escalonamento (`MinMaxScaler`) e codificação (`LabelEncoder`).
- Salvamento das variáveis `X` e `y` para uso posterior.

---

### 🔸 Seleção por Variância

- Cálculo da variância de cada atributo numérico.
- Aplicação do `VarianceThreshold` com `threshold=0.02`.
- Verificação de quais atributos foram mantidos.
- Separação dos dados em treino e teste.
- Treinamento de um `RandomForestClassifier`.
- Avaliação do desempenho com métricas de acurácia.

📉 Resultado: o modelo teve desempenho inferior ao modelo treinado com todos os atributos, indicando que atributos de baixa variância e até mesmo os categóricos excluídos possuem valor preditivo.

---

### 🔸 Seleção por Importância com ExtraTreesClassifier

- Treinamento de um `ExtraTreesClassifier` com todos os atributos para avaliação da importância de cada um.
- Seleção dos atributos com importância superior a `0.07`.
- Filtragem da base `X` com base nesses atributos.
- Separação dos dados em treino e teste.
- Novo treinamento com `RandomForestClassifier`.
- Avaliação da acurácia.

📈 Resultado: o desempenho foi **melhor do que o modelo baseado em variância**, porém **ainda inferior ao modelo com todos os atributos**.

---

## ✅ Conclusão

A seleção de atributos pode ajudar a reduzir a dimensionalidade, simplificar modelos e reduzir overfitting. No entanto, neste caso específico:

- **A seleção por variância removeu atributos importantes**, resultando em perda de desempenho.
- **A seleção por importância se saiu melhor**, mas ainda **não superou o uso da base completa**.

Esse exercício mostra que a redução de dimensionalidade deve ser feita com critério, e nem sempre menos atributos resultam em modelos melhores.

## 👨‍💻 Autor

Matheus — Estudante de Análise e Desenvolvimento de Sistemas, com foco em Ciência de Dados.
