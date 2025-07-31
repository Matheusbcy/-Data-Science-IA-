# 📚 Manual ERP - Assistente Virtual com ChatGPT e Streamlit 🤖

## 📝 Descrição

Este projeto consiste em um assistente virtual construído com Streamlit e modelos de linguagem para responder perguntas baseadas no conteúdo de um manual em formato PDF. O usuário pode digitar suas dúvidas e receber respostas contextualizadas e detalhadas, com base no texto do manual previamente processado.

O sistema utiliza técnicas de processamento de linguagem natural, incluindo:

- 📄 Leitura e segmentação do PDF em blocos de texto (chunks).
- 🧠 Geração de embeddings para os chunks de texto com modelos pré-treinados.
- 🔍 Indexação e recuperação de informações relevantes via vetorstore.
- 💬 Uso de um modelo de linguagem (ChatGroq) para gerar respostas baseadas no contexto recuperado e no histórico da conversa.

## 🚀 Funcionalidades

- 🖥️ Interface web simples e interativa com Streamlit.
- 🗂️ Suporte a histórico de conversas, permitindo diálogos contextuais.
- ✍️ Respostas detalhadas, claras e em português.
- 📦 Carregamento e divisão automática do manual em pedaços para melhor recuperação de informações.

## 🎯 Como usar

1. Abra a aplicação Streamlit.
2. Digite sua pergunta na caixa de chat.
3. Aguarde a resposta gerada com base no manual ERP.

## 🛠️ Tecnologias usadas

- 🐍 Python
- ⚡ Streamlit
- 🔗 LangChain
- 🤗 HuggingFace Embeddings
- 📚 Chroma Vectorstore
- 🤖 Modelos ChatGroq

## 🔧 Melhorias Futuras

- 💾 **Cache do vetorstore:** Salvar a indexação dos documentos para evitar recarregamento a cada consulta, melhorando performance.
- 🎨 **Interface aprimorada:** Adicionar indicadores de carregamento, opção para reiniciar o chat e melhor visualização do histórico.
- 🧩 **Modularização do código:** Separar funções em módulos para facilitar manutenção e escalabilidade.
- ⚙️ **Parâmetros configuráveis externamente:** Usar arquivos de configuração para ajustar modelos, temperatura e parâmetros do chatbot.
- 🚨 **Tratamento de erros:** Implementar capturas de exceções e mensagens amigáveis para o usuário.
- ✂️ **Limitar o histórico:** Evitar que o prompt fique muito grande e cause lentidão.
- ✍️ **Melhoria dos prompts:** Tornar as instruções ao modelo mais dinâmicas e específicas para diferentes tipos de perguntas.
- 🔐 **Segurança:** Validação e sanitização das entradas do usuário, além de controles de acesso para a aplicação.
- 🌍 **Suporte a múltiplos idiomas:** Tornar o assistente mais acessível para usuários de diferentes línguas.
