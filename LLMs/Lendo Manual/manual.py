import streamlit as st
import time

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()

st.set_page_config(page_title="Manual", page_icon="📚")
st.title("Converse com seu Manual📚")

user_query = st.chat_input("Digite sua mensagem aqui..")

model_class = "gemma2-9b-it"

def model(model="gemma2-9b-it", temperature=0.6):
    llm = ChatGroq(
        model=model,
        max_tokens=1024,
        timeout=None,
        max_retries=2,
        temperature=temperature,
    )

    return llm

def config_retriever(uploads):
    loader = PyPDFLoader(uploads)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, separators=["\n\n", "\n", ".", " ", ""]
    )
    splits = text_splitter.split_documents(docs)
    st.write(f"Total de chunks: {len(splits)}")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

    retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 6})

    return retriever


def config_chain(model_class, retriever):
    llm = model(model=model_class)

    token_s, token_e = "", ""

    context_q_system_prompt = "You are a helpful, intelligent assistant who responds to user questions, based only on the context provided below. Always explain your answers with clarity and detail, and provide step-by-step reasoning when relevant. If the user’s question is technical, use concise code snippets, and explain them. If there is missing context, politely state that more information is needed."
    context_q_system_prompt = token_s + context_q_system_prompt
    context_q_user_prompt = "Question: {input}" + token_e
    context_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", context_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", context_q_user_prompt),
        ]
    )
    history_aware_retriever = create_history_aware_retriever(
        llm=llm, retriever=retriever, prompt=context_q_prompt
    )

    qa_prompt_template = """Você é um assistente virtual prestativo e está respondendo perguntas gerais.
    Use os seguintes pedaços de contexto recuperado para responder a perguntas.
    Se você não sabe a resposta, apenas diga que não sabe. Mantenha a resposta concisa.
    Responsa detalhadamento cada pergunta, Responda em português.  \n\n
    Pergunta: {input} \n
    Contexto: {context}
    """

    qa_prompt = PromptTemplate.from_template(token_s + qa_prompt_template + token_e)

    qa_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)

    return rag_chain


if "retriever" not in st.session_state:
    st.session_state.retriever = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Olá, sou o seu assistente virtual! Como posso ajuda você")
    ]

for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

start = time.time()

if user_query is not None and user_query != "":
    with st.chat_message("Human"):
        st.markdown(user_query)

    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("AI"):
        if st.session_state.retriever is None:
            st.session_state.retriever = config_retriever("T22182C.pdf")

        chain_rag = config_chain(model_class, st.session_state.retriever)
        result = chain_rag.invoke(
            {"input": user_query, "chat_history": st.session_state.chat_history}
        )
        resp = result["answer"]
        st.write(resp)

        st.session_state.chat_history.append(AIMessage(content=resp))


end = time.time()

print("Tempo: ", end - start)
