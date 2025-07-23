# 📊 Análise de Cesta de Compras com Apriori

Este projeto tem como objetivo aplicar o algoritmo **Apriori** para análise de associações entre itens comprados em conjunto em uma base de dados de transações reais. Ele faz parte de um exercício prático para consolidar conhecimentos em análise de dados, pré-processamento e mineração de dados com Python.

---

## 🗃️ Base de Dados

A base utilizada é a **Market Basket Analysis**, disponível no Kaggle no link:

[Market Basket Analysis – Kaggle](https://www.kaggle.com/datasets/aslanahmedov/market-basket-analysis)

### 📌 Informações do Dataset:
- **BillNo**: ID da transação.
- **Itemname**: Nome do produto adquirido.
- **Quantity**: Quantidade adquirida.
- **Date**: Data e hora da transação.
- **Price**: Preço unitário.
- **CustomerID**: ID do cliente.
- **Country**: País do cliente.

---

## 🔧 Etapas do Projeto

### 1. **Download e Leitura da Base**
- A base foi baixada do Kaggle.
- Foi utilizado o arquivo `.csv`, levando em consideração o delimitador `;`.

### 2. **Pré-processamento**
- Contagem de frequência de itens.
- Seleção dos itens mais frequentes (ocorrências ≥ 1000).
- Filtragem das transações com apenas os itens selecionados.
- Agrupamento por número da fatura, criando listas de itens por compra.

### 3. **Preparação para o Apriori**
- Transações organizadas como listas de listas.
- Salvamento dos dados filtrados em um arquivo `.txt` separado por `;`.

### 54. **Carregamento das Transações**
- Leitura do arquivo `.txt` em um DataFrame.
- Preenchimento de valores ausentes.
- Conversão para estrutura compatível com o algoritmo Apriori.

---

## 📈 Mineração de Regras de Associação

### 🔍 Parâmetros do Algoritmo Apriori:
- **min_support**: 0.02
- **min_confidence**: 0.25
- **min_lift**: 5

Após a execução, o conjunto de regras geradas foi organizado em um DataFrame com os seguintes atributos:
- Item A (conjunto antecedente)
- Item B (conjunto consequente)
- Suporte
- Confiança
- Lift

As regras foram ordenadas de forma decrescente pelo valor de lift, priorizando as associações mais fortes.

---

## 🧠 Objetivo do Exercício

Este exercício permite praticar:
- Coleta e leitura de dados reais.
- Manipulação de dados com `pandas`.
- Filtragem e agrupamento de dados.
- Aplicação do algoritmo Apriori com a biblioteca `apyori`.
- Interpretação de regras de associação.

---

## 📁 Saídas Geradas

- Arquivo `itemlist.txt`: contém as transações filtradas e formatadas.
- DataFrame com as regras de associação extraídas, ordenadas por relevância (lift).

---

## 🧪 Requisitos

- Google Colab ou Jupyter com acesso ao Google Drive.
- Bibliotecas: `pandas`, `apyori`, `kagglehub`.

---

## ✅ Conclusão

Este exercício reforça a importância do pré-processamento de dados para algoritmos de mineração e a aplicação prática de regras de associação no contexto de negócios, como em análise de cestas de compras.
