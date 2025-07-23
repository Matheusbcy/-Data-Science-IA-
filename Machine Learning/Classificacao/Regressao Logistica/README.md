# Aprendizado Supervisionado - Regressão Logística

Este repositório contém um exercício prático utilizando o algoritmo de **Regressão Logística** para classificação, com base em um dataset salvo no arquivo `cover_type.pkl`. O exercício faz parte do curso de Machine Learning da IA Expert Academy.

---

## 📁 Estrutura

- `cover_type.pkl`: Arquivo com os dados já processados, contendo os splits de treino e teste.
- `regressao_logistic.ipynb`: Notebook Jupyter com o código completo de carregamento, treinamento e avaliação do modelo.

---

## 📌 Objetivos do exercício

1. **Carregar os dados**: Separar variáveis preditoras (`X`) e o alvo (`y`), com seus respectivos splits de treino e teste.
2. **Instanciar o modelo de Regressão Logística**: Usando os parâmetros padrão:
   ```python
   from sklearn.linear_model import LogisticRegression

   modelo = LogisticRegression()
3. **Fazer previsões**: Utilizando o split de teste.
   ```python
   y_pred = modelo.predict(X_test)
4. **Avaliar o desempenho do modelo:**
## 📊 Avaliar o desempenho do modelo

```python
# Acurácia
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2f}")

# Matriz de Confusão
matriz = confusion_matrix(y_test, y_pred)
print("Matriz de Confusão:")
print(matriz)

# Relatório de Classificação
print("Relatório de Classificação:")
print(classification_report(y_test, y_pred))

# Visualização (opcional com Yellowbrick)
from yellowbrick.classifier import ConfusionMatrix

cm = ConfusionMatrix(modelo)
cm.fit(X_train, y_train)
cm.score(X_test, y_test)

## 🛠️ Bibliotecas utilizadas

- `scikit-learn`
- `pickle`
- `yellowbrick` *(opcional para visualização)*
```

## Como executar

Clone o repositório:

```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
```
Instale as dependências:
```bash
    !pip install yellowbrick
```    
Execute o jupyter notebook
```bash
    jupyter notebook logistic_regression.ipynb
```

## 📚 Créditos
Exercício desenvolvido como parte da trilha de Machine Learning da IA Expert Academy.

## 🧠 Conceitos aplicados

- Classificação supervisionada

- Regressão Logística

- Métricas de avaliação (accuracy, confusion matrix, classification report)

- Visualização com Yellowbrick
