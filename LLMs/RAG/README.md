# 📚 Projeto RAG (Retrieval-Augmented Generation) com LLM

Este projeto implementa um sistema de Geração Aumentada por Recuperação (RAG) que utiliza um Modelo de Linguagem Grande (LLM) para extrair e responder a perguntas de forma contextualizada a partir de documentos. A arquitetura RAG permite que o LLM forneça respostas mais precisas e relevantes, recuperando informações específicas de uma base de conhecimento antes de gerar a resposta final.

## ✨ Recursos

* **Processamento de Documentos:** Ingestão de documentos PDF e divisão em chunks gerenciáveis.
* **Embeddings Vetoriais:** Criação de representações vetoriais (embeddings) dos textos para busca de similaridade.
* **Banco de Dados Vetorial:** Armazenamento eficiente dos embeddings em um banco de dados vetorial (ChromaDB).
* **Recuperação de Contexto:** Capacidade de buscar e recuperar informações relevantes do banco de dados com base na pergunta do usuário.
* **Geração Aumentada:** Utilização de um LLM (ex: Llama 3) para gerar respostas informativas, enriquecidas pelo contexto recuperado.
* **Interface Simples:** Demonstração da invocação do sistema com uma pergunta direta.

--

O projeto requer um token de autenticação do Hugging Face para acessar o modelo Llama 3.

Você pode configurar isso diretamente no seu script Python, usando `os.environ["HF_TOKEN"] = getpass("Digite seu token Hugging Face: ")`. Isso solicitará o token durante a execução.

Alternativamente, você pode criar um arquivo `.env` na raiz do projeto (requer a instalação de `python-dotenv`) e adicionar a linha `HF_TOKEN="seu_token_aqui"` nele, substituindo "seu_token_aqui" pelo seu token real.

### 1. Preparar os Dados

Certifique-se de que o arquivo PDF que você deseja usar (`Perfil_Profissional_e_Pessoal_Matheus.pdf` no exemplo) esteja no caminho especificado: `/content/Perfil_Profissional_e_Pessoal_Matheus.pdf`. Você pode ajustar a variável `file_path` no código para apontar para o seu documento.

### 2. Executar o Notebook/Script

O projeto é tipicamente executado em um ambiente de notebook (Jupyter, Google Colab). Siga as células na ordem apresentada nas suas imagens originais para realizar os seguintes passos:

1.  Carregar e dividir o documento.
2.  Gerar embeddings e armazená-los no vetor store.
3.  Configurar o LLM (Llama 3).
4.  Definir o template do prompt.
5.  Criar e invocar a cadeia RAG com sua pergunta.

## ⚙️ Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **LangChain:** Framework para desenvolvimento de aplicações com LLMs.
* **Hugging Face Transformers:** Biblioteca para modelos de linguagem.
* **Llama 3:** Modelo de Linguagem Grande (LLM) utilizado para geração de texto.
* **BitsAndBytes & Accelerate:** Para quantização e otimização de modelos.
* **Sentence-Transformers:** Para geração de embeddings.
* **ChromaDB:** Banco de dados vetorial para armazenamento e busca de similaridade.
* **PyPDFLoader:** Para carregamento de documentos PDF.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request.
