from app.services.document_loader import load_documents_from_web
from app.services.qa_system import initialize_qa_system

def get_qa_response(question, url=None):
    if url:
        # Load documents from the URL
        documents = load_documents_from_web(url)
        
        # Initialize the QA system
        qa_system = initialize_qa_system(documents)
        
        # Get the answer from the system
        response = qa_system.invoke(question)
        return response
    else:
        raise ValueError("No URL provided, and no default context is available.")
