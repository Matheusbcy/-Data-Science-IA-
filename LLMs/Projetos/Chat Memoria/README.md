# 🤖 Seu Assistente Virtual

Uma aplicação web desenvolvida com Streamlit e integrada a modelos de linguagem (LLMs) para criar um assistente virtual interativo em português.

---

## 🎥 Demonstração em Vídeo

🎬 Assista no YouTube: https://www.youtube.com/watch?v=ygDe2KKxdlI&ab_channel=MatheusFreitas 

Clique na imagem abaixo para assistir ao vídeo de demonstração no YouTube (irá te levar para outra guia)

[![Assista ao vídeo](https://img.youtube.com/vi/ygDe2KKxdlI/maxresdefault.jpg)](https://www.youtube.com/watch?v=ygDe2KKxdlI&ab_channel=MatheusFreitas)


## 📋 Descrição

Este projeto tem como objetivo fornecer um assistente virtual capaz de:

- Interagir em tempo real com o usuário
- Manter o histórico de mensagens durante a sessão
- Utilizar diferentes modelos de linguagem por meio da LangChain e da API do ChatGroq
- Responder perguntas de forma natural, clara e em português

---

## 🧠 Como Funciona

1. A aplicação é iniciada com Streamlit, configurando a interface web com título e ícone.
2. É carregado um modelo de linguagem (como gemma2-9b-it ou moonshotai/kimi-k2-instruct) usando a biblioteca LangChain.
3. Um prompt é estruturado com um histórico de mensagens e a entrada do usuário.
4. O modelo processa a entrada e gera uma resposta, que é exibida na interface.
5. O histórico é atualizado continuamente, simulando uma conversa.

---

## 🔧 Tecnologias Utilizadas

- Streamlit para interface web interativa
- LangChain Core para construção da cadeia de prompts
- ChatGroq como provedor de LLMs
- dotenv para gerenciamento de variáveis de ambiente
- Python como linguagem principal

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado.
2. Crie um arquivo `.env` com sua chave de API da Groq.
3. Execute o aplicativo com `streamlit run nome_do_arquivo.py`.
4. Acesse o endereço local exibido no terminal para usar o assistente.

---

## 📂 Estrutura da Sessão

Durante a execução:

- A conversa é armazenada em `st.session_state.chat_history`.
- As mensagens são exibidas em caixas separadas para o usuário e o assistente.
- O campo de entrada permite interações contínuas com o modelo.

---

## 💡 Possibilidades de Expansão

- Salvamento de histórico de forma persistente
- Personalização do comportamento do assistente
- Integração com bases de conhecimento ou bancos de dados externos

---

## 🧑‍💻 Autor

Este projeto foi desenvolvido com foco em experimentação e prática com modelos de linguagem e construção de interfaces amigáveis para usuários finais.

---

## 📜 Licença

Este projeto é distribuído sob uma licença de uso livre para fins educacionais e experimentais.

