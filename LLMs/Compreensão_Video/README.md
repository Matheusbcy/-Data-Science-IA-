# 📺 Projeto — Transcrição e Compreensão de Vídeos com LLMs

Este projeto tem como objetivo transcrever vídeos do YouTube e utilizar modelos de linguagem (LLMs) para gerar respostas baseadas no conteúdo transcrito. A aplicação é ideal para resumos, explicações e extração de tópicos importantes de vídeos longos.

---

## ⚙️ Instalação e Configuração

Antes de executar o notebook, é necessário instalar algumas bibliotecas:

- `langchain`, com suporte a `huggingface`, `ollama`, `openai`, `groq`
- `youtube-transcript-api` para extrair a transcrição dos vídeos
- `pytube` para obter metadados dos vídeos
- Bibliotecas auxiliares: `requests`, `bs4`, `getpass`, `IPython.display`, entre outras

---

## 📥 Coleta de Transcrição

O processo de transcrição envolve:

- Extração do ID do vídeo a partir da URL
- Coleta da transcrição com suporte multilíngue (português e inglês)
- Unificação do texto em um único bloco contínuo, removendo quebras de linha
- Salvamento do conteúdo transcrito em um arquivo `.txt`

---

## ℹ️ Coleta de Metadados

O projeto também captura:

- Título do vídeo via scraping com BeautifulSoup
- Geração de uma estrutura contendo o título e a transcrição para facilitar o input no LLM

---

## 🤖 Integração com LLM

- Utilização do modelo `gemma-2-9b-it` via `ChatGroq`
- Configuração com temperatura ajustável
- Criação de um prompt personalizado com template baseado na transcrição e na consulta do usuário
- Geração de uma `chain` LangChain para estruturar o fluxo entre prompt e resposta

---

## 💬 Exemplos de Consultas

O modelo pode responder a diversas perguntas com base na transcrição do vídeo, como:

- `resuma`
- `summarize de forma clara de entender em pt-br`
- `explique em 1 frase sobre o que fala esse vídeo`
- `liste os temas desse vídeo`
- `liste os temas desse vídeo, resposta em português brasil, utilize bullet points`

---

## ✅ Requisitos

- Conta no Groq com chave de API válida (`GROQ_API_KEY`)
- Python 3.10+
- Acesso à internet para baixar vídeos/transcrições

---

## 📌 Objetivos de Aprendizado

- Integrar transcrição de vídeos com processamento de linguagem natural
- Utilizar LLMs para extrair, resumir e interpretar informações
- Automatizar tarefas de entendimento de vídeos educacionais, tutoriais ou jogos

---

## 🚀 Próximos Passos

- Suporte a múltiplos vídeos em lote
- Geração automática de resumos em PDF
- Classificação de sentimentos com base no conteúdo transcrito
- Interface gráfica para facilitar o uso

---

## 🧑‍💻 Autor

Matheus — Estudante de Análise e Desenvolvimento de Sistemas com foco em Ciência de Dados e IA.
****
