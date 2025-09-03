import streamlit as st

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

# Configurações do Streamlit

st.set_page_config(page_title="Seu assistente virtual", page_icon="🤖")
st.title("Seu assistente virtual 🤖")

model_class = "gemma2-9b-it"  # moonshotai/kimi-k2-instruct

def model(model="gemma2-9b-it", temperature=0.6):
    llm = ChatGroq(
        model=model,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
        temperature=temperature,
    )

    return llm


def model_response(user_query, chat_history, model_class):

    # Carregamento da LLM
    if model_class == "gemma2-9b-it":
        llm = model(model="gemma2-9b-it")
    elif model_class == "moonshotai/kimi-k2-instruct":
        llm = model(model="moonshotai/kimi-k2-instruct")

    # Definição dos prompts

    language = "português"
    system_prompt = "Você é um assistente prestativo e está respondendo perguntas gerais. Responda em {language}"

    # Adequando a pipline
    user_prompt = "{input}"

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", user_prompt),
        ]
    )

    # Criação da chain

    chain = prompt_template | llm | StrOutputParser()

    # Retorno da resposta

    return chain.stream(
        {"chat_history": chat_history, "input": user_query, "language": language}
    )


# Criando nova sessão
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Olá, sou o seu assistente virtual! Como posso ajuda você")
    ]

# Recuperando messagens
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

user_query = st.chat_input("Digite sua mensagem aqui...")

if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        resp = st.write_stream(model_response(user_query,
                                              st.session_state.chat_history,
                                              model_class))
    st.session_state.chat_history.append(AIMessage(content = resp))
