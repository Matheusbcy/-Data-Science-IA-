# 🌲 Classificação com Rede Neural Artificial (MLPClassifier)

Este projeto utiliza uma rede neural artificial (MLP - Multi-Layer Perceptron) para classificar tipos de cobertura do solo com base em variáveis ambientais. Os dados vêm do arquivo `cover_type.pkl`, que deve conter os conjuntos `X`, `y`, `X_train`, `X_test`, `y_train`, `y_test`.

---

## 📁 Estrutura do Exercício

### 1. Carregamento dos dados
Carregar o arquivo `cover_type.pkl` a partir do Google Drive ou sistema local. As variáveis necessárias são:
- `X_train`, `X_test`: Dados preditores
- `y_train`, `y_test`: Rótulos de classe

### 2. Instanciação do modelo
Utilizamos `MLPClassifier` da biblioteca `sklearn.neural_network`, com os seguintes parâmetros:
- `verbose=True`
- `hidden_layer_sizes=(100, 50)`

### 3. Treinamento
Treinamento do modelo com os dados de treino utilizando o método `.fit()`.

### 4. Predição
Utilizar o método `.predict()` no conjunto de teste para obter as previsões de classe.

### 5. Avaliação do modelo
Inclui os seguintes passos:
- Cálculo da **acurácia** com `accuracy_score`
- Exibição da **matriz de confusão** com `confusion_matrix`
- Geração do **relatório de classificação** com `classification_report`

---

## 🧪 Bibliotecas utilizadas

```python
import pickle
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
```

## ✅ Resultados esperados

- Um modelo treinado com boa acurácia.
- Uma matriz de confusão clara que mostra o desempenho por classe.
- Um relatório de classificação contendo:
  - Precisão (precision)
  - Revocação (recall)
  - F1-score por classe

---

## 📌 Observações

- É altamente recomendável **normalizar os dados** (por exemplo, com `StandardScaler`) antes de treinar o MLPClassifier.
- O MLP pode ser sensível à escala dos dados e aos hiperparâmetros definidos.
- O parâmetro `verbose=True` ajuda a acompanhar a evolução do `loss` durante o treinamento.

---

## 💡 Dica Extra

- Se o modelo **demorar muito** para treinar, aumente `max_iter` ou use `early_stopping=True`.
- Se o treinamento **parar muito cedo**, tente reduzir `tol`.
- Teste diferentes arquiteturas da rede, como `hidden_layer_sizes=(100,)` ou `(100, 50, 25)`.
- Avalie também a troca do solver (`adam`, `lbfgs`, `sgd`) para encontrar o mais adequado ao seu conjunto de dados.

## 📂 Arquivo de dados

O arquivo `cover_type.pkl` deve conter os conjuntos de dados previamente salvos utilizando a biblioteca `pickle`. A estrutura esperada é a seguinte:

```python
with open('cover_type.pkl', 'rb') as f:
    X_train, X_test, y_train, y_test = pickle.load(f)
```

## 👤 Autor

- Exercício acadêmico desenvolvido para prática de classificação com redes neurais artificiais (MLP) utilizando a biblioteca scikit-learn