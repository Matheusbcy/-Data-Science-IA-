# Aprendizado Baseado em Instâncias - KNN

Este repositório contém um exercício prático utilizando o algoritmo **KNN (K-Nearest Neighbors)** para classificação, com base em um dataset salvo no arquivo `cover_type.pkl`. O exercício faz parte do curso de Machine Learning da IA Expert Academy.

---

## 📁 Estrutura

- `cover_type.pkl`: Arquivo com os dados já processados, contendo os splits de treino e teste.
- `knn.ipynb`: Notebook Jupyter com o código completo de carregamento, treinamento e avaliação do modelo.

---

## 📌 Objetivos do exercício

1. **Carregar os dados**: Separar variáveis preditoras (`X`) e o alvo (`y`), com seus respectivos splits de treino e teste.
2. **Instanciar o modelo KNN**: Usando os parâmetros padrão:
   ```python
   n_neighbors=5, p=2, metric='minkowski'
3. **Fazer previsões**: Utilizando o split de teste.
   ```python
   y_pred = knn_classifier.predict(X_test)
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

visualizer = ConfusionMatrix(knn_classifier)
visualizer.fit(X_train, y_train)
visualizer.score(X_test, y_test)
visualizer.show()

## 🛠️ Bibliotecas utilizadas

- `scikit-learn`
- `matplotlib`
- `pandas`
- `yellowbrick` *(opcional para visualização)*
```

## Como executar

Clone o repositório:

```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
```
Instale as dependências:
```bash
    pip install -r requirements.txt
```    
Execute o jupyter notebook
```bash
    jupyter notebook knn.ipynb
```

## 📚 Créditos
Exercício desenvolvido como parte da trilha de Machine Learning da IA Expert Academy.

## 🧠 Conceitos aplicados

1. Classificação supervisionada

2. Algoritmo KNN

3. Métricas de avaliação (accuracy, confusion matrix, classification report)

4. Visualização com Yellowbrick