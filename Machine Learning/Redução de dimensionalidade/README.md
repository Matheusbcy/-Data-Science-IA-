# Parte 5.6 - Tópicos complementares - Redução de dimensionalidade

## Carregar dados

Importe as bibliotecas necessárias para manipulação de dados, redução de dimensionalidade, classificação e avaliação.

---

## Introdução

Utilizaremos a base de dados de cobertura vegetal, já processada e armazenada no arquivo `cover_type_num.pkl`.  
Este arquivo contém duas variáveis principais:  
- `X`: atributos numéricos normalizados  
- `y`: variável alvo codificada com LabelEncoder

---

## Carregar dados

Carregue as variáveis `X` e `y` a partir do arquivo salvo no Drive.

---

## Visualizar os dados

Confira o formato (shape) das variáveis `X` e `y` para entender o tamanho e as dimensões da base.

---

## Dividir os dados em treino e teste

Separe os dados, destinando 25% para teste e 75% para treino.  
Garanta que a divisão seja estratificada para manter a proporção das classes em ambos os conjuntos.

---

## PCA - Análise de Componentes Principais

- Instancie o PCA com 6 componentes principais.  
- Aplique o PCA nos dados de treino e teste.  
- Verifique o formato das variáveis transformadas.  
- Analise a variância explicada por cada componente e a soma total dessa variância.

---

## Treinamento e avaliação com Random Forest (PCA)

- Crie um classificador Random Forest com 40 árvores.  
- Treine o classificador usando os dados transformados pelo PCA.  
- Realize predições no conjunto de teste.  
- Calcule e exiba a acurácia do modelo.

---

## Kernel PCA

- Instancie o Kernel PCA com 6 componentes e kernel do tipo RBF.  
- Aplique o Kernel PCA nos dados de treino e teste.  
- Treine o classificador Random Forest com os dados transformados pelo Kernel PCA.  
- Realize predições e calcule a acurácia.

---

## Linear Discriminant Analysis (LDA)

> **Importante:** O número de componentes no LDA deve ser menor ou igual ao número de classes menos 1. Para duas classes, use 1 componente.

- Instancie o LDA com o número correto de componentes.  
- Aplique o LDA nos dados de treino e teste.  
- Treine o classificador Random Forest com os dados transformados pelo LDA.  
- Faça as predições e calcule a acurácia.

---

## Resumo

Neste exercício, aplicamos três técnicas de redução de dimensionalidade:

- **PCA:** método linear que reduz dimensões explicando a maior variância dos dados.  
- **Kernel PCA:** técnica não linear que usa funções kernel para capturar relações complexas.  
- **LDA:** técnica supervisionada que maximiza a separação entre as classes.


