from langchain.chains import RetrievalQA
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain.vectorstores import Chroma
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import GPT4AllEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

MODEL_NAME="llama3"

def initialize_qa_system(documents):
    # Initialize the LLM (Ollama in this case
    llm = OllamaLLM(model = MODEL_NAME)

    # Create embeddings for the documents
    embeddings = GPT4AllEmbeddings(model="gpt4all")
    #vectorstore = FAISS.from_texts(documents, embeddings)
    vectorstore = Chroma.from_documents(documents, embedding=GPT4AllEmbeddings())
    
    # Create retriever from vectorstore
    retriever = vectorstore.as_retriever()

    # Define the prompt template
    template="""
    Use the following context {context} to answer the question. If the context is not sufficient,\ 
    provide a general response, but indicating that the response has not context enough.
    
    Question: {question}

    """
    prompt = ChatPromptTemplate.from_template(template)

    qa_rag_chain=(
        {"context":retriever, "question":RunnablePassthrough()}
        |prompt
        |llm
        |StrOutputParser()
    )

    return qa_rag_chain
