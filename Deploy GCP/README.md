# 🌐 Deploy de Modelos de Machine Learning com Google Cloud Platform (GCP)

Aprenda a levar modelos de Machine Learning para **produção na nuvem**, utilizando os principais serviços da **Google Cloud Platform (GCP)**. Este repositório documenta uma jornada completa: desde o **treinamento de uma CNN localmente com Python** até o **deploy do modelo em múltiplos serviços escaláveis da GCP**, como **GCE, Cloud Run, GKE, App Engine e Cloud Functions**.

---

## 🚀 Objetivos do Projeto

- Conhecer os principais serviços da GCP:
  - Google Compute Engine (GCE)
  - App Engine (GAE)
  - Kubernetes Engine (GKE)
  - Cloud Run
  - Cloud Functions
- Entender qual serviço é ideal para cada tipo de aplicação.
- Treinar e avaliar um modelo de **CNN para classificação de imagens**.
- Construir um projeto Python local pronto para deploy.
- Implementar o modelo em múltiplos serviços da GCP.
- Aprender a **configurar ambientes**, gerenciar recursos e evitar custos desnecessários com a **limpeza pós-deploy**.

---

## 📚 Descrição

O deploy de modelos de Machine Learning é o passo que transforma uma solução teórica em uma **aplicação real, escalável e acessível por usuários**. É nessa etapa que os modelos passam a gerar valor, sendo conectados a sistemas, APIs e interfaces web.

Este projeto/cuso aborda:

- Preparação do ambiente local
- Treinamento de uma CNN com TensorFlow/Keras
- Criação de uma API Python para servir o modelo
- Deploy em diferentes serviços da GCP
- Comparação entre as opções (custos, escalabilidade, complexidade)

Ao final, você terá uma **aplicação web funcional de classificação de imagens** rodando na nuvem, com deploy profissional.

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologias |
|-----------|-------------|
| Linguagem | Python |
| Framework ML | TensorFlow / Keras |
| Web/API | Flask ou FastAPI |
| Nuvem | Google Cloud Platform |
| Containerização | Docker |
| Deploy | GCE, GAE, Cloud Run, GKE, Cloud Functions |

---

## 🧪 Etapas do Projeto

### 1️⃣ Treinamento do Modelo (Local)
- Importação de dados (Dataset de imagens)
- Construção da CNN com Keras
- Treinamento e avaliação
- Exportação do modelo (`model.h5`)

### 2️⃣ Criação da API Python
- Criação de endpoint para previsão de imagens
- Tratamento de upload de arquivos
- Resposta com classe prevista

### 3️⃣ Deploy em diferentes serviços GCP
| Serviço | Perfil Ideal |
|---------|-------------|
| Cloud Run | APIs containerizadas com escalabilidade automática |
| App Engine | Aplicações web simples e leves |
| Compute Engine | Maior controle da infraestrutura |
| Kubernetes Engine | Projetos complexos e escaláveis com múltiplos containers |
| Cloud Functions | Funções event-driven com baixo custo |

---

## 🧠 Conceitos Aprendidos

✔ Diferenças entre serviços da GCP  
✔ Como escolher o serviço adequado para seu projeto  
✔ Criação de APIs com Flask/FastAPI  
✔ Containerização com Docker  
✔ Deploy com Cloud Run, GAE, GKE, GCF e GCE  
✔ Gerenciamento de custos e limpeza automática de recursos  

---

## 💡 Resultado Esperado

Ao final, você terá:

✔ Um modelo de CNN treinado para classificação de imagens  
✔ Uma API funcional servindo o modelo  
✔ Deploy realizado com sucesso em múltiplos serviços da GCP  
✔ Controle dos custos e limpeza dos recursos pós-deploy  
✔ Entendimento do ciclo completo da solução: **Treinar → Construir → Deploy → Escalar**

---
