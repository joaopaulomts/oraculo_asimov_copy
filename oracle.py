from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings  # Atualizado para o novo pacote
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnablePassthrough

_ = load_dotenv()

# 1. Carregar o conjunto de dados
loader = CSVLoader(file_path="knowledge_base.csv")
documents = loader.load()

# Usar embeddings locais com SentenceTransformers
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(documents, embeddings)
retriever = vectorstore.as_retriever()

# Usar o modelo local com Ollama
llm = Ollama(model="deepseek-r1")

rag_template = """
Você é um atendente de uma empresa.
Seu trabalho é conversar com os clientes, consultando a base de dados da empresa, e dar uma resposta simples e precisa para ele, baseada na base de dados da empresa fornecida como contexto.

Contexto: {context}

Pergunta do cliente: {question}

"""
prompt = ChatPromptTemplate.from_template(rag_template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
)

# Invocar a cadeia com uma pergunta
response = chain.invoke("Quais são os melhores processadores para games e por que?")
print(response)