from langchain_community.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import GPT4AllEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_documents_from_web(url: str):
    try:
        loader = WebBaseLoader(url)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        documents = text_splitter.split_documents(docs)
        logger.info(f"Successfully loaded {len(documents)} document(s) from {url}.")
        
        return documents

    except ValueError as ve:
        logger.error(f"ValueError while loading URL: {url} - {str(ve)}")
        raise
    except Exception as e:
        logger.error(f"Error while loading documents from URL {url}: {str(e)}")
        raise
