# ⚡ Aceleração de Data Science e Machine Learning com GPU

Este repositório apresenta exemplos, notebooks e projetos práticos que demonstram como acelerar o processamento de dados e o treinamento de modelos de Machine Learning utilizando **GPU** com a plataforma **RAPIDS**, da NVIDIA.

O conteúdo explora a utilização das bibliotecas **cuDF, cuPy e cuML** como substitutas de **Pandas, NumPy e Scikit-Learn**, além da integração com **DASK** para paralelismo e escalabilidade.

---

## 🎯 Objetivo do Repositório

Demonstrar, na prática:

- Como migrar projetos tradicionais em Python (CPU) para versões aceleradas em GPU
- Como utilizar as bibliotecas RAPIDS para manipulação de dados e treinamento de modelos
- Como comparar o desempenho entre CPU vs GPU
- Como aplicar paralelismo em múltiplas GPUs com DASK

---

## 🚀 Principais Tecnologias

| Biblioteca | Equivalente Tradicional | Função Principal |
|------------|-------------------------|------------------|
| cuDF       | Pandas                  | DataFrames em GPU |
| cuPy       | NumPy                   | Operações numéricas e matriciais |
| cuML       | Scikit-Learn            | Machine Learning acelerado na GPU |
| DASK       | Multiprocessing / Spark | Processamento paralelo e distribuído |

---

## 🧪 Conteúdos Demonstrados

### 🔹 Processamento Acelerado
- Comparação de velocidade entre **Pandas x cuDF**
- Conversão automática de DataFrames para execução em GPU

### 🔹 Machine Learning com GPU
- Classificação e regressão com cuML
- Comparativo de tempo: Scikit-Learn (CPU) vs cuML (GPU)
- Pipelines completos de ML utilizando GPU

### 🔹 Paralelismo com DASK
- Execução distribuída e paralela de tarefas
- Integração com cuDF e cuML em múltiplas GPUs

---

## ⚙️ Como Executar

1️⃣ Utilize **Google Colab com GPU ativada**  
> *Runtime → Change runtime type → GPU*

2️⃣ Instale a stack RAPIDS dentro do notebook (comandos incluídos nos notebooks)

3️⃣ Execute os notebooks na ordem proposta para entender a evolução CPU → GPU → Paralelismo

---

## ⚡ Principais Benefícios Comprovados

| Cenário | CPU (Pandas / Sklearn) | GPU (cuDF / cuML) |
|--------|-------------------------|-------------------|
| Carga e tratamento de dados | Médio | Muito rápido |
| Treinamento de modelos | Lento | Até **900x mais rápido** |
| Execução em paralelo | Limitada | Escalável com DASK |

> Em alguns experimentos observados, tarefas que levariam **horas na CPU** foram executadas em **minutos ou segundos na GPU**.

---

## 🤝 Como Contribuir

- Experimentos de desempenho com outros modelos
- Adição de notebooks com novos algoritmos em GPU
- Integração com PyTorch, TensorFlow ou Spark

Pull requests são bem-vindos!

---
